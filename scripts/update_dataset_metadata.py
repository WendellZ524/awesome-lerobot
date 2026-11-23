#!/usr/bin/env python3
"""Refresh Hugging Face download sizes in README.md where size slots exist.

The source of truth for dataset links is datasets.json. Download size means the
same total byte count shown by the Hugging Face "Files and versions" page as
"Total file size".
"""

from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = ROOT / "datasets.json"
DEFAULT_README = ROOT / "README.md"
HF_BASE = "https://huggingface.co/datasets"


SIZE_RE = re.compile(r'\{"size":(\d+)\};')
SIZE_LINE_RE = re.compile(r"(?m)^(- 📦 Size: ).*$")
INLINE_RE_TEMPLATE = (
    r"(\[[^\]]+]\(https://huggingface\.co/datasets/{}\):\s*)"
    r"([0-9.]+ (?:TB|GB|MB|kB|B))"
)


def load_dataset_ids(path: Path) -> list[str]:
    payload = json.loads(path.read_text())
    entries = payload.get("huggingface_datasets", [])
    ids = []
    for entry in entries:
        dataset_id = entry.get("id")
        if not dataset_id:
            raise ValueError(f"Missing dataset id in {path}")
        ids.append(dataset_id)
    if len(ids) != len(set(ids)):
        raise ValueError(f"Duplicate dataset ids in {path}")
    return ids


def fetch_text(url: str, token: str | None = None, timeout: int = 30) -> str:
    headers = {
        "User-Agent": "awesome-lerobot-metadata/1.0",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read().decode("utf-8", errors="replace")


def fetch_download_size(dataset_id: str, token: str | None = None) -> int:
    url = f"{HF_BASE}/{dataset_id}/tree/main"
    text = fetch_text(url, token=token)
    decoded = html.unescape(text)
    matches = SIZE_RE.findall(decoded)
    if not matches:
        raise ValueError(f"Could not find Total file size field in {url}")
    return int(matches[-1])


def format_size(num_bytes: int) -> str:
    if num_bytes == 0:
        return "0 B"
    units = [
        ("TB", 1_000_000_000_000),
        ("GB", 1_000_000_000),
        ("MB", 1_000_000),
        ("kB", 1_000),
    ]
    for unit, factor in units:
        if num_bytes >= factor:
            return f"{num_bytes / factor:.2f} {unit}"
    return f"{num_bytes} B"


def update_checked_date(text: str, checked_date: str) -> str:
    return re.sub(
        r"Values below were checked on \d{4}-\d{2}-\d{2}\.",
        f"Values below were checked on {checked_date}.",
        text,
    )


def replace_inline_size(text: str, dataset_id: str, size: str) -> tuple[str, int]:
    escaped_url = re.escape(dataset_id)
    pattern = re.compile(INLINE_RE_TEMPLATE.format(escaped_url))
    return pattern.subn(rf"\g<1>{size}", text)


def replace_block_size(text: str, dataset_id: str, size: str) -> tuple[str, int]:
    url = f"https://huggingface.co/datasets/{dataset_id}"
    marker = f"]({url})"
    pos = text.find(marker)
    if pos < 0:
        return text, 0
    next_heading = text.find("\n### ", pos)
    if next_heading < 0:
        next_heading = len(text)
    block = text[pos:next_heading]

    size_match = SIZE_LINE_RE.search(block)
    if size_match and (
        "Original" in size_match.group(0) or "community" in size_match.group(0)
    ):
        return text, 0
    if block.count("https://huggingface.co/datasets/") > 1 and size_match:
        return text, 0

    updated, count = SIZE_LINE_RE.subn(
        rf"\g<1>{size} download size on Hugging Face.", block, count=1
    )
    if count == 0:
        return text, 0
    return text[:pos] + updated + text[next_heading:], count


def has_documented_size_gap(text: str, dataset_id: str) -> bool:
    marker = f"https://huggingface.co/datasets/{dataset_id}"
    pos = text.find(marker)
    if pos < 0:
        return False
    context = text[max(0, pos - 300) : min(len(text), pos + 700)]
    return "Total file size unavailable" in context or "`usedStorage`" in context


def update_readme(
    text: str, sizes: dict[str, str], checked_date: str
) -> tuple[str, list[str], list[str]]:
    text = update_checked_date(text, checked_date)
    missing = []
    skipped = []
    for dataset_id, size in sizes.items():
        text, count = replace_inline_size(text, dataset_id, size)
        if count:
            continue
        text, count = replace_block_size(text, dataset_id, size)
        if count == 0:
            marker = f"https://huggingface.co/datasets/{dataset_id}"
            if marker in text:
                skipped.append(dataset_id)
            else:
                missing.append(dataset_id)
    return text, missing, skipped


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--readme", type=Path, default=DEFAULT_README)
    parser.add_argument("--write", action="store_true", help="Write README.md in place.")
    parser.add_argument(
        "--checked-date",
        default=dt.date.today().isoformat(),
        help="Date to write into README metadata text.",
    )
    parser.add_argument(
        "--token-env",
        default="HF_TOKEN",
        help="Environment variable containing a Hugging Face token, if needed.",
    )
    parser.add_argument(
        "--only",
        nargs="*",
        help="Optional subset of dataset ids to refresh.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    token = None
    if args.token_env:
        import os

        token = os.environ.get(args.token_env)

    dataset_ids = load_dataset_ids(args.source)
    if args.only:
        wanted = set(args.only)
        unknown = sorted(wanted.difference(dataset_ids))
        if unknown:
            print(f"Unknown dataset ids: {', '.join(unknown)}", file=sys.stderr)
            return 2
        dataset_ids = [dataset_id for dataset_id in dataset_ids if dataset_id in wanted]

    readme_text = args.readme.read_text()

    sizes: dict[str, str] = {}
    failures: dict[str, str] = {}
    known_size_gaps: dict[str, str] = {}
    for dataset_id in dataset_ids:
        try:
            num_bytes = fetch_download_size(dataset_id, token=token)
        except (urllib.error.URLError, TimeoutError, ValueError) as exc:
            if has_documented_size_gap(readme_text, dataset_id):
                known_size_gaps[dataset_id] = str(exc)
                continue
            failures[dataset_id] = str(exc)
            continue
        sizes[dataset_id] = format_size(num_bytes)
        print(f"{dataset_id}: {sizes[dataset_id]}")

    updated, missing, skipped = update_readme(readme_text, sizes, args.checked_date)

    if missing:
        print(
            "Dataset ids found in source but not updated in README: "
            + ", ".join(sorted(missing)),
            file=sys.stderr,
        )

    if skipped:
        print(
            "Dataset ids found as links without a refreshable size slot: "
            + ", ".join(sorted(skipped)),
            file=sys.stderr,
        )

    if failures:
        print("Failed to refresh these datasets:", file=sys.stderr)
        for dataset_id, error in sorted(failures.items()):
            print(f"- {dataset_id}: {error}", file=sys.stderr)

    if known_size_gaps:
        print("Documented size gaps kept unchanged:", file=sys.stderr)
        for dataset_id, error in sorted(known_size_gaps.items()):
            print(f"- {dataset_id}: {error}", file=sys.stderr)

    if args.write:
        args.readme.write_text(updated)
    else:
        print("Dry run only. Re-run with --write to update README.md.")

    return 1 if failures or missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
