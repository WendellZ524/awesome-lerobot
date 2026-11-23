# Dataset Metadata Maintenance

`datasets.json` is the source of truth for Hugging Face dataset repositories
tracked by this list. Add or remove dataset links there first, then update
`README.md`.

Dataset size means the download size shown by the Hugging Face repository
`Files and versions` page as `Total file size`. The updater reads that same
page and extracts the embedded total `size` value from the static HTML. Links
without a size slot in `README.md` are tracked but skipped by the updater.
If that field is not public but the Hugging Face API exposes `usedStorage`,
write it as API storage rather than as a download size.

Run a dry check:

```bash
python3 scripts/update_dataset_metadata.py
```

Update `README.md`:

```bash
python3 scripts/update_dataset_metadata.py --write
```

Refresh only selected datasets:

```bash
python3 scripts/update_dataset_metadata.py --only lerobot/aloha_mobile_chair --write
```

For private or gated datasets, set `HF_TOKEN` before running the script.
If Hugging Face does not expose the `Total file size` field in the public HTML,
leave the README size as unavailable instead of filling in a different storage
metric.
