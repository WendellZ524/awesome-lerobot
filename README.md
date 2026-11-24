# 🤖 Awesome LeRobot

A curated list of embodied AI and robot-learning datasets, with a focus on
datasets that are available in, converted to, or useful for the LeRobot format.

The list is organized by the year in which the dataset or benchmark was first
published. Primary entries separate the original or canonical data source from
known LeRobot-format releases, including community conversions and raw mirrors
when they are available.

Dataset links are tracked in [datasets.json](datasets.json). Dataset sizes use
the Hugging Face `Files and versions` page `Total file size` when it is public;
when that field is missing, the entry explicitly says if Hugging Face API
`usedStorage` was used instead. Durations are computed from Hugging Face
`meta/info.json` when both `total_frames` and `fps` are available; otherwise the
duration is marked as unavailable from public Hugging Face metadata. Values
below were checked on 2026-06-16.

Deep research notes for VLA / WAM training-data gaps are tracked in
[docs/VLA_WAM_DATASET_GAP_RESEARCH.md](docs/VLA_WAM_DATASET_GAP_RESEARCH.md).

The [Data Pyramid audit](docs/DATA_PYRAMID_COVERAGE.md) checks the November 2026 survey against this catalog. The [LeRobot conversion backlog](docs/DATA_PYRAMID_CONVERSION_GAPS.md) lists unverified releases separately, including a paper-tables-only view.

## Contents

- [2026](#2026)
- [2025](#2025)
- [2024](#2024)
- [2023](#2023)
- [Contributing](#contributing)

## 2026

### HumanCOIN

HumanCOIN pairs first-person manipulation with multiview RGB, depth, head and wrist 6-DoF poses, and step-level action and object annotations. The paper reports 12,500 hours across 38 scene classes. L1 includes inferred gaze (10,000 h), L2 adds surface EMG (2,000 h), and L3 adds EEG (500 h). L3 also measures hand pose and finger kinematics directly, making it the first tier to inspect for a hand-rig evaluation. [Paper](https://arxiv.org/abs/2611.26434) · [Project](https://flagopen.github.io/HumanCOIN/) · [Publisher directory](https://huggingface.co/HumanCOIN/datasets)

Representative task repositories: [L1](https://huggingface.co/datasets/HumanCOIN/l1_balcony_clean_task_1600x1300_30fps_2views) · [L2](https://huggingface.co/datasets/HumanCOIN/l2_dining_room_arrange_candy_left_1920x1200_30fps_9views_emg8) · [L3](https://huggingface.co/datasets/HumanCOIN/l3_beverage_shop_pour_beverage_left_1920x1184_30fps_11views_eeg128_emg8). All three list gated access and CC BY-NC 4.0. Their file indexes expose LeRobot-style metadata; the exact format version and per-joint rotation fields require access to the gated schema.


### Egocentric manipulation releases reviewed 2026-11-23

Acquisition order for wrist pose in camera coordinates and articulated hands. Start with a workbench episode; verify camera calibration, joint conventions, timestamps, visibility and rights before scaling.

| Order | Release | First useful unit and reason |
|---|---|---|
| 1 | [NVIDIA PhysicalAI-Human-1M-100K](https://huggingface.co/datasets/nvidia/PhysicalAI-Human-1M-100K) | Public 100K-hour subset of Human-1M. The card links the payload bucket; each vendor/batch/version shard is LeRobot v3. Inspect one studio stereo episode and one in-the-wild example. Confirm pose coordinate frames, joint rotations and mask semantics. CC BY 4.0. [Schema](https://huggingface.co/datasets/nvidia/PhysicalAI-Human-1M-100K/blob/main/data/schema.json) · [GR00T 2 paper](https://research.nvidia.com/labs/gear/gr00t-2/assets/gr00t2_whitepaper.pdf) |
| 2 | [Lightwheel EgoDemo](https://huggingface.co/datasets/LightwheelAI/EgoDemo) | Sample from EgoSuite-Open100K. Select EgoProStandard (wrist + hand pose) first; verify one sequence, then expand selectively to [EgoPro](https://huggingface.co/datasets/LightwheelAI/EgoPro). [EgoStandard](https://huggingface.co/datasets/LightwheelAI/EgoStandard) is secondary. Demo card lists commercial-training-no-resale-v1.0; check terms before sharing synthesized data. Demo overlaps the parent release. [Release notes](https://huggingface.co/blog/LightwheelAI/egosuite-open100k) |
| 3 | [HOT3D](https://facebookresearch.github.io/hot3d/) | Geometry benchmark for glove overlays. Start with a grasp clip with hand and object pose, render depth to test occlusion. Dataset agreement and model dependencies have separate terms. |
| 4 | [EgoVerse](https://egoverse.ai/assets/pdf/EgoVerse.pdf) | Cross-source motion diversity: 1,362 h in the cited release, 3D hand pose and camera motion. Verify per-source rights, coordinates and overlap before acquisition. |
| 5 | [EgoSteer-Egocentric](https://huggingface.co/datasets/EgoSteer/EgoSteer-Egocentric) | Derived training reference. Eight source folders in the published Hub release; distinguish estimated tracks from source annotations. Wrist and fingertips are useful for coarse motion; inspect the schema before using it for a 21-node rig. Do not add its hours to overlapping originals. |

Existing [Apple EgoDex](https://github.com/apple-aiml-research/ml-egodex) remains a local research baseline. Compare the existing community conversion against original transforms and confidence before scheduling another copy. Apple lists CC BY-NC-ND for the data.


### AIRoA MoMa Dataset

- 📄 Paper: [AIRoA MoMa Dataset: A Large-Scale Hierarchical Dataset for Mobile Manipulation](https://arxiv.org/abs/2509.25032)
- 💻 Project / repo: [airoa-moma on Hugging Face](https://huggingface.co/datasets/airoa-org/airoa-moma)
- ⬇️ Original / canonical data: [airoa-org/airoa-moma](https://huggingface.co/datasets/airoa-org/airoa-moma)
- 🤖 LeRobot format: Native LeRobot v2.1 format according to the dataset paper.
- 📦 Size: Hugging Face Files page `Total file size` unavailable; API
  `usedStorage` reports 191.07 GB.
- ⏱️ Duration: Not available from public metadata; `meta/info.json` requires
  authorization.
- ⚖️ License / access: Hugging Face metadata declares `cc-by-nc-sa-4.0`; access
  is gated with automatic approval.
- 📝 Notes: Mobile manipulation dataset with RGB, robot state, force-torque sensing,
  and hierarchical annotations.

### Phone2Act

- 📄 Paper: [Phone2Act: A Low-Cost, Hardware-Agnostic Teleoperation System for Scalable VLA Data Collection](https://arxiv.org/abs/2605.01948)
- 💻 Project / repo: TBD
- ⬇️ Original / canonical data: TBD
- 🤖 LeRobot format: The paper states that demonstrations are exported natively in
  LeRobot format; public dataset location still needs confirmation.
- 📦 Size: TBD; no public Hugging Face dataset confirmed.
- ⏱️ Duration: TBD; no public Hugging Face dataset confirmed.
- ⚖️ License / access: TBD.
- 📝 Notes: Teleoperation and data-collection system using a smartphone as a 6-DoF
  controller.

## 2025

### EgoDex

- 📄 Paper: [EgoDex: Learning Dexterous Manipulation from Large-Scale Egocentric Video](https://arxiv.org/abs/2505.11709)
- 💻 Project / repo: [apple/ml-egodex](https://github.com/apple/ml-egodex)
- ⬇️ Original / canonical data: Apple CDN downloads from the official repo:
  [train part 1](https://ml-site.cdn-apple.com/datasets/egodex/part1.zip),
  [part 2](https://ml-site.cdn-apple.com/datasets/egodex/part2.zip),
  [part 3](https://ml-site.cdn-apple.com/datasets/egodex/part3.zip),
  [part 4](https://ml-site.cdn-apple.com/datasets/egodex/part4.zip),
  [part 5](https://ml-site.cdn-apple.com/datasets/egodex/part5.zip),
  [test set](https://ml-site.cdn-apple.com/datasets/egodex/test.zip), and
  [additional data](https://ml-site.cdn-apple.com/datasets/egodex/extra.zip).
- 🤖 LeRobot format: Community conversion available as
  [yixuan-tan/EgoDex-LeRobot-v3.0](https://huggingface.co/datasets/yixuan-tan/EgoDex-LeRobot-v3.0).
- 📦 Size: Original Apple zip files total about 1.72 TB from the listed package
  sizes; community LeRobot conversion is 1.47 TB download size on Hugging Face.
- ⏱️ Duration: 829 h in the official dataset: about 725 h train, 7 h test, and
  97 h additional data. The community LeRobot conversion does not expose public
  `meta/info.json`.
- ⚖️ License / access: Official dataset is CC-by-NC-ND according to the Apple
  repo; public Hugging Face conversion license is not declared in HF metadata.
- 📝 Notes: Egocentric dexterous manipulation dataset collected on Apple Vision
  Pro with 30 Hz 1080p video, paired 3D head/upper-body/hand pose annotations,
  natural-language annotations, and 194 active tabletop manipulation tasks.

### LeVR / LeFranX

- 📄 Paper: [LeVR: A Modular VR Teleoperation Framework for Imitation Learning in Dexterous Manipulation](https://arxiv.org/abs/2509.14349)
- 💻 Project / repo: [wengmister/LeFranX](https://github.com/wengmister/LeFranX)
- ⬇️ Original / canonical data: [LeFranX Dataset collection](https://huggingface.co/collections/wengmister/lefranx-dataset)
  on Hugging Face, with demo-task datasets for Franka FER + Robotera XHand.
- 🤖 LeRobot format: Native LeRobot v2.1 demo datasets:
  [wengmister/toaster](https://huggingface.co/datasets/wengmister/toaster),
  [wengmister/orange_cube_pnp_with_force](https://huggingface.co/datasets/wengmister/orange_cube_pnp_with_force),
  and [wengmister/box_pnp](https://huggingface.co/datasets/wengmister/box_pnp).
- 📦 Size:
  - [wengmister/toaster](https://huggingface.co/datasets/wengmister/toaster): 365.52 MB download size on Hugging Face.
  - [wengmister/orange_cube_pnp_with_force](https://huggingface.co/datasets/wengmister/orange_cube_pnp_with_force): 199.54 MB download size on Hugging Face.
  - [wengmister/box_pnp](https://huggingface.co/datasets/wengmister/box_pnp): 391.55 MB download size on Hugging Face.
- ⏱️ Duration:
  - Total: 47.4 min from public `meta/info.json`.
  - Toaster: 17.8 min from 32,007 frames at 30 FPS.
  - Orange cube pick-and-place: 10.7 min from 19,340 frames at 30 FPS.
  - Box pick-and-place: 18.9 min from 33,943 frames at 30 FPS.
- ⚖️ License / access: Public Hugging Face datasets declare `apache-2.0`;
  LeFranX code is Apache-2.0.
- 📝 Notes: LeRobot extension for Franka FER and XHand, built around a modular VR
  teleoperation workflow with `franka_server`, `franka_xhand_teleoperator`, and
  added LeRobot robot / teleoperator classes.

### Additional 2025 LeRobot-Format Datasets

- [IPEC-COMMUNITY/FastUMI_100k_lerobot](https://huggingface.co/datasets/IPEC-COMMUNITY/FastUMI_100k_lerobot):
  Total file size unavailable from the public Files page; Hugging Face API
  `usedStorage` reports about 1.40 TB; duration unavailable because
  `meta/info.json` was not found.
- [huanbo1/pipette-lerobot-datasets](https://huggingface.co/datasets/huanbo1/pipette-lerobot-datasets):
  2.48 GB; duration unavailable because `meta/info.json` was not found.
- [TommyZihao/lerobot_zihao_dataset_shake_hands](https://huggingface.co/datasets/TommyZihao/lerobot_zihao_dataset_shake_hands):
  404.79 MB; 5.6 min from 10,113 frames at 30 FPS.

## 2024

### DROID

- 📄 Paper: [DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset](https://arxiv.org/abs/2403.12945)
- 💻 Project / repo: [droid-dataset.github.io](https://droid-dataset.github.io/)
- ⬇️ Original / canonical data: [DROID dataset project](https://droid-dataset.github.io/)
- 🤖 LeRobot format: Community / LeRobot Hub version available as
  [lerobot/droid_1.0.1](https://huggingface.co/datasets/lerobot/droid_1.0.1).
- 📦 Size: 412.01 GB download size on Hugging Face.
- ⏱️ Duration: 511.67 h from 27,630,375 frames at 15 FPS.
- ⚖️ License / access: Public Hugging Face conversion declares `apache-2.0`;
  verify original DROID terms before redistribution.
- 📝 Notes: Large-scale in-the-wild robot manipulation dataset with diverse scenes
  and tasks.

### Mobile ALOHA

- 📄 Paper: [Mobile ALOHA: Learning Bimanual Mobile Manipulation with Low-Cost Whole-Body Teleoperation](https://arxiv.org/abs/2401.02117)
- 💻 Project / repo: [mobile-aloha.github.io](https://mobile-aloha.github.io/)
- ⬇️ Original / canonical data: [Mobile ALOHA project](https://mobile-aloha.github.io/)
- 🤖 LeRobot format: Multiple ALOHA-related datasets are available under the
  `lerobot/` organization on Hugging Face.
- 📦 Size: See the LeRobot dataset variants below.
- ⏱️ Duration: See the LeRobot dataset variants below.
- ⚖️ License / access: Public Hugging Face variants; license can vary by variant,
  so verify the selected repository before reuse.
- 🤖 LeRobot dataset variants:
  - [lerobot/aloha_sim_transfer_cube_human](https://huggingface.co/datasets/lerobot/aloha_sim_transfer_cube_human): 69.88 MB; 6.7 min from 20,000 frames at 50 FPS.
  - [lerobot/aloha_sim_transfer_cube_scripted](https://huggingface.co/datasets/lerobot/aloha_sim_transfer_cube_scripted): 71.55 MB; 6.7 min from 20,000 frames at 50 FPS.
  - [lerobot/aloha_sim_insertion_human](https://huggingface.co/datasets/lerobot/aloha_sim_insertion_human): 91.35 MB; 8.3 min from 25,000 frames at 50 FPS.
  - [lerobot/aloha_sim_insertion_scripted](https://huggingface.co/datasets/lerobot/aloha_sim_insertion_scripted): 70.99 MB; 6.7 min from 20,000 frames at 50 FPS.
  - [lerobot/aloha_sim_transfer_cube_human_image](https://huggingface.co/datasets/lerobot/aloha_sim_transfer_cube_human_image): 528.32 MB; 6.7 min from 20,000 frames at 50 FPS.
  - [lerobot/aloha_sim_transfer_cube_scripted_image](https://huggingface.co/datasets/lerobot/aloha_sim_transfer_cube_scripted_image): 554.02 MB; 6.7 min from 20,000 frames at 50 FPS.
  - [lerobot/aloha_sim_insertion_human_image](https://huggingface.co/datasets/lerobot/aloha_sim_insertion_human_image): 728.26 MB; 8.3 min from 25,000 frames at 50 FPS.
  - [lerobot/aloha_sim_insertion_scripted_image](https://huggingface.co/datasets/lerobot/aloha_sim_insertion_scripted_image): 539.87 MB; 6.7 min from 20,000 frames at 50 FPS.
  - [lerobot/aloha_mobile_cabinet](https://huggingface.co/datasets/lerobot/aloha_mobile_cabinet): 1.74 GB; 42.5 min from 127,500 frames at 50 FPS.
  - [lerobot/aloha_mobile_chair](https://huggingface.co/datasets/lerobot/aloha_mobile_chair): 2.16 GB; 36.7 min from 110,000 frames at 50 FPS.
  - [lerobot/aloha_mobile_elevator](https://huggingface.co/datasets/lerobot/aloha_mobile_elevator): 583.52 MB; 15.0 min from 45,000 frames at 50 FPS.
  - [lerobot/aloha_mobile_shrimp](https://huggingface.co/datasets/lerobot/aloha_mobile_shrimp): 1.32 GB; 22.5 min from 67,500 frames at 50 FPS.
  - [lerobot/aloha_mobile_wash_pan](https://huggingface.co/datasets/lerobot/aloha_mobile_wash_pan): 1.14 GB; 18.3 min from 55,000 frames at 50 FPS.
  - [lerobot/aloha_mobile_wipe_wine](https://huggingface.co/datasets/lerobot/aloha_mobile_wipe_wine): 1.30 GB; 21.7 min from 65,000 frames at 50 FPS.
  - [lerobot/aloha_static_battery](https://huggingface.co/datasets/lerobot/aloha_static_battery): 791.31 MB; 9.8 min from 29,400 frames at 50 FPS.
  - [lerobot/aloha_static_candy](https://huggingface.co/datasets/lerobot/aloha_static_candy): 872.30 MB; 11.7 min from 35,000 frames at 50 FPS.
  - [lerobot/aloha_static_coffee](https://huggingface.co/datasets/lerobot/aloha_static_coffee): 1.57 GB; 18.3 min from 55,000 frames at 50 FPS.
  - [lerobot/aloha_static_coffee_new](https://huggingface.co/datasets/lerobot/aloha_static_coffee_new): 2.05 GB; 25.0 min from 75,000 frames at 50 FPS.
  - [lerobot/aloha_static_cups_open](https://huggingface.co/datasets/lerobot/aloha_static_cups_open): 509.17 MB; 6.7 min from 20,000 frames at 50 FPS.
  - [lerobot/aloha_static_fork_pick_up](https://huggingface.co/datasets/lerobot/aloha_static_fork_pick_up): 1.53 GB; 20.0 min from 60,000 frames at 50 FPS.
  - [lerobot/aloha_static_screw_driver](https://huggingface.co/datasets/lerobot/aloha_static_screw_driver): 531.69 MB; 6.7 min from 20,000 frames at 50 FPS.
  - [lerobot/aloha_static_tape](https://huggingface.co/datasets/lerobot/aloha_static_tape): 868.36 MB; 11.7 min from 35,000 frames at 50 FPS.
  - [lerobot/aloha_static_thread_velcro](https://huggingface.co/datasets/lerobot/aloha_static_thread_velcro): 143.53 MB; 11.4 min from 34,300 frames at 50 FPS.
  - [lerobot/aloha_static_towel](https://huggingface.co/datasets/lerobot/aloha_static_towel): 591.69 MB; 8.3 min from 25,000 frames at 50 FPS.
  - [lerobot/aloha_static_vinh_cup](https://huggingface.co/datasets/lerobot/aloha_static_vinh_cup): 1.08 GB; 15.2 min from 45,500 frames at 50 FPS.
  - [lerobot/aloha_static_vinh_cup_left](https://huggingface.co/datasets/lerobot/aloha_static_vinh_cup_left): Files page `Total file size` unavailable in the latest dry run; API `usedStorage` reports 4.13 GB; 16.7 min from 50,000 frames at 50 FPS.
  - [lerobot/aloha_static_ziploc_slide](https://huggingface.co/datasets/lerobot/aloha_static_ziploc_slide): 522.08 MB; 5.6 min from 16,800 frames at 50 FPS.
  - [lerobot/aloha_static_pingpong_test](https://huggingface.co/datasets/lerobot/aloha_static_pingpong_test): 176.50 MB; 2.0 min from 6,000 frames at 50 FPS.
  - [lerobot/aloha_static_pro_pencil](https://huggingface.co/datasets/lerobot/aloha_static_pro_pencil): 528.18 MB; 2.9 min from 8,750 frames at 50 FPS.
- 📝 Notes: Bimanual mobile manipulation with whole-body teleoperation.

### UMI

- 📄 Paper: [Universal Manipulation Interface: In-The-Wild Robot Teaching Without In-The-Wild Robots](https://arxiv.org/abs/2402.10329)
- 💻 Project / repo: [umi-gripper.github.io](https://umi-gripper.github.io/)
- ⬇️ Original / canonical data: [UMI project](https://umi-gripper.github.io/)
- 🤖 LeRobot format: Community / LeRobot Hub version available as
  [lerobot/umi_cup_in_the_wild](https://huggingface.co/datasets/lerobot/umi_cup_in_the_wild).
- 📦 Size: 3.15 GB download size on Hugging Face.
- ⏱️ Duration: 19.43 h from 699,432 frames at 10 FPS.
- ⚖️ License / access: Public Hugging Face conversion declares `apache-2.0`;
  verify original UMI terms before redistribution.
- 📝 Notes: In-the-wild human demonstration collection with portable grippers.

### Additional 2024 LeRobot-Format Datasets

- xArm tasks:
  - [lerobot/xarm_lift_medium](https://huggingface.co/datasets/lerobot/xarm_lift_medium): 17.83 MB; 22.2 min from 20,000 frames at 15 FPS.
  - [lerobot/xarm_lift_medium_image](https://huggingface.co/datasets/lerobot/xarm_lift_medium_image): 78.80 MB; 22.2 min from 20,000 frames at 15 FPS.
  - [lerobot/xarm_lift_medium_replay](https://huggingface.co/datasets/lerobot/xarm_lift_medium_replay): 18.93 MB; 22.2 min from 20,000 frames at 15 FPS.
  - [lerobot/xarm_lift_medium_replay_image](https://huggingface.co/datasets/lerobot/xarm_lift_medium_replay_image): 78.80 MB; 22.2 min from 20,000 frames at 15 FPS.
  - [lerobot/xarm_push_medium](https://huggingface.co/datasets/lerobot/xarm_push_medium): 16.32 MB; 22.2 min from 20,000 frames at 15 FPS.
  - [lerobot/xarm_push_medium_image](https://huggingface.co/datasets/lerobot/xarm_push_medium_image): 78.80 MB; 22.2 min from 20,000 frames at 15 FPS.
  - [lerobot/xarm_push_medium_replay](https://huggingface.co/datasets/lerobot/xarm_push_medium_replay): 18.28 MB; 22.2 min from 20,000 frames at 15 FPS.
  - [lerobot/xarm_push_medium_replay_image](https://huggingface.co/datasets/lerobot/xarm_push_medium_replay_image): 78.80 MB; 22.2 min from 20,000 frames at 15 FPS.
- Unitree H1 tasks:
  - [lerobot/unitreeh1_fold_clothes](https://huggingface.co/datasets/lerobot/unitreeh1_fold_clothes): 965.91 MB; 6.3 min from 19,000 frames at 50 FPS.
  - [lerobot/unitreeh1_rearrange_objects](https://huggingface.co/datasets/lerobot/unitreeh1_rearrange_objects): 145.10 MB; 2.4 min from 7,150 frames at 50 FPS.
  - [lerobot/unitreeh1_two_robot_greeting](https://huggingface.co/datasets/lerobot/unitreeh1_two_robot_greeting): 82.85 MB; 1.2 min from 3,750 frames at 50 FPS.
  - [lerobot/unitreeh1_warehouse](https://huggingface.co/datasets/lerobot/unitreeh1_warehouse): 248.21 MB; 3.8 min from 11,275 frames at 50 FPS.
- Third-party conversion:
  [DexJoCo/DexJoCo-Datasets-LeRobot](https://huggingface.co/datasets/DexJoCo/DexJoCo-Datasets-LeRobot):
  34.60 GB; duration unavailable because `meta/info.json` was not found.
- Raw / original mirrors:
  - [lerobot-raw/umi_cup_in_the_wild_raw](https://huggingface.co/datasets/lerobot-raw/umi_cup_in_the_wild_raw): 17.99 GB.
  - [aloha_sim_transfer_cube_human_raw](https://huggingface.co/datasets/lerobot-raw/aloha_sim_transfer_cube_human_raw): 19.18 GB.
  - [aloha_sim_transfer_cube_scripted_raw](https://huggingface.co/datasets/lerobot-raw/aloha_sim_transfer_cube_scripted_raw): 19.18 GB.
  - [aloha_sim_insertion_human_raw](https://huggingface.co/datasets/lerobot-raw/aloha_sim_insertion_human_raw): 23.05 GB.
  - [aloha_sim_insertion_scripted_raw](https://huggingface.co/datasets/lerobot-raw/aloha_sim_insertion_scripted_raw): 19.18 GB.
  - [aloha_mobile_cabinet_raw](https://huggingface.co/datasets/lerobot-raw/aloha_mobile_cabinet_raw): 7.53 GB.
  - [aloha_mobile_chair_raw](https://huggingface.co/datasets/lerobot-raw/aloha_mobile_chair_raw): 7.97 GB.
  - [aloha_mobile_elevator_raw](https://huggingface.co/datasets/lerobot-raw/aloha_mobile_elevator_raw): 3.96 GB.
  - [aloha_mobile_shrimp_raw](https://huggingface.co/datasets/lerobot-raw/aloha_mobile_shrimp_raw): 4.16 GB.
  - [aloha_mobile_wash_pan_raw](https://huggingface.co/datasets/lerobot-raw/aloha_mobile_wash_pan_raw): 4.31 GB.
  - [aloha_mobile_wipe_wine_raw](https://huggingface.co/datasets/lerobot-raw/aloha_mobile_wipe_wine_raw): 4.65 GB.
  - [xarm_lift_medium_raw](https://huggingface.co/datasets/lerobot-raw/xarm_lift_medium_raw): 847.86 MB.
  - [xarm_lift_medium_replay_raw](https://huggingface.co/datasets/lerobot-raw/xarm_lift_medium_replay_raw): 847.86 MB.
  - [xarm_push_medium_raw](https://huggingface.co/datasets/lerobot-raw/xarm_push_medium_raw): 847.78 MB.
  - [xarm_push_medium_replay_raw](https://huggingface.co/datasets/lerobot-raw/xarm_push_medium_replay_raw): 847.78 MB.
  - [unitreeh1_fold_clothes_raw](https://huggingface.co/datasets/lerobot-raw/unitreeh1_fold_clothes_raw): 2.17 GB.
  - [unitreeh1_rearrange_objects_raw](https://huggingface.co/datasets/lerobot-raw/unitreeh1_rearrange_objects_raw): 297.05 MB.
  - [unitreeh1_two_robot_greeting_raw](https://huggingface.co/datasets/lerobot-raw/unitreeh1_two_robot_greeting_raw): 189.95 MB.
  - [unitreeh1_warehouse_raw](https://huggingface.co/datasets/lerobot-raw/unitreeh1_warehouse_raw): 699.08 MB.

## 2023

### BridgeData V2

- 📄 Paper: [BridgeData V2: A Dataset for Robot Learning at Scale](https://arxiv.org/abs/2308.12952)
- 💻 Project / repo: [rail-berkeley.github.io/bridgedata](https://rail-berkeley.github.io/bridgedata/)
- ⬇️ Original / canonical data: [BridgeData project](https://rail-berkeley.github.io/bridgedata/)
- 🤖 LeRobot format: Community conversion available as
  [nvidia/BridgeData2_LeRobot_v3](https://huggingface.co/datasets/nvidia/BridgeData2_LeRobot_v3).
- 📦 Size: 90.47 GB download size on Hugging Face.
- ⏱️ Duration: 100.06 h from 1,801,090 frames at 5 FPS.
- ⚖️ License / access: Public Hugging Face conversion; license is marked `other`
  in Hugging Face metadata.
- 📝 Notes: Large-scale low-cost robot manipulation dataset across many
  environments.

### LIBERO

- 📄 Paper: [LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning](https://arxiv.org/abs/2306.03310)
- 💻 Project / repo: [libero-project.github.io](https://libero-project.github.io/)
- ⬇️ Original / canonical data: [LIBERO project](https://libero-project.github.io/)
- 🤖 LeRobot format: Community / LeRobot Hub version available as
  [lerobot/libero_10_image](https://huggingface.co/datasets/lerobot/libero_10_image).
- 📦 Size: 12.77 GB download size on Hugging Face.
- ⏱️ Duration: 2.82 h from 101,469 frames at 10 FPS.
- ⚖️ License / access: Public Hugging Face conversion declares `apache-2.0`;
  verify original LIBERO terms before redistribution.
- 📝 Notes: Lifelong robot learning benchmark with task suites and demonstrations.

### Open X-Embodiment

- 📄 Paper: [Open X-Embodiment: Robotic Learning Datasets and RT-X Models](https://arxiv.org/abs/2310.08864)
- 💻 Project / repo: [robotics-transformer-x.github.io](https://robotics-transformer-x.github.io/)
- ⬇️ Original / canonical data: [Open X-Embodiment project page](https://robotics-transformer-x.github.io/)
- 🤖 LeRobot format: Needs verification for each converted subset.
- 📦 Size: No single Hugging Face dataset repository tracked here; verify each
  converted subset separately.
- ⏱️ Duration: No single Hugging Face dataset repository tracked here; verify
  each converted subset separately.
- ⚖️ License / access: Varies by source dataset and converted subset.
- 📝 Notes: Cross-embodiment dataset mixture assembled from many robots and
  institutions.
- 🤖 Notable public OXE component datasets:
  - RT-1 / Fractal / Everyday Robots: [lerobot-raw/fractal20220817_data_raw](https://huggingface.co/datasets/lerobot-raw/fractal20220817_data_raw) raw mirror, 119.26 GB; [IPEC-COMMUNITY/fractal20220817_data_lerobot](https://huggingface.co/datasets/IPEC-COMMUNITY/fractal20220817_data_lerobot) LeRobot conversion, API `usedStorage` 21.93 GB, 350.59 h from 3,786,400 frames at 3 FPS.
  - Taco Play: [lerobot/taco_play](https://huggingface.co/datasets/lerobot/taco_play), 1.06 GB, 4.40 h from 237,798 frames at 15 FPS; alternative [IPEC-COMMUNITY/taco_play_lerobot](https://huggingface.co/datasets/IPEC-COMMUNITY/taco_play_lerobot).
  - Jaco Play: [lerobot/jaco_play](https://huggingface.co/datasets/lerobot/jaco_play), 428.87 MB, 2.17 h from 77,965 frames at 10 FPS; raw mirror [lerobot-raw/jaco_play_raw](https://huggingface.co/datasets/lerobot-raw/jaco_play_raw), 9.92 GB.
  - RoboTurk: [lerobot/roboturk](https://huggingface.co/datasets/lerobot/roboturk), 2.00 GB, 5.21 h from 187,507 frames at 10 FPS; raw mirror [lerobot-raw/roboturk_raw](https://huggingface.co/datasets/lerobot-raw/roboturk_raw), 48.73 GB.
  - FMB: [lerobot/fmb](https://huggingface.co/datasets/lerobot/fmb), API `usedStorage` 9.10 GB, 9.39 h from 338,188 frames at 10 FPS; raw mirror [lerobot-raw/fmb_raw](https://huggingface.co/datasets/lerobot-raw/fmb_raw), 382.83 GB.
  - Stanford Kuka Multimodal: [lerobot/stanford_kuka_multimodal_dataset](https://huggingface.co/datasets/lerobot/stanford_kuka_multimodal_dataset), 280.02 MB, 2.08 h from 149,985 frames at 20 FPS; raw mirror [lerobot-raw/stanford_kuka_multimodal_dataset_raw](https://huggingface.co/datasets/lerobot-raw/stanford_kuka_multimodal_dataset_raw).
  - Language Table: [IPEC-COMMUNITY/language_table_lerobot](https://huggingface.co/datasets/IPEC-COMMUNITY/language_table_lerobot), API `usedStorage` 76.52 GB, 195.71 h from 7,045,476 frames at 10 FPS; raw mirror [lerobot-raw/language_table_raw](https://huggingface.co/datasets/lerobot-raw/language_table_raw).
  - FurnitureBench: [IPEC-COMMUNITY/furniture_bench_dataset_lerobot](https://huggingface.co/datasets/IPEC-COMMUNITY/furniture_bench_dataset_lerobot), API `usedStorage` 19.64 GB, 109.67 h from 3,948,057 frames at 10 FPS; raw mirror [lerobot-raw/furniture_bench_dataset_raw](https://huggingface.co/datasets/lerobot-raw/furniture_bench_dataset_raw), 123.48 GB.
  - DOBBE: [IPEC-COMMUNITY/dobbe_lerobot](https://huggingface.co/datasets/IPEC-COMMUNITY/dobbe_lerobot), API `usedStorage` 3.56 GB, 84.44 h from 1,139,911 frames at 3.75 FPS; raw mirror [lerobot-raw/dobbe_raw](https://huggingface.co/datasets/lerobot-raw/dobbe_raw), 19.57 GB.
  - Raw-only mirrors to verify before first-class promotion: [lerobot-raw/robo_net_raw](https://huggingface.co/datasets/lerobot-raw/robo_net_raw) 234.84 GB, [lerobot-raw/robo_set_raw](https://huggingface.co/datasets/lerobot-raw/robo_set_raw) 191.83 GB, [lerobot-raw/bc_z_raw](https://huggingface.co/datasets/lerobot-raw/bc_z_raw) 86.48 GB, [lerobot-raw/kuka_raw](https://huggingface.co/datasets/lerobot-raw/kuka_raw) 835.41 GB, [lerobot-raw/mimic_play_raw](https://huggingface.co/datasets/lerobot-raw/mimic_play_raw) 5.98 GB, and [lerobot-raw/viola_raw](https://huggingface.co/datasets/lerobot-raw/viola_raw) 11.17 GB.

### Additional 2023 LeRobot-Format Datasets

- PushT:
  - [lerobot/pusht](https://huggingface.co/datasets/lerobot/pusht): 7.69 MB; 42.8 min from 25,650 frames at 10 FPS.
  - [lerobot/pusht_image](https://huggingface.co/datasets/lerobot/pusht_image): 31.62 MB; 42.8 min from 25,650 frames at 10 FPS.
  - [lerobot/pusht_keypoints](https://huggingface.co/datasets/lerobot/pusht_keypoints): 2.25 MB; 42.8 min from 25,650 frames at 10 FPS.
  - [lerobot-raw/pusht_raw](https://huggingface.co/datasets/lerobot-raw/pusht_raw): 31.01 MB.
- LIBERO community conversion:
  [Sylvest/libero_plus_lerobot](https://huggingface.co/datasets/Sylvest/libero_plus_lerobot):
  Total file size unavailable from the public Files page; Hugging Face API
  `usedStorage` reports 7.85 GB; 31.08 h from 2,238,036 frames at 20 FPS.
- Open X-Embodiment raw mirrors:
  - [CONQ hose manipulation](https://huggingface.co/datasets/lerobot-raw/conq_hose_manipulation_raw): 2.85 GB.
  - [Tokyo U LSMO](https://huggingface.co/datasets/lerobot-raw/tokyo_u_lsmo_raw): 352.03 MB.
  - [Imperial College Sawyer wrist cam](https://huggingface.co/datasets/lerobot-raw/imperialcollege_sawyer_wrist_cam_raw): 85.86 MB.
  - [USC cloth sim](https://huggingface.co/datasets/lerobot-raw/usc_cloth_sim_raw): 266.91 MB.
  - [ASU table top](https://huggingface.co/datasets/lerobot-raw/asu_table_top_raw): 773.45 MB.
  - [CMU Franka exploration](https://huggingface.co/datasets/lerobot-raw/cmu_franka_exploration_dataset_raw): Files page `Total file size` unavailable in the latest dry run; API `usedStorage` reports 631.49 MB.
  - [CMU Stretch](https://huggingface.co/datasets/lerobot-raw/cmu_stretch_raw): Files page `Total file size` unavailable in the latest dry run; API `usedStorage` reports 763.43 MB.
  - [NYU ROT](https://huggingface.co/datasets/lerobot-raw/nyu_rot_dataset_raw): 5.61 MB.
  - [TidyBot](https://huggingface.co/datasets/lerobot-raw/tidybot_raw): 20.85 MB.
  - [UTokyo PR2 opening fridge](https://huggingface.co/datasets/lerobot-raw/utokyo_pr2_opening_fridge_raw): 378.10 MB.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). New entries should include:

- Dataset name and publication year.
- Paper link.
- Project page or code repository.
- Canonical download location.
- LeRobot-format location, if one exists.
- License and access restrictions, when known.
- A short note describing what was actually verified.
- Add Hugging Face dataset repositories to [datasets.json](datasets.json), then
  run `python3 scripts/update_dataset_metadata.py --write` to refresh download
  sizes in this README.
