# VLA / WAM Dataset Gap Research

Last checked: 2026-06-16.

This note tracks dataset gaps found by working backward from VLA, generalist
policy, and world/action-model papers. It is intentionally a staging document:
move a dataset into `README.md` only after confirming its publication year,
canonical source, license, and whether a LeRobot-format version exists.
Candidate Hugging Face links in this note are not added to `datasets.json`
until they are promoted into the main README.

## Search Strategy

- Start from VLA / generalist policy papers and ask which robot data they train
  on.
- Treat Open X-Embodiment (OXE) as a dataset mixture, not as one dataset. OXE
  explicitly aggregates many pre-existing robot datasets.
- Prefer direct Hugging Face dataset links when a LeRobot or raw mirror exists.
- Keep raw mirrors separate from converted LeRobot datasets.

## Evidence From Model Papers

### Open X-Embodiment / RT-X

- Source: [Open X-Embodiment project](https://robotics-transformer-x.github.io/).
- Key signal: the project says OXE standardizes and pools data from 22 robot
  embodiments, 21 institutions, and 60 existing datasets. Its public dataset
  table includes many datasets not yet represented as first-class README
  entries, including `taco_play`, `jaco_play`, `roboturk`, `language_table`,
  `bc_z`, `robo_net`, `robo_set`, `fmb`, `dobbe`, `mimic_play`, and
  `furniture_bench_dataset`.
- Implication for this repo: `Open X-Embodiment` should stay as an umbrella
  entry, but high-value component datasets should be tracked individually when
  they have public raw or LeRobot repositories.

### OpenVLA

- Source: [OpenVLA arXiv](https://arxiv.org/abs/2406.09246).
- Key signal: OpenVLA reports training on 970k real-world robot demonstrations
  and built-in support for training on Open X-Embodiment datasets.
- Implication: OXE component datasets are directly relevant to VLA data
  curation, not only to the original RT-X paper.

### Octo

- Source: [Octo arXiv](https://arxiv.org/abs/2405.12213).
- Key signal: Octo reports training on 800k trajectories from Open
  X-Embodiment.
- Implication: datasets represented in OXE, especially those with public
  LeRobot conversions, are important to include or at least track.

### RT-1 / RT-2

- Sources: [RT-1 arXiv](https://arxiv.org/abs/2212.06817) and
  [RT-2 arXiv](https://arxiv.org/abs/2307.15818).
- Key signal: RT-1 emphasizes large-scale real-robot data collection, and RT-2
  co-fine-tunes VLMs on robot trajectory data and web-scale vision-language
  tasks.
- Implication: the Google / Everyday Robots / Fractal dataset line is a major
  missing source, even if the canonical release is through OXE/RLDS/HF mirrors.

### RDT-1B

- Source: [RDT-1B arXiv](https://arxiv.org/abs/2410.07864).
- Key signal: RDT-1B reports pre-training on a large multi-robot dataset
  collection and then fine-tuning on a 6K+ episode bimanual dataset.
- Implication: bimanual/dexterous datasets deserve better coverage beyond
  Mobile ALOHA and LeFranX.

### pi0 / pi0.5

- Sources: [pi0 arXiv](https://arxiv.org/abs/2410.24164) and
  [pi0.5 arXiv](https://arxiv.org/abs/2504.16054).
- Key signal: pi0 uses large and diverse robot data from multiple robot
  platforms; pi0.5 adds heterogeneous tasks, semantic prediction, web data, and
  other sources for open-world generalization.
- Implication: public OXE/LeRobot datasets are only the open part of this
  family, but they still reveal which dataset families matter.

### SmolVLA

- Source: [SmolVLA arXiv](https://arxiv.org/abs/2506.01844).
- Key signal: SmolVLA explicitly frames itself around community-collected
  affordable-robot data and releases code, pretrained models, and training data.
- Implication: this repo should track LeRobot community datasets beyond the
  official `lerobot/` organization.

## High-Priority Gaps

These are strong candidates for direct README entries or expanded
year-specific "Additional LeRobot-format datasets" sections.

| Dataset family | Why it matters | Public HF / LeRobot evidence | Current status |
| --- | --- | --- | --- |
| RT-1 / Fractal / Everyday Robots | Core data lineage for RT-1, RT-2, OXE, OpenVLA, and Octo. | [lerobot-raw/fractal20220817_data_raw](https://huggingface.co/datasets/lerobot-raw/fractal20220817_data_raw), [IPEC-COMMUNITY/fractal20220817_data_lerobot](https://huggingface.co/datasets/IPEC-COMMUNITY/fractal20220817_data_lerobot) | Added to README as an OXE component dataset. |
| Taco Play | OXE component; public LeRobot v3 version exists. | [lerobot/taco_play](https://huggingface.co/datasets/lerobot/taco_play), [IPEC-COMMUNITY/taco_play_lerobot](https://huggingface.co/datasets/IPEC-COMMUNITY/taco_play_lerobot) | Added to README as an OXE component dataset. |
| Jaco Play | OXE component; public LeRobot v3 version exists. | [lerobot/jaco_play](https://huggingface.co/datasets/lerobot/jaco_play), [IPEC-COMMUNITY/jaco_play_lerobot](https://huggingface.co/datasets/IPEC-COMMUNITY/jaco_play_lerobot) | Added to README as an OXE component dataset. |
| RoboTurk | Classic human-teleoperation manipulation dataset; OXE component. | [lerobot/roboturk](https://huggingface.co/datasets/lerobot/roboturk), [lerobot-raw/roboturk_raw](https://huggingface.co/datasets/lerobot-raw/roboturk_raw) | Added to README as an OXE component dataset. |
| FMB | OXE component; official LeRobot version exists. | [lerobot/fmb](https://huggingface.co/datasets/lerobot/fmb), [lerobot-raw/fmb_raw](https://huggingface.co/datasets/lerobot-raw/fmb_raw) | Added to README as an OXE component dataset. |
| Stanford Kuka Multimodal | OXE/Kuka lineage; official LeRobot version exists. | [lerobot/stanford_kuka_multimodal_dataset](https://huggingface.co/datasets/lerobot/stanford_kuka_multimodal_dataset), [lerobot-raw/stanford_kuka_multimodal_dataset_raw](https://huggingface.co/datasets/lerobot-raw/stanford_kuka_multimodal_dataset_raw) | Added to README as an OXE component dataset. |
| Language Table | Large OXE component with public LeRobot conversion. | [lerobot-raw/language_table_raw](https://huggingface.co/datasets/lerobot-raw/language_table_raw), [IPEC-COMMUNITY/language_table_lerobot](https://huggingface.co/datasets/IPEC-COMMUNITY/language_table_lerobot) | Added to README as an OXE component dataset. |
| FurnitureBench | OXE component; many community conversions. | [lerobot-raw/furniture_bench_dataset_raw](https://huggingface.co/datasets/lerobot-raw/furniture_bench_dataset_raw), [IPEC-COMMUNITY/furniture_bench_dataset_lerobot](https://huggingface.co/datasets/IPEC-COMMUNITY/furniture_bench_dataset_lerobot) | Added to README as an OXE component dataset. |
| DOBBE | OXE component with LeRobot community conversion. | [lerobot-raw/dobbe_raw](https://huggingface.co/datasets/lerobot-raw/dobbe_raw), [IPEC-COMMUNITY/dobbe_lerobot](https://huggingface.co/datasets/IPEC-COMMUNITY/dobbe_lerobot) | Added to README as an OXE component dataset. |
| RoboNet | Large multi-robot video dataset; OXE raw mirror exists. | [lerobot-raw/robo_net_raw](https://huggingface.co/datasets/lerobot-raw/robo_net_raw) | Added to README as raw-only OXE mirror; LeRobot conversion still needs verification. |
| RoboSet | Large multi-robot dataset; OXE raw mirror and community conversions exist. | [lerobot-raw/robo_set_raw](https://huggingface.co/datasets/lerobot-raw/robo_set_raw), [bxyjsnd/robo_set_lerobot](https://huggingface.co/datasets/bxyjsnd/robo_set_lerobot) | Raw mirror added to README; conversion provenance still needs verification. |
| BC-Z | OXE raw mirror exists; important language-conditioned robot learning lineage. | [lerobot-raw/bc_z_raw](https://huggingface.co/datasets/lerobot-raw/bc_z_raw) | Added to README as raw-only OXE mirror; LeRobot conversion still needs verification. |
| MimicPlay | Human/robot imitation-play lineage; OXE raw mirror exists. | [lerobot-raw/mimic_play_raw](https://huggingface.co/datasets/lerobot-raw/mimic_play_raw) | Added to README as raw-only OXE mirror. |
| VIOLA | OXE component with raw mirror. | [lerobot-raw/viola_raw](https://huggingface.co/datasets/lerobot-raw/viola_raw) | Added to README as raw-only OXE mirror; canonical project still needs verification. |

## HF Metadata Snapshot For Priority Candidates

Values below come from Hugging Face public API and `meta/info.json` where
available. `usedStorage` is not always the same as the Files page "Total file
size"; confirm again before moving into `README.md`.

| HF repo | Storage / size signal | Duration signal | License signal |
| --- | --- | --- | --- |
| [lerobot/taco_play](https://huggingface.co/datasets/lerobot/taco_play) | `usedStorage`: 2.37 GB | 237,798 frames at 15 FPS = 4.40 h | `cc-by-4.0` |
| [lerobot/jaco_play](https://huggingface.co/datasets/lerobot/jaco_play) | `usedStorage`: 870.13 MB | 77,965 frames at 10 FPS = 2.17 h | `cc-by-4.0` |
| [lerobot/roboturk](https://huggingface.co/datasets/lerobot/roboturk) | `usedStorage`: 4.01 GB | 187,507 frames at 10 FPS = 5.21 h | `apache-2.0` |
| [lerobot/fmb](https://huggingface.co/datasets/lerobot/fmb) | `usedStorage`: 9.10 GB | 338,188 frames at 10 FPS = 9.39 h | `apache-2.0` |
| [lerobot/stanford_kuka_multimodal_dataset](https://huggingface.co/datasets/lerobot/stanford_kuka_multimodal_dataset) | `usedStorage`: 589.11 MB | 149,985 frames at 20 FPS = 2.08 h | `mit` |
| [IPEC-COMMUNITY/fractal20220817_data_lerobot](https://huggingface.co/datasets/IPEC-COMMUNITY/fractal20220817_data_lerobot) | `usedStorage`: 21.93 GB | 3,786,400 frames at 3 FPS = 350.59 h | `apache-2.0` |
| [IPEC-COMMUNITY/language_table_lerobot](https://huggingface.co/datasets/IPEC-COMMUNITY/language_table_lerobot) | `usedStorage`: 76.52 GB | 7,045,476 frames at 10 FPS = 195.71 h | `apache-2.0` |
| [IPEC-COMMUNITY/furniture_bench_dataset_lerobot](https://huggingface.co/datasets/IPEC-COMMUNITY/furniture_bench_dataset_lerobot) | `usedStorage`: 19.64 GB | 3,948,057 frames at 10 FPS = 109.67 h | `apache-2.0` |
| [IPEC-COMMUNITY/dobbe_lerobot](https://huggingface.co/datasets/IPEC-COMMUNITY/dobbe_lerobot) | `usedStorage`: 3.56 GB | 1,139,911 frames at 3.75 FPS = 84.44 h | `apache-2.0` |
| [lerobot-raw/robo_net_raw](https://huggingface.co/datasets/lerobot-raw/robo_net_raw) | `usedStorage`: 234.84 GB | no public `meta/info.json` | not declared in HF metadata |
| [lerobot-raw/robo_set_raw](https://huggingface.co/datasets/lerobot-raw/robo_set_raw) | `usedStorage`: 191.83 GB | no public `meta/info.json` | not declared in HF metadata |
| [lerobot-raw/bc_z_raw](https://huggingface.co/datasets/lerobot-raw/bc_z_raw) | `usedStorage`: 86.48 GB | no public `meta/info.json` | not declared in HF metadata |
| [lerobot-raw/kuka_raw](https://huggingface.co/datasets/lerobot-raw/kuka_raw) | `usedStorage`: 835.41 GB | no public `meta/info.json` | not declared in HF metadata |
| [lerobot-raw/language_table_raw](https://huggingface.co/datasets/lerobot-raw/language_table_raw) | `usedStorage`: 429.36 GB | no public `meta/info.json` | not declared in HF metadata |
| [lerobot-raw/furniture_bench_dataset_raw](https://huggingface.co/datasets/lerobot-raw/furniture_bench_dataset_raw) | `usedStorage`: 123.48 GB | no public `meta/info.json` | not declared in HF metadata |

## Recommended Next README Additions

1. Add first-class entries for `RT-1 / Fractal`, `Taco Play`, `Jaco Play`,
   `RoboTurk`, `FMB`, and `Stanford Kuka Multimodal`.
2. Add a compact `Open X-Embodiment component datasets` subsection under the
   relevant year for raw-only datasets whose canonical publication year is still
   unclear.
3. For `Language Table`, `FurnitureBench`, `DOBBE`, `RoboNet`, `RoboSet`,
   `BC-Z`, `MimicPlay`, and `VIOLA`, verify canonical project pages and paper
   years before moving them into the main timeline.
4. Keep `Open X-Embodiment` as an umbrella entry, but do not let it hide its
   component datasets.
