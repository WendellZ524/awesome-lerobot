# Data Pyramid coverage audit

Checked 2026-11-23 against [arXiv v3](https://arxiv.org/html/2607.24744v3), the [authors’ companion catalog](https://github.com/worldbench/awesome-embodied-data-pyramid), and the [pre-audit project README](https://github.com/WendellZ524/awesome-lerobot/tree/b8d047e). Each row is a dataset, benchmark, or separately named related resource. Versions and named derivatives can have separate rows. The register includes all dataset rows in Tables 1, 2, 4–8, additional named sources in the narrative and companion entries. T3 reports quality checks and T9 compares models. Companion-only items extend the paper; the register does not interpret every cited model, simulator or reference as a downloadable dataset.

383 audited entries; 21 matched the baseline README/registry and 362 had no baseline match. Format evidence: 80; Tagged release: 15; Candidate only: 10; No verified release: 278. Of the 207 distinct entries in the paper tables, 16 matched the baseline and 191 had no match.

**Reading the evidence.** Prior coverage means a name/alias or linked dataset matched the old README/registry; raw mirrors qualify for prior catalog coverage only. Each candidate was checked against public Hub discovery, with targeted inspection of dataset cards, publisher tags and root or nested schema metadata. A metadata link demonstrates a specific repository or subset; benchmark outputs and task-specific captures need not reproduce the original collection. A publisher tag lacks independent schema verification. Search is bounded (up to 100 Hub results per name and selected candidates); restricted, differently named, off-Hub and unpublished conversions can be missed. This audit does not certify payload completeness, usage rights or visual labels.

[Separate list of entries without a verified LeRobot release](DATA_PYRAMID_CONVERSION_GAPS.md). The authors explicitly report LeRobot v3 conversion for six source families (1,721 processed repositories); [their release note](https://github.com/worldbench/awesome-embodied-data-pyramid#datapyramid-collection-and-processing-code) distinguishes processed scope and upload progress.

## Real robot

| Dataset / resource | Source | In project before audit | LeRobot status | Evidence / lookup |
|---|---|---|---|---|
| ABC-130K | [T1](https://arxiv.org/html/2607.24744v3#S2.T1) · [T2](https://arxiv.org/html/2607.24744v3#S2.T2) · [source](https://arxiv.org/pdf/2606.27375) | No match | Format evidence | [Authors: converted subset; upload in progress](https://www.modelscope.cn/datasets/jasper0519/DataPyramid); [v3.0 metadata](https://huggingface.co/datasets/lerobot/abc_130k_v3_smoke/blob/main/meta/info.json) · [Hub search](https://huggingface.co/datasets?search=ABC-130K) |
| ActionNet | [T1](https://arxiv.org/html/2607.24744v3#S2.T1) · [source](https://action-net.org/) | No match | Tagged release | [Publisher tag only](https://huggingface.co/datasets/glory-hyeok/actionnet-3k-og-lerobot) · [Hub search](https://huggingface.co/datasets?search=ActionNet) |
| AgiBot World 2026 | [T1](https://arxiv.org/html/2607.24744v3#S2.T1) · [T2](https://arxiv.org/html/2607.24744v3#S2.T2) · [source](https://huggingface.co/datasets/agibot-world/AgiBotWorld2026) | No match | Format evidence | [Authors: converted subset; upload in progress](https://www.modelscope.cn/datasets/jasper0519/DataPyramid); [v3.0 metadata](https://huggingface.co/datasets/Voxel51/AgiBotWorld2026-sample-10ep/blob/main/meta/info.json) · [Hub search](https://huggingface.co/datasets?search=AgiBot%20World%202026) |
| AgiBot World Beta | [T1](https://arxiv.org/html/2607.24744v3#S2.T1) · [T2](https://arxiv.org/html/2607.24744v3#S2.T2) · [source](https://arxiv.org/abs/2503.06669) | No match | Format evidence | [Authors: converted subset; upload in progress](https://www.modelscope.cn/datasets/jasper0519/DataPyramid); [v3.0 metadata](https://huggingface.co/datasets/BAAI-DataCube/AgiBotWorld-Beta_G1_task_537_make_the_bed/blob/main/meta/info.json) · [Hub search](https://huggingface.co/datasets?search=AgiBot%20World%20Beta) |
| AIST-Bimanual | [T1](https://arxiv.org/html/2607.24744v3#S2.T1) · [source](https://aistairc.github.io/aist_bimanip_site/) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=AIST-Bimanual) |
| ALOHA Unleashed | [T1](https://arxiv.org/html/2607.24744v3#S2.T1) · [source](https://arxiv.org/abs/2410.13126) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=ALOHA%20Unleashed) |
| Baihu-VTouch | [T1](https://arxiv.org/html/2607.24744v3#S2.T1) · [source](https://arxiv.org/abs/2604.20444) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=Baihu-VTouch) |
| BC-Z | [T1](https://arxiv.org/html/2607.24744v3#S2.T1) · [source](https://arxiv.org/abs/2202.02005) | Yes | Format evidence | [v2.0 metadata](https://huggingface.co/datasets/IPEC-COMMUNITY/bc_z_lerobot/blob/main/meta/info.json) · [Hub search](https://huggingface.co/datasets?search=BC-Z) |
| BridgeData | [T1](https://arxiv.org/html/2607.24744v3#S2.T1) · [source](https://arxiv.org/abs/2109.13396) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=BridgeData) |
| BridgeData V2 | [T1](https://arxiv.org/html/2607.24744v3#S2.T1) · [source](https://arxiv.org/abs/2308.12952) | Yes | Format evidence | [v3.0 metadata](https://huggingface.co/datasets/Jackie1/bridgedata-v2-train-to-lerobot/blob/main/meta/info.json); [Release card](https://huggingface.co/datasets/nvidia/BridgeData2_LeRobot_v3) · [Hub search](https://huggingface.co/datasets?search=BridgeData%20V2) |
| DAML | [T1](https://arxiv.org/html/2607.24744v3#S2.T1) · [source](https://arxiv.org/abs/1802.01557) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=DAML) |
| DECO-50 | [T1](https://arxiv.org/html/2607.24744v3#S2.T1) · [source](https://arxiv.org/abs/2602.05513) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=DECO-50) |
| Dexora | [T1](https://arxiv.org/html/2607.24744v3#S2.T1) · [source](https://arxiv.org/abs/2605.18722) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=Dexora) |
| DROID | [T1](https://arxiv.org/html/2607.24744v3#S2.T1) · [source](https://arxiv.org/abs/2403.12945) | Yes | Format evidence | [v3.0 metadata](https://huggingface.co/datasets/lerobot/droid_1.0.1/blob/main/meta/info.json) · [Hub search](https://huggingface.co/datasets?search=DROID) |
| EgoMimic | [T1](https://arxiv.org/html/2607.24744v3#S2.T1) · [source](https://arxiv.org/abs/2410.24221) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=EgoMimic) |
| FMB dataset | [T1](https://arxiv.org/html/2607.24744v3#S2.T1) · [source](https://arxiv.org/abs/2401.08553) | Yes | Format evidence | [v3.0 metadata](https://huggingface.co/datasets/lerobot/fmb/blob/main/meta/info.json) · [Hub search](https://huggingface.co/datasets?search=FMB) |
| FurnitureBench | [T1](https://arxiv.org/html/2607.24744v3#S2.T1) · [T6](https://arxiv.org/html/2607.24744v3#S5.T6) · [source](https://arxiv.org/abs/2305.12821) | Yes | Format evidence | [v2.0 metadata](https://huggingface.co/datasets/IPEC-COMMUNITY/furniture_bench_dataset_lerobot/blob/main/meta/info.json) · [Hub search](https://huggingface.co/datasets?search=FurnitureBench) |
| Haptile | [T1](https://arxiv.org/html/2607.24744v3#S2.T1) · [source](https://arxiv.org/abs/2606.04825) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=Haptile) |
| Humanoid Everyday | [T1](https://arxiv.org/html/2607.24744v3#S2.T1) · [source](https://arxiv.org/abs/2510.08807) | No match | Format evidence | [Publisher: LeRobot release](https://github.com/physical-superintelligence-lab/Humanoid-Everyday); [2.1 metadata](https://huggingface.co/datasets/USC-PSI-Lab/humanoid-everyday/blob/main/meta/info.json) · [Hub search](https://huggingface.co/datasets?search=Humanoid%20Everyday) |
| LET-Base-Dataset | [T1](https://arxiv.org/html/2607.24744v3#S2.T1) · [source](https://www.modelscope.cn/datasets/lejurobot/LET-Base-Dataset) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=LET-Base-Dataset) |
| LET-Dex-Dataset | [T1](https://arxiv.org/html/2607.24744v3#S2.T1) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=LET-Dex-Dataset) |
| MIME | [T1](https://arxiv.org/html/2607.24744v3#S2.T1) · [source](https://arxiv.org/abs/1810.07121) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=MIME) |
| MolmoAct2-BimanualYAM | [T1](https://arxiv.org/html/2607.24744v3#S2.T1) · [source](https://arxiv.org/abs/2605.02881) | No match | Format evidence | [v3.0 metadata](https://huggingface.co/datasets/allenai/MolmoAct2-BimanualYAM-Dataset/blob/main/meta/info.json); [Release card](https://huggingface.co/datasets/allenai/MolmoAct2-BimanualYAM-Dataset) · [Hub search](https://huggingface.co/datasets?search=MolmoAct2-BimanualYAM) |
| MolmoAct2-SO100/101 | [T1](https://arxiv.org/html/2607.24744v3#S2.T1) · [source](https://arxiv.org/abs/2605.02881) | No match | Format evidence | [Publisher: component data links](https://huggingface.co/datasets/allenai/MolmoAct2-SO100_101-Dataset); [Release card](https://huggingface.co/datasets/allenai/MolmoAct2-SO100_101-Dataset) · [Hub search](https://huggingface.co/datasets?search=MolmoAct2-SO100/101) |
| MotionTrans | [T1](https://arxiv.org/html/2607.24744v3#S2.T1) · [source](https://arxiv.org/abs/2509.17759) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=MotionTrans) |
| MT-Opt | [T1](https://arxiv.org/html/2607.24744v3#S2.T1) · [source](https://arxiv.org/abs/2104.08212) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=MT-Opt) |
| OmniViTac | [T1](https://arxiv.org/html/2607.24744v3#S2.T1) · [source](https://arxiv.org/abs/2603.19201) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=OmniViTac) |
| Open Galaxea | [T1](https://arxiv.org/html/2607.24744v3#S2.T1) · [source](https://arxiv.org/abs/2509.00576) | No match | Format evidence | [Publisher: Galaxea Open-World LeRobot release](https://github.com/OpenGalaxea/GalaxeaVLA) · [Hub search](https://huggingface.co/datasets?search=Open%20Galaxea) |
| Open X-Embodiment | [T1](https://arxiv.org/html/2607.24744v3#S2.T1) · [source](https://arxiv.org/abs/2310.08864) | Yes | Tagged release | [Publisher tag only](https://huggingface.co/datasets/ehalicki/open-x-embodiment-320x240) · [Hub search](https://huggingface.co/datasets?search=Open%20X-Embodiment) |
| Open-H-Embodiment | [T1](https://arxiv.org/html/2607.24744v3#S2.T1) · [source](https://arxiv.org/abs/2604.21017) | No match | Format evidence | [Publisher: LeRobot v3.0](https://github.com/open-h/open-h-embodiment) · [Hub search](https://huggingface.co/datasets?search=Open-H-Embodiment) |
| PH2D | [T1](https://arxiv.org/html/2607.24744v3#S2.T1) · [source](https://arxiv.org/abs/2503.13441) | No match | Format evidence | [v2.1 metadata](https://huggingface.co/datasets/duzetao/ph2d_20dim_v2116/blob/main/meta/info.json); [Release card](https://huggingface.co/datasets/duzetao/ph2d_20dim_v2116) · [Hub search](https://huggingface.co/datasets?search=PH2D) |
| Pinto and Gupta | [T1](https://arxiv.org/html/2607.24744v3#S2.T1) · [source](https://arxiv.org/abs/1509.06825) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=Pinto%20and%20Gupta) |
| QT-Opt | [T1](https://arxiv.org/html/2607.24744v3#S2.T1) · [source](https://arxiv.org/abs/1806.10293) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=QT-Opt) |
| RealSource World | [T1](https://arxiv.org/html/2607.24744v3#S2.T1) · [source](https://realmanrobot.github.io/real_source_dataset) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=RealSource%20World) |
| REASSEMBLE | [T1](https://arxiv.org/html/2607.24744v3#S2.T1) · [source](https://arxiv.org/abs/2502.05086) | No match | Format evidence | [v3.0 metadata](https://huggingface.co/datasets/robot-lev/reassemble/blob/main/meta/info.json) · [Hub search](https://huggingface.co/datasets?search=REASSEMBLE) |
| RH20T | [T1](https://arxiv.org/html/2607.24744v3#S2.T1) · [source](https://arxiv.org/abs/2307.00595) | No match | Format evidence | [v2.1 metadata](https://huggingface.co/datasets/hainh22/rh20t_task_003/blob/main/meta/info.json) · [Hub search](https://huggingface.co/datasets?search=RH20T) |
| RoboCOIN | [T1](https://arxiv.org/html/2607.24744v3#S2.T1) · [source](https://arxiv.org/abs/2511.17441) | No match | Tagged release | [Publisher tag only](https://huggingface.co/datasets/RoboCOIN/Agilex_Cobot_Magic_plate_storage) · [Hub search](https://huggingface.co/datasets?search=RoboCOIN) |
| RoboMIND | [T1](https://arxiv.org/html/2607.24744v3#S2.T1) · [T2](https://arxiv.org/html/2607.24744v3#S2.T2) · [source](https://arxiv.org/abs/2412.13877) | No match | Format evidence | [Authors: converted subset; upload in progress](https://www.modelscope.cn/datasets/jasper0519/DataPyramid) · [Hub search](https://huggingface.co/datasets?search=RoboMIND) |
| RoboMIND 2.0 | [T1](https://arxiv.org/html/2607.24744v3#S2.T1) · [source](https://arxiv.org/abs/2512.24653) | No match | Format evidence | [v2.1 metadata](https://huggingface.co/datasets/ml-resources/RoboMIND2.0/blob/main/camera_extrinsics_intrinsics/franka/robogene_Twoarm_franka_press_seal_on_A4_plate_clamp/meta/info.json) · [Hub search](https://huggingface.co/datasets?search=RoboMIND%202.0) |
| RoboNet | [T1](https://arxiv.org/html/2607.24744v3#S2.T1) · [T8](https://arxiv.org/html/2607.24744v3#S6.T8) · [source](https://arxiv.org/abs/1910.11215) | Yes | No verified release | [Hub search](https://huggingface.co/datasets?search=RoboNet) |
| RoboSet | [T1](https://arxiv.org/html/2607.24744v3#S2.T1) · [source](https://arxiv.org/abs/2309.01918) | Yes | Format evidence | [v2.1 metadata](https://huggingface.co/datasets/bxyjsnd/robo_set_new_lerobot/blob/main/meta/info.json); [Release card](https://huggingface.co/datasets/bxyjsnd/robo_set_lerobot) · [Hub search](https://huggingface.co/datasets?search=RoboSet) |
| RoboTurk | [T1](https://arxiv.org/html/2607.24744v3#S2.T1) · [source](https://arxiv.org/abs/1811.02790) | Yes | Format evidence | [v3.0 metadata](https://huggingface.co/datasets/lerobot/roboturk/blob/main/meta/info.json) · [Hub search](https://huggingface.co/datasets?search=RoboTurk) |
| RT-1 | [T1](https://arxiv.org/html/2607.24744v3#S2.T1) · [source](https://arxiv.org/abs/2212.06817) | Yes | Format evidence | [v2.0 metadata](https://huggingface.co/datasets/IPEC-COMMUNITY/fractal20220817_data_lerobot/blob/main/meta/info.json) · [Hub search](https://huggingface.co/datasets?search=RT-1) |
| Unitree UnifoLM-WBT | [T1](https://arxiv.org/html/2607.24744v3#S2.T1) · [source](https://huggingface.co/collections/unitreerobotics/unifolm-wbt-dataset) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=Unitree%20UnifoLM-WBT) |

## Converted sources

| Dataset / resource | Source | In project before audit | LeRobot status | Evidence / lookup |
|---|---|---|---|---|
| Galaxea Lite / Pro | [T2](https://arxiv.org/html/2607.24744v3#S2.T2) | No match | Format evidence | [Authors: converted subset; upload in progress](https://www.modelscope.cn/datasets/jasper0519/DataPyramid) · [Hub search](https://huggingface.co/datasets?search=Galaxea%20Lite) |

## Simulation data

| Dataset / resource | Source | In project before audit | LeRobot status | Evidence / lookup |
|---|---|---|---|---|
| Dex1B | [T7](https://arxiv.org/html/2607.24744v3#S5.T7) · [source](https://arxiv.org/abs/2506.17198) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=Dex1B) |
| DexGraspNet | [T7](https://arxiv.org/html/2607.24744v3#S5.T7) · [source](https://arxiv.org/abs/2210.02697) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=DexGraspNet) |
| DexGraspNet 2.0 | [T7](https://arxiv.org/html/2607.24744v3#S5.T7) · [T8](https://arxiv.org/html/2607.24744v3#S6.T8) · [source](https://arxiv.org/abs/2410.23004) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=DexGraspNet%202.0) |
| DexMimicGen | [T7](https://arxiv.org/html/2607.24744v3#S5.T7) · [source](https://arxiv.org/abs/2410.24185) | No match | Format evidence | [v2.1 metadata](https://huggingface.co/datasets/slowturtle99/dexmimicgen_lerobot_dataset/blob/main/dexmimicgen.two_arm_box_cleanup/meta/info.json) · [Hub search](https://huggingface.co/datasets?search=DexMimicGen) |
| InternData-A1 | [T2](https://arxiv.org/html/2607.24744v3#S2.T2) · [T7](https://arxiv.org/html/2607.24744v3#S5.T7) · [source](https://arxiv.org/abs/2511.16651) | No match | Format evidence | [Authors: converted subset; upload in progress](https://www.modelscope.cn/datasets/jasper0519/DataPyramid); [v3.0 metadata](https://huggingface.co/datasets/Voxel51/interndata-a1-close-the-laptop-369ep/blob/main/meta/info.json) · [Hub search](https://huggingface.co/datasets?search=InternData-A1) |
| InternData-M1 | [T7](https://arxiv.org/html/2607.24744v3#S5.T7) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=InternData-M1) |
| MimicGen | [T7](https://arxiv.org/html/2607.24744v3#S5.T7) · [source](https://arxiv.org/abs/2310.17596) | No match | Format evidence | [v2.1 metadata](https://huggingface.co/datasets/locht131/mimicgen_1000_lerobot/blob/main/meta/info.json) · [Hub search](https://huggingface.co/datasets?search=MimicGen) |
| MolmoB0T | [T7](https://arxiv.org/html/2607.24744v3#S5.T7) · [source](https://arxiv.org/abs/2603.16861) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=MolmoB0T) |
| NVIDIA GR00T-X Sim | [T7](https://arxiv.org/html/2607.24744v3#S5.T7) · [source](https://arxiv.org/abs/2503.14734) | No match | Format evidence | [v3.0 metadata](https://huggingface.co/datasets/cfahlgren1/gr00t-x-embodiment-sim-gr1-pouring-v3/blob/main/meta/info.json); [Community subset with format declaration](https://huggingface.co/datasets/cfahlgren1/gr00t-x-embodiment-sim-gr1-pouring-v3) · [Hub search](https://huggingface.co/datasets?search=GR00T-X-Embodiment-Sim) |
| SynGrasp-1B | [T7](https://arxiv.org/html/2607.24744v3#S5.T7) · [source](https://arxiv.org/abs/2505.03233) | No match | Format evidence | [v3.0 metadata](https://huggingface.co/datasets/vegebirrd/SynGrasp-1B/blob/main/front-side-290cat-500w_lerobot/000b701e-1381-43e6-a966-d03342f30f0e/meta/info.json) · [Hub search](https://huggingface.co/datasets?search=SynGrasp-1B) |

## UMI

| Dataset / resource | Source | In project before audit | LeRobot status | Evidence / lookup |
|---|---|---|---|---|
| Daimon-Infinity | [T4](https://arxiv.org/html/2607.24744v3#S3.T4) · [source](https://arxiv.org/abs/2610.20320) | No match | Format evidence | [v3.0 metadata](https://huggingface.co/datasets/ml-resources/Daimon-Infinity/blob/main/DM-DataClaw/datasets/v1_3_usb_backups_2026-03-04/dag911262r000153_lerobot_0326_143530/meta/info.json); [v3.0 metadata](https://huggingface.co/datasets/daimonrobotics/Daimon-Infinity/blob/main/DM-DataClaw/datasets/v1_3_usb_backups_2026-03-04/dag911262r000153_lerobot_0326_143530/meta/info.json) · [Hub search](https://huggingface.co/datasets?search=Daimon-Infinity) |
| Data Scaling Laws | [T4](https://arxiv.org/html/2607.24744v3#S3.T4) · [source](https://arxiv.org/abs/2410.18647) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=Data%20Scaling%20Laws) |
| DexUMI | [T4](https://arxiv.org/html/2607.24744v3#S3.T4) · [source](https://arxiv.org/abs/2505.21864) | No match | Format evidence | [v3.0 metadata](https://huggingface.co/datasets/NONHUMAN-RESEARCH/dexumi-dataset/blob/main/meta/info.json) · [Hub search](https://huggingface.co/datasets?search=DexUMI) |
| DexWild | [T4](https://arxiv.org/html/2607.24744v3#S3.T4) · [source](https://arxiv.org/abs/2505.07813) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=DexWild) |
| exUMI | [T4](https://arxiv.org/html/2607.24744v3#S3.T4) · [source](https://arxiv.org/abs/2509.14688) | No match | Tagged release | [Publisher tag only](https://huggingface.co/datasets/easyminnn/exumi-lerobot) · [Hub search](https://huggingface.co/datasets?search=exUMI) |
| FastUMI | [T4](https://arxiv.org/html/2607.24744v3#S3.T4) · [source](https://proceedings.mlr.press/v305/zhaxizhuoma25a.html) | No match | Format evidence | [v3.0 metadata](https://huggingface.co/datasets/XixinZhang/fastumi-egg-demos/blob/main/meta/info.json) · [Hub search](https://huggingface.co/datasets?search=FastUMI) |
| FastUMI-100K | [T4](https://arxiv.org/html/2607.24744v3#S3.T4) · [source](https://arxiv.org/abs/2510.08022) | Yes | Format evidence | [v2.1 metadata](https://huggingface.co/datasets/IPEC-COMMUNITY/FastUMI_100k_lerobot/blob/main/dual_arm/Add_Rice_to_Rice_Cooker/meta/info.json); [Release card](https://huggingface.co/datasets/IPEC-COMMUNITY/FastUMI_100k_lerobot) · [Hub search](https://huggingface.co/datasets?search=FastUMI-100K) |
| FreeTacMan | [T4](https://arxiv.org/html/2607.24744v3#S3.T4) · [source](https://arxiv.org/abs/2506.01941) | No match | Tagged release | [Publisher tag only](https://huggingface.co/datasets/easyminnn/freetacman-lerobot) · [Hub search](https://huggingface.co/datasets?search=FreeTacMan) |
| HuMI | [T4](https://arxiv.org/html/2607.24744v3#S3.T4) · [source](https://arxiv.org/abs/2602.06643) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=HuMI) |
| LEGATO | [T4](https://arxiv.org/html/2607.24744v3#S3.T4) · [source](https://arxiv.org/abs/2411.03682) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=LEGATO) |
| ManipForce | [T4](https://arxiv.org/html/2607.24744v3#S3.T4) · [source](https://arxiv.org/abs/2509.19047) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=ManipForce) |
| ManiWAV | [T4](https://arxiv.org/html/2607.24744v3#S3.T4) · [source](https://arxiv.org/abs/2406.19464) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=ManiWAV) |
| MV-UMI | [T4](https://arxiv.org/html/2607.24744v3#S3.T4) · [source](https://arxiv.org/abs/2509.18757) | No match | Format evidence | [v3.0 metadata](https://huggingface.co/datasets/DaivdYuan/mv-umi-markers-placement-raw-lerobot/blob/main/meta/info.json) · [Hub search](https://huggingface.co/datasets?search=MV-UMI) |
| RealOmni | [T4](https://arxiv.org/html/2607.24744v3#S3.T4) · [source](https://www.genrobot.ai/data/open-dataset/) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=RealOmni) |
| TAMEn | [T4](https://arxiv.org/html/2607.24744v3#S3.T4) · [source](https://arxiv.org/abs/2604.07335) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=TAMEn) |
| Touch in the Wild | [T4](https://arxiv.org/html/2607.24744v3#S3.T4) · [source](https://arxiv.org/abs/2507.15062) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=Touch%20in%20the%20Wild) |
| UMI | [T4](https://arxiv.org/html/2607.24744v3#S3.T4) · [source](https://arxiv.org/abs/2402.10329) | Yes | Format evidence | [v3.0 metadata](https://huggingface.co/datasets/lerobot/umi_cup_in_the_wild/blob/main/meta/info.json) · [Hub search](https://huggingface.co/datasets?search=UMI) |
| UMI on Legs | [T4](https://arxiv.org/html/2607.24744v3#S3.T4) · [source](https://openreview.net/forum?id=3i7j8ZPnbm) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=UMI%20on%20Legs) |
| UMI-3D | [T4](https://arxiv.org/html/2607.24744v3#S3.T4) · [source](https://arxiv.org/abs/2604.14089) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=UMI-3D) |
| ViTaMIn | [T4](https://arxiv.org/html/2607.24744v3#S3.T4) · [source](https://arxiv.org/abs/2504.06156) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=ViTaMIn) |
| ViTaMIn-B | [T4](https://arxiv.org/html/2607.24744v3#S3.T4) · [source](https://arxiv.org/abs/2511.05858) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=ViTaMIn-B) |

## Egocentric / exocentric

| Dataset / resource | Source | In project before audit | LeRobot status | Evidence / lookup |
|---|---|---|---|---|
| ARCTIC | [T5](https://arxiv.org/html/2607.24744v3#S4.T5) · [source](https://arxiv.org/abs/2204.13662) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=ARCTIC) |
| Assembly101 | [T5](https://arxiv.org/html/2607.24744v3#S4.T5) · [source](https://arxiv.org/abs/2203.14712) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=Assembly101) |
| AssemblyHands | [T5](https://arxiv.org/html/2607.24744v3#S4.T5) · [source](https://arxiv.org/abs/2304.12301) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=AssemblyHands) |
| CaptainCook4D | [T5](https://arxiv.org/html/2607.24744v3#S4.T5) · [source](https://arxiv.org/abs/2312.14556) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=CaptainCook4D) |
| Charades-Ego | [T5](https://arxiv.org/html/2607.24744v3#S4.T5) · [source](https://arxiv.org/abs/1804.09626) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=Charades-Ego) |
| ChildLens | [T5](https://arxiv.org/html/2607.24744v3#S4.T5) · [source](https://link.springer.com/article/10.3758/s13428-026-02982-6) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=ChildLens) |
| Ego-1K | [T5](https://arxiv.org/html/2607.24744v3#S4.T5) · [source](https://arxiv.org/abs/2603.13741) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=Ego-1K) |
| Ego-Exo4D | [T5](https://arxiv.org/html/2607.24744v3#S4.T5) · [source](https://arxiv.org/abs/2311.18259) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=Ego-Exo4D) |
| Ego4D | [T5](https://arxiv.org/html/2607.24744v3#S4.T5) · [source](https://arxiv.org/abs/2110.07058) | No match | Format evidence | [Derived labels; original media required](https://huggingface.co/datasets/EgoSteer/EgoSteer-Egocentric) · [Hub search](https://huggingface.co/datasets?search=Ego4D) |
| Egocentric-100K | [T5](https://arxiv.org/html/2607.24744v3#S4.T5) · [source](https://huggingface.co/datasets/builddotai/Egocentric-100K) | No match | Format evidence | [3.1.0 metadata](https://huggingface.co/datasets/ShubhamRasal/egocentric-100k-pi0-sample/blob/main/meta/info.json) · [Hub search](https://huggingface.co/datasets?search=Egocentric-100K) |
| EgoDex | [T5](https://arxiv.org/html/2607.24744v3#S4.T5) · [source](https://arxiv.org/abs/2505.11709) | Yes | Format evidence | [v3.0 metadata](https://huggingface.co/datasets/griffinlabs/EgoDex-LeRobot-v3.0/blob/main/test/add_remove_lid/meta/info.json); [v3.0 metadata](https://huggingface.co/datasets/yixuan-tan/EgoDex-LeRobot-v3.0/blob/main/test/add_remove_lid/meta/info.json) · [Hub search](https://huggingface.co/datasets?search=EgoDex) |
| EgoExo-Fitness | [T5](https://arxiv.org/html/2607.24744v3#S4.T5) · [source](https://arxiv.org/abs/2406.08877) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=EgoExo-Fitness) |
| EgoExoLearn | [T5](https://arxiv.org/html/2607.24744v3#S4.T5) · [source](https://arxiv.org/abs/2403.16182) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=EgoExoLearn) |
| EgoHands | [T5](https://arxiv.org/html/2607.24744v3#S4.T5) · [source](https://openaccess.thecvf.com/content_iccv_2015/html/Bambach_Lending_A_Hand_ICCV_2015_paper.html) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=EgoHands) |
| EgoLife | [T5](https://arxiv.org/html/2607.24744v3#S4.T5) · [source](https://arxiv.org/abs/2503.03803) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=EgoLife) |
| EgoLive | [T5](https://arxiv.org/html/2607.24744v3#S4.T5) · [source](https://arxiv.org/abs/2604.23570) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=EgoLive) |
| EgoMAGIC | [T5](https://arxiv.org/html/2607.24744v3#S4.T5) · [source](https://arxiv.org/abs/2604.22036) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=EgoMAGIC) |
| EgoMe | [T5](https://arxiv.org/html/2607.24744v3#S4.T5) · [source](https://arxiv.org/abs/2501.19061) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=EgoMe) |
| EgoSurgery | [T5](https://arxiv.org/html/2607.24744v3#S4.T5) · [source](https://arxiv.org/abs/2405.19644) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=EgoSurgery) |
| EgoVerse | [T5](https://arxiv.org/html/2607.24744v3#S4.T5) · [source](https://arxiv.org/abs/2604.07607) | Yes | Format evidence | [v2.1 metadata](https://huggingface.co/datasets/Noctis12138/egoverse-aria-selected/blob/main/meta/info.json) · [Hub search](https://huggingface.co/datasets?search=EgoVerse) |
| EGTEA Gaze+ | [T5](https://arxiv.org/html/2607.24744v3#S4.T5) · [source](https://doi.org/10.1109/TPAMI.2021.3051319) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=EGTEA%20Gaze%2B) |
| ENIGMA-51 | [T5](https://arxiv.org/html/2607.24744v3#S4.T5) · [source](https://arxiv.org/abs/2309.14809) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=ENIGMA-51) |
| EPIC-KITCHENS v1 | [T5](https://arxiv.org/html/2607.24744v3#S4.T5) · [source](https://arxiv.org/abs/1804.02748) | No match | Candidate only | [candidate](https://huggingface.co/datasets/n3puiol/epic_kitchens_100_lerobot) · [Hub search](https://huggingface.co/datasets?search=EPIC-KITCHENS) |
| EPIC-KITCHENS-100 | [T5](https://arxiv.org/html/2607.24744v3#S4.T5) · [source](https://doi.org/10.1007/s11263-021-01531-2) | No match | Format evidence | [v3.0 metadata](https://huggingface.co/datasets/n3puiol/epic_kitchens_100_lerobot/blob/main/meta/info.json) · [Hub search](https://huggingface.co/datasets?search=EPIC-KITCHENS-100) |
| FPHA | [T5](https://arxiv.org/html/2607.24744v3#S4.T5) · [source](https://arxiv.org/abs/1704.02463) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=FPHA) |
| H2O | [T5](https://arxiv.org/html/2607.24744v3#S4.T5) · [source](https://arxiv.org/abs/2104.11181) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=H2O) |
| HD-EPIC | [T5](https://arxiv.org/html/2607.24744v3#S4.T5) · [source](https://arxiv.org/abs/2502.04144) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=HD-EPIC) |
| HOI4D | [T5](https://arxiv.org/html/2607.24744v3#S4.T5) · [source](https://arxiv.org/abs/2203.01577) | No match | Format evidence | [v3.0 metadata](https://huggingface.co/datasets/JingkunAn/lerobot_hoi4d_dataset/blob/main/meta/info.json) · [Hub search](https://huggingface.co/datasets?search=HOI4D) |
| HoloAssist | [T5](https://arxiv.org/html/2607.24744v3#S4.T5) · [source](https://arxiv.org/abs/2309.17024) | No match | Format evidence | [Derived labels; original media required](https://huggingface.co/datasets/EgoSteer/EgoSteer-Egocentric) · [Hub search](https://huggingface.co/datasets?search=HoloAssist) |
| HOT3D | [T5](https://arxiv.org/html/2607.24744v3#S4.T5) · [source](https://arxiv.org/abs/2411.19167) | Yes | No verified release | [Hub search](https://huggingface.co/datasets?search=HOT3D) |
| HumanNet | [T5](https://arxiv.org/html/2607.24744v3#S4.T5) | No match | Format evidence | [Derived subset in Open-HumanWAM-50K; access controlled](https://github.com/DAGroup-PKU/HumanNet) · [Hub search](https://huggingface.co/datasets?search=HumanNet) |
| IndEgo | [T5](https://arxiv.org/html/2607.24744v3#S4.T5) · [source](https://arxiv.org/abs/2511.19684) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=IndEgo) |
| IndustReal | [T5](https://arxiv.org/html/2607.24744v3#S4.T5) · [source](https://arxiv.org/abs/2310.17323) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=IndustReal) |
| KrishnaCam | [T5](https://arxiv.org/html/2607.24744v3#S4.T5) · [source](https://krsingh.cs.ucdavis.edu/krishna_files/papers/krishnacam/krishnacam_files/kcam_wacv16.pdf) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=KrishnaCam) |
| Open-AoE | [T5](https://arxiv.org/html/2607.24744v3#S4.T5) · [source](https://arxiv.org/abs/2607.14183) | No match | No verified release | [Export / pipeline documented; public output unverified](https://github.com/ant-research/Open-AoE) · [Hub search](https://huggingface.co/datasets?search=Open-AoE) |
| OpenEgo | [T5](https://arxiv.org/html/2607.24744v3#S4.T5) · [source](https://arxiv.org/abs/2509.05513) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=OpenEgo) |
| TASTE-Rob | [T5](https://arxiv.org/html/2607.24744v3#S4.T5) · [source](https://arxiv.org/abs/2503.11423) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=TASTE-Rob) |
| Xperience-10M | [T5](https://arxiv.org/html/2607.24744v3#S4.T5) · [source](https://huggingface.co/datasets/ropedia-ai/xperience-10m) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=Xperience-10M) |

## Simulation benchmarks

| Dataset / resource | Source | In project before audit | LeRobot status | Evidence / lookup |
|---|---|---|---|---|
| Adroit | [T6](https://arxiv.org/html/2607.24744v3#S5.T6) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=Adroit) |
| ARNOLD | [T6](https://arxiv.org/html/2607.24744v3#S5.T6) · [source](https://arxiv.org/abs/2304.04321) | No match | Candidate only | [candidate](https://huggingface.co/datasets/ishika/lerobot_arnold_data_test) · [Hub search](https://huggingface.co/datasets?search=ARNOLD) |
| BEHAVIOR-1K | [T6](https://arxiv.org/html/2607.24744v3#S5.T6) · [source](https://arxiv.org/abs/2403.09227) | No match | Format evidence | [v3.0 metadata](https://huggingface.co/datasets/lerobot/behavior1k-task0010/blob/main/meta/info.json) · [Hub search](https://huggingface.co/datasets?search=BEHAVIOR-1K) |
| Bi-DexHands | [T6](https://arxiv.org/html/2607.24744v3#S5.T6) · [source](https://arxiv.org/abs/2206.08686) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=Bi-DexHands) |
| BiCoord | [T6](https://arxiv.org/html/2607.24744v3#S5.T6) · [source](https://arxiv.org/abs/2604.05831) | No match | Format evidence | [v3.0 metadata](https://huggingface.co/datasets/BanUrsus/bicoord_build_bridge_clean_franka_55eps_multiaction/blob/main/meta/info.json) · [Hub search](https://huggingface.co/datasets?search=BiCoord) |
| BiGym | [T6](https://arxiv.org/html/2607.24744v3#S5.T6) · [source](https://arxiv.org/abs/2407.07788) | No match | Tagged release | [Publisher tag only](https://huggingface.co/datasets/eustance/bigym-all-tasks-3dgs-one-success) · [Hub search](https://huggingface.co/datasets?search=BiGym) |
| CALVIN | [T6](https://arxiv.org/html/2607.24744v3#S5.T6) · [source](https://arxiv.org/abs/2112.03227) | No match | Format evidence | [v2.0 metadata](https://huggingface.co/datasets/ducido/calvin_task_D_D_scale_30_lerobo_format/blob/main/meta/info.json) · [Hub search](https://huggingface.co/datasets?search=CALVIN) |
| DaXBench | [T6](https://arxiv.org/html/2607.24744v3#S5.T6) · [source](https://arxiv.org/abs/2210.13066) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=DaXBench) |
| DexArt | [T6](https://arxiv.org/html/2607.24744v3#S5.T6) · [source](https://arxiv.org/abs/2305.05706) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=DexArt) |
| DuoBench | [T6](https://arxiv.org/html/2607.24744v3#S5.T6) · [source](https://arxiv.org/abs/2606.11901) | No match | Tagged release | [Publisher tag only](https://huggingface.co/datasets/RobotControlStack/duobench) · [Hub search](https://huggingface.co/datasets?search=DuoBench) |
| Franka Kitchen | [T6](https://arxiv.org/html/2607.24744v3#S5.T6) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=Franka%20Kitchen) |
| GarmentLab | [T6](https://arxiv.org/html/2607.24744v3#S5.T6) · [source](https://arxiv.org/abs/2411.01200) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=GarmentLab) |
| GenManip | [T6](https://arxiv.org/html/2607.24744v3#S5.T6) | No match | Tagged release | [Publisher tag only](https://huggingface.co/datasets/Abrms/genmanip-ebench-lerobot-v2.1) · [Hub search](https://huggingface.co/datasets?search=GenManip) |
| HumanoidBench | [T6](https://arxiv.org/html/2607.24744v3#S5.T6) · [source](https://arxiv.org/abs/2403.10506) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=HumanoidBench) |
| LIBERO | [T6](https://arxiv.org/html/2607.24744v3#S5.T6) · [source](https://arxiv.org/abs/2306.03310) | Yes | Format evidence | [v3.0 metadata](https://huggingface.co/datasets/lerobot/libero_10_image/blob/main/meta/info.json) · [Hub search](https://huggingface.co/datasets?search=LIBERO) |
| ManiSkill-HAB | [T6](https://arxiv.org/html/2607.24744v3#S5.T6) · [source](https://arxiv.org/abs/2412.13211) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=ManiSkill-HAB) |
| ManiSkill-ViTac | [T6](https://arxiv.org/html/2607.24744v3#S5.T6) · [source](https://arxiv.org/abs/2411.12503) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=ManiSkill-ViTac) |
| ManiSkill2 | [T6](https://arxiv.org/html/2607.24744v3#S5.T6) · [source](https://arxiv.org/abs/2302.04659) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=ManiSkill2) |
| ManiSkill3 | [T6](https://arxiv.org/html/2607.24744v3#S5.T6) | No match | Format evidence | [v2.1 metadata](https://huggingface.co/datasets/onnoboru/maniskill3-sft-rgb-lerobot-1200ep/blob/main/meta/info.json) · [Hub search](https://huggingface.co/datasets?search=ManiSkill3) |
| MemoryBench | [T6](https://arxiv.org/html/2607.24744v3#S5.T6) | No match | Format evidence | [v2.0 metadata](https://huggingface.co/datasets/memory-vla/memorybench-lerobot/blob/main/test/meta/info.json) · [Hub search](https://huggingface.co/datasets?search=MemoryBench) |
| Meta-World | [T6](https://arxiv.org/html/2607.24744v3#S5.T6) · [source](https://arxiv.org/abs/1910.10897) | No match | Format evidence | [v3.0 metadata](https://huggingface.co/datasets/lerobot/metaworld_mt50/blob/main/meta/info.json) · [Hub search](https://huggingface.co/datasets?search=Meta-World) |
| MIKASA-Robo-VLA | [T6](https://arxiv.org/html/2607.24744v3#S5.T6) | No match | Format evidence | [v3.0 metadata](https://huggingface.co/datasets/mikasa-robo/mikasa-robo-vla-lerobot/blob/main/batteries_checker_easy_3_vla_v0/meta/info.json) · [Hub search](https://huggingface.co/datasets?search=MIKASA-Robo-VLA) |
| PlasticineLab | [T6](https://arxiv.org/html/2607.24744v3#S5.T6) · [source](https://arxiv.org/abs/2104.03311) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=PlasticineLab) |
| REALM | [T6](https://arxiv.org/html/2607.24744v3#S5.T6) · [source](https://arxiv.org/abs/2512.19562) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=REALM) |
| RLBench | [T6](https://arxiv.org/html/2607.24744v3#S5.T6) · [source](https://arxiv.org/abs/1909.12271) | No match | Format evidence | [v2.0 metadata](https://huggingface.co/datasets/daixianjie/rlbench_lerobot_test/blob/main/meta/info.json) · [Hub search](https://huggingface.co/datasets?search=RLBench) |
| RMBench | [T6](https://arxiv.org/html/2607.24744v3#S5.T6) · [source](https://arxiv.org/abs/2603.01229) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=RMBench) |
| RoboCasa | [T6](https://arxiv.org/html/2607.24744v3#S5.T6) · [source](https://arxiv.org/abs/2406.02523) | No match | Format evidence | [v2.1 metadata](https://huggingface.co/datasets/ishika/robocasa_gr1_tabletop_tasks_fingertips/blob/main/meta/info.json) · [Hub search](https://huggingface.co/datasets?search=RoboCasa) |
| RoboCasa365 | [T6](https://arxiv.org/html/2607.24744v3#S5.T6) · [source](https://arxiv.org/abs/2603.04356) | No match | Tagged release | [Publisher tag only](https://huggingface.co/datasets/OpenMOSS-Team/robocasa365-lerobot-v3.0) · [Hub search](https://huggingface.co/datasets?search=RoboCasa365) |
| RoboCerebra | [T6](https://arxiv.org/html/2607.24744v3#S5.T6) · [source](https://arxiv.org/abs/2506.06677) | No match | Format evidence | [v3.0 metadata](https://huggingface.co/datasets/lerobot/robocerebra_unified/blob/main/meta/info.json) · [Hub search](https://huggingface.co/datasets?search=RoboCerebra) |
| RoboDojo | [T6](https://arxiv.org/html/2607.24744v3#S5.T6) · [source](https://arxiv.org/abs/2607.04434) | No match | Format evidence | [v3.0 metadata](https://huggingface.co/datasets/seungkukim/robodojo-pexpert-4task-lerobot-v3.0/blob/main/meta/info.json) · [Hub search](https://huggingface.co/datasets?search=RoboDojo) |
| RoboEval | [T6](https://arxiv.org/html/2607.24744v3#S5.T6) · [source](https://arxiv.org/abs/2507.00435) | No match | Format evidence | [v2.1 metadata](https://huggingface.co/datasets/NatashaYang/roboeval_lerobot_dataset/blob/main/meta/info.json) · [Hub search](https://huggingface.co/datasets?search=RoboEval) |
| RoboHive | [T6](https://arxiv.org/html/2607.24744v3#S5.T6) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=RoboHive) |
| RoboMemArena | [T6](https://arxiv.org/html/2607.24744v3#S5.T6) · [source](https://arxiv.org/abs/2605.10921) | No match | Format evidence | [v3.0 metadata](https://huggingface.co/datasets/yinchenghust/robomemarena_lerobot/blob/main/meta/info.json) · [Hub search](https://huggingface.co/datasets?search=RoboMemArena) |
| RoboMimic | [T6](https://arxiv.org/html/2607.24744v3#S5.T6) · [source](https://arxiv.org/abs/2108.03298) | No match | Format evidence | [v3.0 metadata](https://huggingface.co/datasets/ViaCatalyst/robomimic-lift-ph-lerobot-v3/blob/main/meta/info.json) · [Hub search](https://huggingface.co/datasets?search=RoboMimic) |
| RoboMME | [T6](https://arxiv.org/html/2607.24744v3#S5.T6) · [source](https://arxiv.org/abs/2603.04639) | No match | Format evidence | [v3.0 metadata](https://huggingface.co/datasets/lerobot/robomme/blob/main/meta/info.json) · [Hub search](https://huggingface.co/datasets?search=RoboMME) |
| RobotArena∞ | [T6](https://arxiv.org/html/2607.24744v3#S5.T6) · [source](https://arxiv.org/abs/2510.23571) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=RobotArena%E2%88%9E) |
| RoboTwin | [T6](https://arxiv.org/html/2607.24744v3#S5.T6) · [source](https://arxiv.org/abs/2409.02920) | No match | Format evidence | [v3.0 metadata](https://huggingface.co/datasets/suz22/RoboTwin_clean/blob/main/meta/info.json) · [Hub search](https://huggingface.co/datasets?search=RoboTwin) |
| RoboTwin 2.0 | [T6](https://arxiv.org/html/2607.24744v3#S5.T6) · [source](https://arxiv.org/abs/2506.18088) | No match | Tagged release | [Publisher tag only](https://huggingface.co/datasets/OpenMOSS-Team/robotwin2.0-lerobot-v3.0) · [Hub search](https://huggingface.co/datasets?search=RoboTwin%202.0) |
| SIMPLER-Env | [T6](https://arxiv.org/html/2607.24744v3#S5.T6) · [source](https://arxiv.org/abs/2405.05941) | No match | Format evidence | [v3.0 metadata](https://huggingface.co/datasets/lukasskellijs/simpler_xvla_widowx/blob/main/meta/info.json) · [Hub search](https://huggingface.co/datasets?search=SIMPLER) |
| TacSL | [T6](https://arxiv.org/html/2607.24744v3#S5.T6) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=TacSL) |
| Tactile Gym 2.0 | [T6](https://arxiv.org/html/2607.24744v3#S5.T6) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=Tactile%20Gym%202.0) |
| The Colosseum | [T6](https://arxiv.org/html/2607.24744v3#S5.T6) · [source](https://arxiv.org/abs/2402.08191) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=The%20Colosseum) |
| UniVTAC | [T6](https://arxiv.org/html/2607.24744v3#S5.T6) | No match | Format evidence | [v3.0 metadata](https://huggingface.co/datasets/RoboSynapse/univtac-isaac51_franka-panda_insert-HDMI-v4/blob/main/meta/info.json) · [Hub search](https://huggingface.co/datasets?search=UniVTAC) |
| VIMA-Bench | [T6](https://arxiv.org/html/2607.24744v3#S5.T6) · [source](https://arxiv.org/abs/2210.03094) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=VIMA) |
| VLABench | [T6](https://arxiv.org/html/2607.24744v3#S5.T6) · [source](https://arxiv.org/abs/2412.18194) | No match | Format evidence | [v3.0 metadata](https://huggingface.co/datasets/THULab/vlabench_primitive_ft_lerobot_video/blob/main/meta/info.json) · [Hub search](https://huggingface.co/datasets?search=VLABench) |

## General data

| Dataset / resource | Source | In project before audit | LeRobot status | Evidence / lookup |
|---|---|---|---|---|
| A-OKVQA | [T8](https://arxiv.org/html/2607.24744v3#S6.T8) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=A-OKVQA) |
| ADE20K | [T8](https://arxiv.org/html/2607.24744v3#S6.T8) · [source](https://arxiv.org/abs/1608.05442) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=ADE20K) |
| ALFRED | [T8](https://arxiv.org/html/2607.24744v3#S6.T8) · [source](https://arxiv.org/abs/1912.01734) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=ALFRED) |
| ARKitScenes | [T8](https://arxiv.org/html/2607.24744v3#S6.T8) · [source](https://arxiv.org/abs/2111.08897) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=ARKitScenes) |
| Charades-STA | [T8](https://arxiv.org/html/2607.24744v3#S6.T8) · [source](https://arxiv.org/abs/1705.02101) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=Charades-STA) |
| ChartQA | [T8](https://arxiv.org/html/2607.24744v3#S6.T8) · [source](https://arxiv.org/abs/2203.10244) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=ChartQA) |
| CLEVRER | [T8](https://arxiv.org/html/2607.24744v3#S6.T8) · [source](https://arxiv.org/abs/1910.01442) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=CLEVRER) |
| COIN | [T8](https://arxiv.org/html/2607.24744v3#S6.T8) · [source](https://arxiv.org/abs/1903.02874) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=COIN) |
| DiDeMo | [T8](https://arxiv.org/html/2607.24744v3#S6.T8) · [source](https://arxiv.org/abs/1708.01641) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=DiDeMo) |
| DocVQA | [T8](https://arxiv.org/html/2607.24744v3#S6.T8) · [source](https://arxiv.org/abs/2007.00398) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=DocVQA) |
| Ego4D NLQ | [T8](https://arxiv.org/html/2607.24744v3#S6.T8) · [source](https://arxiv.org/abs/2110.07058) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=Ego4D%20NLQ) |
| EgoPlan-IT | [T8](https://arxiv.org/html/2607.24744v3#S6.T8) · [source](https://arxiv.org/abs/2312.06722) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=EgoPlan-IT) |
| EgoTaskQA | [T8](https://arxiv.org/html/2607.24744v3#S6.T8) · [source](https://arxiv.org/abs/2210.03929) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=EgoTaskQA) |
| GraspNet-1Billion | [T8](https://arxiv.org/html/2607.24744v3#S6.T8) · [source](https://openaccess.thecvf.com/content_CVPR_2020/html/Fang_GraspNet-1Billion_A_Large-Scale_Benchmark_for_General_Object_Grasping_CVPR_2020_paper.html) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=GraspNet-1Billion) |
| HiREST | [T8](https://arxiv.org/html/2607.24744v3#S6.T8) · [source](https://arxiv.org/abs/2303.16406) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=HiREST) |
| InfLevel | [T8](https://arxiv.org/html/2607.24744v3#S6.T8) · [source](https://openreview.net/forum?id=9NjqD9i48M) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=InfLevel) |
| IntPhys | [T8](https://arxiv.org/html/2607.24744v3#S6.T8) · [source](https://arxiv.org/abs/1803.07616) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=IntPhys) |
| LLaRP | [T8](https://arxiv.org/html/2607.24744v3#S6.T8) · [source](https://arxiv.org/abs/2310.17722) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=LLaRP) |
| LLaVA-Instruct-150K | [T8](https://arxiv.org/html/2607.24744v3#S6.T8) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=LLaVA-Instruct-150K) |
| LLaVA-OneVision-SI | [T8](https://arxiv.org/html/2607.24744v3#S6.T8) · [source](https://arxiv.org/abs/2408.03326) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=LLaVA-OneVision-SI) |
| LLaVA-Video-178K | [T8](https://arxiv.org/html/2607.24744v3#S6.T8) · [source](https://arxiv.org/abs/2410.02713) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=LLaVA-Video-178K) |
| MMScan | [T8](https://arxiv.org/html/2607.24744v3#S6.T8) · [source](https://arxiv.org/abs/2406.09401) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=MMScan) |
| Moment-10M | [T8](https://arxiv.org/html/2607.24744v3#S6.T8) · [source](https://arxiv.org/abs/2402.11435) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=Moment-10M) |
| MultiUI | [T8](https://arxiv.org/html/2607.24744v3#S6.T8) · [source](https://arxiv.org/abs/2410.13824) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=MultiUI) |
| Objects365 | [T8](https://arxiv.org/html/2607.24744v3#S6.T8) · [source](https://ieeexplore.ieee.org/document/9009553) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=Objects365) |
| OCR-VQA | [T8](https://arxiv.org/html/2607.24744v3#S6.T8) · [source](https://ieeexplore.ieee.org/document/8978122/) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=OCR-VQA) |
| PACO-LVIS | [T8](https://arxiv.org/html/2607.24744v3#S6.T8) · [source](https://arxiv.org/abs/2301.01795) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=PACO-LVIS) |
| PixMo | [T8](https://arxiv.org/html/2607.24744v3#S6.T8) · [source](https://arxiv.org/abs/2409.17146) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=PixMo) |
| PixMo-Points | [T8](https://arxiv.org/html/2607.24744v3#S6.T8) · [source](https://arxiv.org/abs/2409.17146) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=PixMo-Points) |
| RealVLG-11B | [T8](https://arxiv.org/html/2607.24744v3#S6.T8) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=RealVLG-11B) |
| RefCOCO | [T8](https://arxiv.org/html/2607.24744v3#S6.T8) · [source](https://arxiv.org/abs/1608.00272) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=RefCOCO) |
| RH20T-P | [T8](https://arxiv.org/html/2607.24744v3#S6.T8) · [source](https://doi.org/10.1109/iros60139.2025.11246228) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=RH20T-P) |
| RobAVA | [T8](https://arxiv.org/html/2607.24744v3#S6.T8) · [source](https://openaccess.thecvf.com/content/ICCV2025/papers/Sun_RobAVA_A_Large-scale_Dataset_and_Baseline_Towards_Video_based_Robotic_ICCV_2025_paper.pdf) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=RobAVA) |
| RoboAfford++ | [T8](https://arxiv.org/html/2607.24744v3#S6.T8) · [source](https://arxiv.org/abs/2511.12436) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=RoboAfford%2B%2B) |
| RoboFail | [T8](https://arxiv.org/html/2607.24744v3#S6.T8) · [source](https://arxiv.org/abs/2306.15724) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=RoboFail) |
| RoboPoint | [T8](https://arxiv.org/html/2607.24744v3#S6.T8) · [source](https://arxiv.org/abs/2406.10721) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=RoboPoint) |
| RoboVQA | [T8](https://arxiv.org/html/2607.24744v3#S6.T8) · [source](https://arxiv.org/abs/2311.00899) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=RoboVQA) |
| RoVid-X | [T8](https://arxiv.org/html/2607.24744v3#S6.T8) · [source](https://arxiv.org/abs/2601.15282) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=RoVid-X) |
| SA-1B | [T8](https://arxiv.org/html/2607.24744v3#S6.T8) · [source](https://arxiv.org/abs/2304.02643) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=SA-1B) |
| ScanNet | [T8](https://arxiv.org/html/2607.24744v3#S6.T8) · [source](https://www.scan-net.org/) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=ScanNet) |
| ScanNet++ | [T8](https://arxiv.org/html/2607.24744v3#S6.T8) · [source](https://kaldir.vc.in.tum.de/scannetpp/) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=ScanNet%2B%2B) |
| ScanQA | [T8](https://arxiv.org/html/2607.24744v3#S6.T8) · [source](https://arxiv.org/abs/2112.10482) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=ScanQA) |
| ShareGPT4V | [T8](https://arxiv.org/html/2607.24744v3#S6.T8) · [source](https://arxiv.org/abs/2311.12793) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=ShareGPT4V) |
| ShareRobot | [T8](https://arxiv.org/html/2607.24744v3#S6.T8) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=ShareRobot) |
| SQA3D | [T8](https://arxiv.org/html/2607.24744v3#S6.T8) · [source](https://arxiv.org/abs/2210.07474) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=SQA3D) |
| SuctionNet-1Billion | [T8](https://arxiv.org/html/2607.24744v3#S6.T8) · [source](https://arxiv.org/abs/2103.12311) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=SuctionNet-1Billion) |
| TextOCR | [T8](https://arxiv.org/html/2607.24744v3#S6.T8) · [source](https://arxiv.org/abs/2105.05486) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=TextOCR) |
| WildDet3D | [T8](https://arxiv.org/html/2607.24744v3#S6.T8) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=WildDet3D) |

## Real-Robot Data

| Dataset / resource | Source | In project before audit | LeRobot status | Evidence / lookup |
|---|---|---|---|---|
| ALOHA | [§2](https://arxiv.org/html/2607.24744v3#S2) · [source](https://arxiv.org/abs/2304.13705) | Yes | Candidate only | [candidate](https://huggingface.co/datasets/lerobot/aloha_sim_insertion_human) · [Hub search](https://huggingface.co/datasets?search=ALOHA) |
| ArmnetBench v0.1 rollout release | [§2](https://arxiv.org/html/2607.24744v3#S2) · [source](https://arxiv.org/abs/2611.03168) | No match | Format evidence | [v3.0 metadata](https://huggingface.co/datasets/armnet/armnetbench_v01_lerobot_bimanual_so101/blob/main/meta/info.json) · [Hub search](https://huggingface.co/datasets?search=ArmnetBench) |
| DROID-3D | [§2](https://arxiv.org/html/2607.24744v3#S2) · [source](https://arxiv.org/abs/2610.08780) | No match | Format evidence | [v3.0 metadata](https://huggingface.co/datasets/Voxel51/droid-3d-rgb-68ep/blob/main/meta/info.json) · [Hub search](https://huggingface.co/datasets?search=DROID-3D) |
| EgoSteer-RealWorld | Companion · [source](https://arxiv.org/abs/2607.09701) | No match | Format evidence | [v3.0 metadata](https://huggingface.co/datasets/EgoSteer/EgoSteer-RealWorld/blob/main/meta/info.json); [Release card](https://huggingface.co/datasets/EgoSteer/EgoSteer-RealWorld) · [Hub search](https://huggingface.co/datasets?search=EgoSteer-RealWorld) |
| FineART | Companion · [source](https://arxiv.org/abs/2609.36416) | No match | Format evidence | [v3.0 metadata](https://huggingface.co/datasets/lerobot/FineART/blob/main/meta/info.json); [Release card](https://huggingface.co/datasets/lerobot/FineART) · [Hub search](https://huggingface.co/datasets?search=FineART) |
| GazeAct | [§2](https://arxiv.org/html/2607.24744v3#S2) · [source](https://arxiv.org/abs/2610.24507) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=GazeAct) |
| HALO | [§2](https://arxiv.org/html/2607.24744v3#S2) · [source](https://arxiv.org/abs/2611.16439) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=HALO) |
| Handwritten-Alphabet-LfD | Companion · [source](https://arxiv.org/abs/2608.06221) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=Handwritten-Alphabet-LfD) |
| HumanPlus | [§2](https://arxiv.org/html/2607.24744v3#S2) · [source](https://arxiv.org/abs/2406.10454) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=HumanPlus) |
| Mobile ALOHA | Companion · [source](https://arxiv.org/abs/2401.02117) | Yes | Format evidence | [v3.0 metadata](https://huggingface.co/datasets/s-choi/mobile_aloha_lerobot_3.0/blob/main/meta/info.json) · [Hub search](https://huggingface.co/datasets?search=Mobile%20ALOHA) |
| OmniH2O | Companion · [source](https://arxiv.org/abs/2406.08858) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=OmniH2O) |
| OpenNeoData | Companion · [source](https://research.neoteai.com/assets/n0-foundation-paper.pdf) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=OpenNeoData) |
| PanoVLA-Dataset | Companion · [source](https://arxiv.org/abs/2608.02257) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=PanoVLA-Dataset) |
| PrimeBot Household | [§2](https://arxiv.org/html/2607.24744v3#S2) · [§3](https://arxiv.org/html/2607.24744v3#S3) · [source](https://arxiv.org/abs/2609.03591) | No match | Format evidence | [v2.1 metadata](https://huggingface.co/datasets/challenge-2026/challenge_data/blob/main/example_data/robot_data_sample/meta/info.json); [Release card](https://huggingface.co/datasets/challenge-2026/challenge_data) · [Hub search](https://huggingface.co/datasets?search=PrimeBot%20Household) |
| PRISM | [§2](https://arxiv.org/html/2607.24744v3#S2) · [§8](https://arxiv.org/html/2607.24744v3#S8) · [source](https://arxiv.org/abs/2608.17962) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=PRISM) |
| RoboInter-Data | Companion · [source](https://arxiv.org/abs/2607.18709) | No match | Format evidence | [v2.1 metadata](https://huggingface.co/datasets/InternRobotics/RoboInter-Data/blob/main/Annotation_with_action_lerobotv21/lerobot_droid_anno/meta/info.json) · [Hub search](https://huggingface.co/datasets?search=RoboInter-Data) |
| SharpaDex v1.0 | [§2](https://arxiv.org/html/2607.24744v3#S2) · [source](https://huggingface.co/datasets/Sharpa-Robotics/SharpaDex-v1.0) | No match | Format evidence | [Publisher: v2.1 / v3](https://sharpadex.sharpa.com.cn/); [Release card](https://huggingface.co/datasets/Sharpa-Robotics/SharpaDex-v1.0) · [Hub search](https://huggingface.co/datasets?search=SharpaDex%20v1.0) |
| SoftVTBench | [§2](https://arxiv.org/html/2607.24744v3#S2) · [§8](https://arxiv.org/html/2607.24744v3#S8) · [source](https://arxiv.org/abs/2608.18701) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=SoftVTBench) |

## UMI Data

| Dataset / resource | Source | In project before audit | LeRobot status | Evidence / lookup |
|---|---|---|---|---|
| AIRoA-0 | [§3](https://arxiv.org/html/2607.24744v3#S3) · [source](https://arxiv.org/abs/2611.03815) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=AIRoA-0) |
| RUMI | [§3](https://arxiv.org/html/2607.24744v3#S3) · [source](https://arxiv.org/abs/2611.15802) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=RUMI) |
| Soft YUBI | [§3](https://arxiv.org/html/2607.24744v3#S3) · [source](https://arxiv.org/abs/2611.03779) | No match | Format evidence | [Release card](https://huggingface.co/datasets/LuteCorp/soft-yubi-100h); [Publisher tag only](https://huggingface.co/datasets/LuteCorp/soft-yubi-100h) · [Hub search](https://huggingface.co/datasets?search=Soft%20YUBI) |
| UMI-Live | [§3](https://arxiv.org/html/2607.24744v3#S3) · [source](https://arxiv.org/abs/2610.39385) | No match | Candidate only | [candidate](https://huggingface.co/datasets/brandonyang/umi-live-test) · [Hub search](https://huggingface.co/datasets?search=UMI-Live) |

## Egocentric & Ego-Exo Data

| Dataset / resource | Source | In project before audit | LeRobot status | Evidence / lookup |
|---|---|---|---|---|
| ACE-Data-0 | [§4](https://arxiv.org/html/2607.24744v3#S4) · [§8](https://arxiv.org/html/2607.24744v3#S8) · [source](https://arxiv.org/abs/2607.28625) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=ACE-Data-0) |
| ADT | Companion · [source](https://arxiv.org/abs/2306.06362) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=ADT) |
| AEA | Companion · [source](https://arxiv.org/abs/2402.13349) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=AEA) |
| CMU-MMAC | Companion · [source](https://publications.ri.cmu.edu/guide-to-the-carnegie-mellon-university-multimodal-activity-cmu-mmac-database) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=CMU-MMAC) |
| CS2-10k | Companion · [source](https://reka.ai/news/cs2-10k-a-large-scale-egocentric-counter-strike-2-dataset) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=CS2-10k) |
| DreamHand | [§4](https://arxiv.org/html/2607.24744v3#S4) · [source](https://arxiv.org/abs/2608.20308) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=DreamHand) |
| EGO-CH | Companion · [source](https://arxiv.org/abs/2002.00899) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=EGO-CH) |
| Ego-Deliver | Companion · [source](https://dl.acm.org/doi/10.1145/3474085.3475336) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=Ego-Deliver) |
| Ego-Exo4D-HM | [§4](https://arxiv.org/html/2607.24744v3#S4) · [source](https://arxiv.org/abs/2609.30187) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=Ego-Exo4D-HM) |
| Ego-EXTRA | Companion · [source](https://arxiv.org/abs/2512.13238) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=Ego-EXTRA) |
| Ego2Robot | Companion · [source](https://arxiv.org/abs/2608.02580) | No match | Candidate only | [candidate](https://huggingface.co/datasets/introvoyz041/ego2robot-factory-episodes) · [Hub search](https://huggingface.co/datasets?search=Ego2Robot) |
| EgoAIM / Gaze2HOI | Companion · [source](https://arxiv.org/abs/2610.27877) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=EgoAIM) |
| EgoBody | Companion · [source](https://arxiv.org/abs/2112.07642) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=EgoBody) |
| EgoCart | Companion · [source](https://iplab.dmi.unict.it/fpv/publications/spera2018egocentric.pdf) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=EgoCart) |
| EgoCom | Companion · [source](https://doi.org/10.1109/TPAMI.2020.3025105) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=EgoCom) |
| EgoConvNet | Companion · [source](https://openaccess.thecvf.com/content_cvpr_2016/html/Singh_First_Person_Action_CVPR_2016_paper.html) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=EgoConvNet) |
| EgoDexter | Companion · [source](https://handtracker.mpi-inf.mpg.de/projects/OccludedHands/index.htm) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=EgoDexter) |
| EgoEMG | [§4](https://arxiv.org/html/2607.24744v3#S4) · [source](https://arxiv.org/abs/2605.05712) | No match | Format evidence | [memmap_export_v1 metadata](https://huggingface.co/datasets/IInfact/EgoEMG-snippet/blob/main/meta/info.json) · [Hub search](https://huggingface.co/datasets?search=EgoEMG) |
| EgoEngine | Companion · [source](https://arxiv.org/abs/2606.12604) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=EgoEngine) |
| EgoEVHands | Companion · [source](https://arxiv.org/abs/2605.12297) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=EgoEVHands) |
| EgoExOR | [§4](https://arxiv.org/html/2607.24744v3#S4) · [source](https://proceedings.neurips.cc/paper_files/paper/2025/hash/5e3ffa2c53dce23986ca0f8d1d2bbc7e-Abstract-Datasets_and_Benchmarks_Track.html) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=EgoExOR) |
| EgoExplorer | [§4](https://arxiv.org/html/2607.24744v3#S4) · [source](https://arxiv.org/abs/2610.18872) | No match | Format evidence | [Publisher: v3 release](https://github.com/InternRobotics/EgoExplorer) · [Hub search](https://huggingface.co/datasets?search=EgoExplorer) |
| EgoForce | Companion · [source](https://arxiv.org/abs/2610.19155) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=EgoForce) |
| EgoFun3D | Companion · [source](https://arxiv.org/abs/2604.11038) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=EgoFun3D) |
| EgoGesture | Companion · [source](https://nlpr.ia.ac.cn/iva/yfzhang/datasets/EgoGesture.pdf) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=EgoGesture) |
| EgoHand | [§4](https://arxiv.org/html/2607.24744v3#S4) · [source](https://arxiv.org/abs/2610.30293) | No match | Candidate only | [candidate](https://huggingface.co/datasets/pepijn223/egovista-kitchen-manipulation-v1-egohand-soma-uncapped) · [Hub search](https://huggingface.co/datasets?search=EgoHand) |
| EgoHOS | Companion · [source](https://arxiv.org/abs/2208.03826) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=EgoHOS) |
| EgoHTR | Companion · [source](https://arxiv.org/abs/2607.13472) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=EgoHTR) |
| EgoMatrix | [§4](https://arxiv.org/html/2607.24744v3#S4) · [source](https://arxiv.org/abs/2610.18822) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=EgoMatrix) |
| EgoObjects | Companion · [source](https://arxiv.org/abs/2309.08816) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=EgoObjects) |
| EgoOops | Companion · [source](https://arxiv.org/abs/2410.05343) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=EgoOops) |
| EgoPAT3D | Companion · [source](https://arxiv.org/abs/2203.13116) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=EgoPAT3D) |
| EgoPressure | Companion · [source](https://arxiv.org/abs/2409.02224) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=EgoPressure) |
| EgoSPT | Companion · [source](https://arxiv.org/abs/2605.20085) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=EgoSPT) |
| EgoSteer | Companion · [source](https://arxiv.org/abs/2607.09701) | Yes | Tagged release | [Publisher tag only](https://huggingface.co/datasets/EgoSteer/EgoSteer-Egocentric) · [Hub search](https://huggingface.co/datasets?search=EgoSteer) |
| EgoSuite-Open100K | Companion · [source](https://huggingface.co/blog/LightwheelAI/egosuite-open100k) | Yes | Format evidence | [Publisher: EgoDemo / EgoPro samples](https://huggingface.co/datasets/LightwheelAI/EgoDemo) · [Hub search](https://huggingface.co/datasets?search=EgoSuite-Open100K) |
| EgoTac | [§4](https://arxiv.org/html/2607.24744v3#S4) · [§8](https://arxiv.org/html/2607.24744v3#S8) · [source](https://arxiv.org/abs/2608.15060) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=EgoTac) |
| EgoTactile | Companion · [source](https://arxiv.org/abs/2606.09243) | No match | Format evidence | [v3.0 metadata](https://huggingface.co/datasets/OpenGraphLabs-Research/ego-tactile-manipulation/blob/main/meta/info.json) · [Hub search](https://huggingface.co/datasets?search=EgoTactile) |
| EgoTouch | [§4](https://arxiv.org/html/2607.24744v3#S4) · [source](https://arxiv.org/abs/2605.13083) | No match | Tagged release | [Publisher tag only](https://huggingface.co/datasets/easyminnn/egotouch-lerobot) · [Hub search](https://huggingface.co/datasets?search=EgoTouch) |
| EgoTraj | Companion · [source](https://arxiv.org/abs/2605.19004) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=EgoTraj) |
| EgoVid-5M | Companion · [source](https://arxiv.org/abs/2411.08380) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=EgoVid-5M) |
| EgoWild2Dex / EgoWild | Companion · [source](https://arxiv.org/abs/2609.23755) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=EgoWild2Dex) |
| EgoX-Data-6M / EgoXperience | Companion · [source](https://arxiv.org/abs/2610.26625) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=EgoX-Data-6M) |
| EgoXtreme | Companion · [source](https://arxiv.org/abs/2603.25135) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=EgoXtreme) |
| FEEL | [§4](https://arxiv.org/html/2607.24744v3#S4) · [source](https://arxiv.org/abs/2603.15847) | No match | Tagged release | [Publisher tag only](https://huggingface.co/datasets/FeelAuthors/FEEL-Benchmark) · [Hub search](https://huggingface.co/datasets?search=FEEL) |
| HandEdit | [§4](https://arxiv.org/html/2607.24744v3#S4) · [source](https://arxiv.org/abs/2608.12122) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=HandEdit) |
| HaWoR | Companion · [source](https://arxiv.org/abs/2501.02973) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=HaWoR) |
| HumanCLAW | Companion · [source](https://arxiv.org/abs/2607.27180) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=HumanCLAW) |
| HumanEgo | Companion · [source](https://arxiv.org/abs/2605.24934) | No match | Format evidence | [v2.1 metadata](https://huggingface.co/datasets/Coffeecoderss/humanego_serve_bread_lingbot_lerobot_with_latents/blob/main/humanego_serve_bread_lingbot_eef_train/meta/info.json) · [Hub search](https://huggingface.co/datasets?search=HumanEgo) |
| HumanVerse / lambda0 | Companion · [source](https://arxiv.org/abs/2610.18950) | No match | No verified release | [Export / pipeline documented; public output unverified](https://github.com/LambdaHumanoid/openlambda) · [Hub search](https://huggingface.co/datasets?search=HumanVerse) |
| HuRo | [§4](https://arxiv.org/html/2607.24744v3#S4) · [source](https://arxiv.org/abs/2609.10706) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=HuRo) |
| LEMMA | Companion · [source](https://arxiv.org/abs/2007.15781) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=LEMMA) |
| MECCANO | Companion · [source](https://arxiv.org/abs/2010.05654) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=MECCANO) |
| MobileEgo Anywhere | Companion · [source](https://arxiv.org/abs/2605.05945) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=MobileEgo%20Anywhere) |
| MOVE | [§4](https://arxiv.org/html/2607.24744v3#S4) · [§6](https://arxiv.org/html/2607.24744v3#S6) · [source](https://arxiv.org/abs/2608.00486) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=MOVE) |
| NVIDIA PhysicalAI Human-1M-100K | Companion · [source](https://huggingface.co/datasets/nvidia/PhysicalAI-Human-1M-100K) | Yes | Format evidence | [Publisher: v3 shards](https://huggingface.co/datasets/nvidia/PhysicalAI-Human-1M-100K); [Release card](https://huggingface.co/datasets/nvidia/PhysicalAI-Human-1M-100K) · [Hub search](https://huggingface.co/datasets?search=NVIDIA%20PhysicalAI%20Human-1M-100K) |
| Nymeria | [§4](https://arxiv.org/html/2607.24744v3#S4) · [source](https://arxiv.org/abs/2406.09905) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=Nymeria) |
| Open-HumanWAM-50K | Companion · [source](https://arxiv.org/abs/2611.06817) | No match | Tagged release | [Publisher tag only](https://huggingface.co/datasets/DAGroup-PKU/Open-HumanWAM-50K) · [Hub search](https://huggingface.co/datasets?search=Open-HumanWAM-50K) |
| Pegasus | [§4](https://arxiv.org/html/2607.24744v3#S4) · [source](https://arxiv.org/abs/2607.26903) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=Pegasus) |
| PEV | Companion · [source](https://openaccess.thecvf.com/content_cvpr_2016/html/Yonetani_Recognizing_Micro-Actions_and_CVPR_2016_paper.html) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=PEV) |
| PVSG | Companion · [source](https://arxiv.org/abs/2311.17058) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=PVSG) |
| React / ACTS | Companion · [source](https://arxiv.org/abs/2610.24285) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=React) |
| RekaDaily-10k | Companion · [source](https://reka.ai/news/rekadaily-10k-egocentric-household-manipulation-data) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=RekaDaily-10k) |
| RoboMoCap | [§4](https://arxiv.org/html/2607.24744v3#S4) · [source](https://arxiv.org/abs/2611.10994) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=RoboMoCap) |
| RoboReact | [§4](https://arxiv.org/html/2607.24744v3#S4) · [source](https://arxiv.org/abs/2608.03387) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=RoboReact) |
| SiMDex | [§4](https://arxiv.org/html/2607.24744v3#S4) · [source](https://arxiv.org/abs/2608.04196) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=SiMDex) |
| THU-READ | Companion · [source](https://doi.org/10.1109/ICIP.2017.8296915) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=THU-READ) |
| ToolDex | [§4](https://arxiv.org/html/2607.24744v3#S4) · [source](https://arxiv.org/abs/2611.09036) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=ToolDex) |
| Touch and Go | [§4](https://arxiv.org/html/2607.24744v3#S4) · [source](https://arxiv.org/abs/2211.12498) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=Touch%20and%20Go) |
| V-JEPA Hand | Companion · [source](https://arxiv.org/abs/2610.26780) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=V-JEPA%20Hand) |
| VLAff | [§4](https://arxiv.org/html/2607.24744v3#S4) · [source](https://arxiv.org/abs/2608.05215) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=VLAff) |
| WEAR | [§4](https://arxiv.org/html/2607.24744v3#S4) · [§5](https://arxiv.org/html/2607.24744v3#S5) · [source](https://arxiv.org/abs/2304.05088) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=WEAR) |
| World In Your Hands | Companion · [source](https://arxiv.org/abs/2512.24310) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=World%20In%20Your%20Hands) |
| You2Me | Companion · [source](https://arxiv.org/abs/1904.09882) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=You2Me) |

## 3D Assets & Scene Datasets

| Dataset / resource | Source | In project before audit | LeRobot status | Evidence / lookup |
|---|---|---|---|---|
| 3D-FRONT | [§5](https://arxiv.org/html/2607.24744v3#S5) · [source](https://arxiv.org/abs/2011.09127) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=3D-FRONT) |
| ABO | [§5](https://arxiv.org/html/2607.24744v3#S5) · [source](https://arxiv.org/abs/2110.06199) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=ABO) |
| GSO | [§5](https://arxiv.org/html/2607.24744v3#S5) · [source](https://arxiv.org/abs/2204.11918) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=GSO) |
| HM3D | [§5](https://arxiv.org/html/2607.24744v3#S5) · [source](https://arxiv.org/abs/2109.08238) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=HM3D) |
| HSSD-200 | [§5](https://arxiv.org/html/2607.24744v3#S5) · [source](https://arxiv.org/abs/2306.11290) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=HSSD) |
| ManiTwin-100K | Companion · [source](https://arxiv.org/abs/2603.16866) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=ManiTwin-100K) |
| Matterport3D | [§5](https://arxiv.org/html/2607.24744v3#S5) · [source](https://arxiv.org/abs/1709.06158) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=Matterport3D) |
| Objaverse | [§5](https://arxiv.org/html/2607.24744v3#S5) · [source](https://arxiv.org/abs/2212.08051) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=Objaverse) |
| Objaverse-XL | [§5](https://arxiv.org/html/2607.24744v3#S5) · [source](https://arxiv.org/abs/2307.05663) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=Objaverse-XL) |
| ObjectFolder 2.0 | [§5](https://arxiv.org/html/2607.24744v3#S5) · [source](https://arxiv.org/abs/2204.02389) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=ObjectFolder%202.0) |
| OmniObject3D | [§5](https://arxiv.org/html/2607.24744v3#S5) · [source](https://arxiv.org/abs/2301.07525) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=OmniObject3D) |
| PhysX-Mobility | [§5](https://arxiv.org/html/2607.24744v3#S5) · [source](https://arxiv.org/abs/2511.13648) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=PhysX-Mobility) |
| PhysXNet & PhysXNet-XL | Companion · [source](https://arxiv.org/abs/2507.12465) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=PhysXNet%20%26%20PhysXNet-XL) |
| PhysXVerse | [§5](https://arxiv.org/html/2607.24744v3#S5) · [source](https://arxiv.org/abs/2605.21572) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=PhysXVerse) |
| ProcTHOR | [§5](https://arxiv.org/html/2607.24744v3#S5) · [source](https://arxiv.org/abs/2206.06994) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=ProcTHOR) |
| Replica | [§2](https://arxiv.org/html/2607.24744v3#S2) · [§5](https://arxiv.org/html/2607.24744v3#S5) · [source](https://arxiv.org/abs/1906.05797) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=Replica) |
| ShapeNet | [§5](https://arxiv.org/html/2607.24744v3#S5) · [source](https://arxiv.org/abs/1512.03012) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=ShapeNet) |

## Benchmarks

| Dataset / resource | Source | In project before audit | LeRobot status | Evidence / lookup |
|---|---|---|---|---|
| CuraEval | [§5](https://arxiv.org/html/2607.24744v3#S5) · [source](https://arxiv.org/abs/2610.38221) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=CuraEval) |
| DexArena | [§5](https://arxiv.org/html/2607.24744v3#S5) · [source](https://arxiv.org/abs/2611.02629) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=DexArena) |
| Evo-DexBench | Companion · [source](https://arxiv.org/abs/2610.21180) | No match | Tagged release | [Publisher tag only](https://huggingface.co/datasets/MINT-SJTU/Evo-DexBench-dataset) · [Hub search](https://huggingface.co/datasets?search=Evo-DexBench) |
| FlatLab | [§5](https://arxiv.org/html/2607.24744v3#S5) · [source](https://arxiv.org/abs/2608.14049) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=FlatLab) |
| HARP-Bench | [§5](https://arxiv.org/html/2607.24744v3#S5) · [source](https://arxiv.org/abs/2611.11123) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=HARP-Bench) |
| LIBERO-PeRM | Companion · [source](https://arxiv.org/abs/2610.22372) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=LIBERO-PeRM) |
| MIKASA | Companion · [source](https://arxiv.org/abs/2502.10550) | No match | Candidate only | [candidate](https://huggingface.co/datasets/liyouzhou/mikasa_robo_all_lerobot) · [Hub search](https://huggingface.co/datasets?search=MIKASA) |
| RoboQuest | Companion · [source](https://arxiv.org/abs/2610.10388) | No match | Format evidence | [Publisher: task-specific v2.1 data](https://github.com/declare-lab/RoboQuest); [Publisher tag only](https://huggingface.co/datasets/declare-lab/RoboQuest) · [Hub search](https://huggingface.co/datasets?search=RoboQuest) |
| SoftGym | [§5](https://arxiv.org/html/2607.24744v3#S5) · [source](https://arxiv.org/abs/2011.07215) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=SoftGym) |

## Simulation/Synthetic Datasets & Data-Generation Systems

| Dataset / resource | Source | In project before audit | LeRobot status | Evidence / lookup |
|---|---|---|---|---|
| ACRONYM | [§6](https://arxiv.org/html/2607.24744v3#S6) · [source](https://arxiv.org/abs/2011.09584) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=ACRONYM) |
| ARSTAG | [§5](https://arxiv.org/html/2607.24744v3#S5) · [source](https://arxiv.org/abs/2609.24563) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=ARSTAG) |
| AutoRSR | [§5](https://arxiv.org/html/2607.24744v3#S5) · [source](https://arxiv.org/abs/2610.20336) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=AutoRSR) |
| AXIS | [§5](https://arxiv.org/html/2607.24744v3#S5) · [source](https://arxiv.org/abs/2607.21588) | No match | Candidate only | [Export / pipeline documented; public output unverified](https://github.com/AxisAIOrg/Axis-V1-Training) · [candidate](https://huggingface.co/datasets/knightnemo/kimodo-x-axis-lerobot-top100-v1) · [Hub search](https://huggingface.co/datasets?search=AXIS) |
| ClothDojo | [§5](https://arxiv.org/html/2607.24744v3#S5) · [source](https://arxiv.org/abs/2611.01190) | No match | Format evidence | [v2.1 metadata](https://huggingface.co/datasets/clothdojo/flatten/blob/main/meta/info.json) · [Hub search](https://huggingface.co/datasets?search=ClothDojo) |
| DemoStream | [§5](https://arxiv.org/html/2607.24744v3#S5) · [source](https://arxiv.org/abs/2610.22020) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=DemoStream) |
| DexSeed | [§5](https://arxiv.org/html/2607.24744v3#S5) · [source](https://arxiv.org/abs/2611.14092) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=DexSeed) |
| DiscoDemo | [§5](https://arxiv.org/html/2607.24744v3#S5) · [source](https://arxiv.org/abs/2610.32093) | No match | Format evidence | [v3.0 metadata](https://huggingface.co/datasets/DAVIAN-Robotics/DiscoDemo-Stage2_GenData-PnP_Banana/blob/main/meta/info.json) · [Hub search](https://huggingface.co/datasets?search=DiscoDemo) |
| DreamGen | [§5](https://arxiv.org/html/2607.24744v3#S5) · [source](https://arxiv.org/abs/2505.12705) | No match | Candidate only | [Export / pipeline documented; public output unverified](https://github.com/NVIDIA/GR00T-Dreams) · [candidate](https://huggingface.co/datasets/Joelkabura/gr1-lerobot-dreamgen-2025-08-29) · [Hub search](https://huggingface.co/datasets?search=DreamGen) |
| FetchMan | Companion · [source](https://arxiv.org/abs/2608.17027) | No match | Format evidence | [v3.0 metadata](https://huggingface.co/datasets/allenai/fetchman-data/blob/main/meta/info.json) · [Hub search](https://huggingface.co/datasets?search=FetchMan) |
| GenSim | [§5](https://arxiv.org/html/2607.24744v3#S5) · [source](https://arxiv.org/abs/2310.01361) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=GenSim) |
| GenSim2 | [§5](https://arxiv.org/html/2607.24744v3#S5) · [source](https://arxiv.org/abs/2410.03645) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=GenSim2) |
| MATE | Companion · [source](https://arxiv.org/abs/2609.26520) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=MATE) |
| MetaGenSim | Companion · [source](https://arxiv.org/abs/2610.19479) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=MetaGenSim) |
| MOMASPLAT | [§5](https://arxiv.org/html/2607.24744v3#S5) · [source](https://arxiv.org/abs/2611.08372) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=MOMASPLAT) |
| ReShoot | Companion · [source](https://arxiv.org/abs/2609.19661) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=ReShoot) |
| RoboGen | [§5](https://arxiv.org/html/2607.24744v3#S5) · [source](https://arxiv.org/abs/2311.01455) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=RoboGen) |
| ScheduleGen | [§5](https://arxiv.org/html/2607.24744v3#S5) · [source](https://arxiv.org/abs/2610.39429) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=ScheduleGen) |
| Self-Demonstrated Generative Control | Companion · [source](https://arxiv.org/abs/2608.19490) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=Self-Demonstrated%20Generative%20Control) |

## Visual Data

| Dataset / resource | Source | In project before audit | LeRobot status | Evidence / lookup |
|---|---|---|---|---|
| COCO | [§6](https://arxiv.org/html/2607.24744v3#S6) · [source](https://arxiv.org/abs/1405.0312) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=COCO) |
| FiRE | Companion · [source](https://dl.acm.org/doi/10.1145/3726302.3729979) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=FiRE) |
| Visual Genome | [§6](https://arxiv.org/html/2607.24744v3#S6) · [source](https://arxiv.org/abs/1602.07332) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=Visual%20Genome) |
| VQA | [§6](https://arxiv.org/html/2607.24744v3#S6) · [§7](https://arxiv.org/html/2607.24744v3#S7) · [source](https://arxiv.org/abs/1505.00468) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=VQA) |

## Segmentation & Localization

| Dataset / resource | Source | In project before audit | LeRobot status | Evidence / lookup |
|---|---|---|---|---|
| 3DSSG | Companion · [source](https://arxiv.org/abs/2004.03967) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=3DSSG) |
| 3RScan | [§6](https://arxiv.org/html/2607.24744v3#S6) · [source](https://arxiv.org/abs/1908.06109) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=3RScan) |
| COLMAP | Companion · [source](https://openaccess.thecvf.com/content_cvpr_2016/html/Schonberger_Structure-From-Motion_Revisited_CVPR_2016_paper.html) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=COLMAP) |
| LVIS | [§6](https://arxiv.org/html/2607.24744v3#S6) · [source](https://arxiv.org/abs/1908.03195) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=LVIS) |
| ORB-SLAM | Companion · [source](https://arxiv.org/abs/1502.00956) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=ORB-SLAM) |
| PTG-FSCIR | Companion · [source](https://arxiv.org/abs/2407.06001) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=PTG-FSCIR) |
| VL-Grasp | Companion · [source](https://arxiv.org/abs/2308.00640) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=VL-Grasp) |
| VOST | Companion · [source](https://arxiv.org/abs/2212.06200) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=VOST) |

## Video & Temporal Data

| Dataset / resource | Source | In project before audit | LeRobot status | Evidence / lookup |
|---|---|---|---|---|
| Cornell Grasp Dataset | [§6](https://arxiv.org/html/2607.24744v3#S6) · [source](https://doi.org/10.1109/ICRA.2011.5980145) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=Cornell%20Grasp%20Dataset) |
| D2E | Companion · [source](https://arxiv.org/abs/2510.05684) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=D2E) |
| FLORA | [§2](https://arxiv.org/html/2607.24744v3#S2) · [source](https://arxiv.org/abs/2610.31779) | No match | Candidate only | [candidate](https://huggingface.co/datasets/pepijn223/abc_130k_v3_train-annotated_flora) · [Hub search](https://huggingface.co/datasets?search=FLORA) |
| KiRoSe | [§2](https://arxiv.org/html/2607.24744v3#S2) · [source](https://arxiv.org/abs/2610.31801) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=KiRoSe) |
| PLAICraft | Companion · [source](https://arxiv.org/abs/2505.12707) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=PLAICraft) |

## Planning / Task Decomposition

| Dataset / resource | Source | In project before audit | LeRobot status | Evidence / lookup |
|---|---|---|---|---|
| EmbodiedGPT | Companion · [source](https://arxiv.org/abs/2305.15021) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=EmbodiedGPT) |
| SCOPE | [§2](https://arxiv.org/html/2607.24744v3#S2) · [§4](https://arxiv.org/html/2607.24744v3#S4) · [source](https://arxiv.org/abs/2610.31518) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=SCOPE) |
| WAP | Companion · [source](https://arxiv.org/abs/2506.21230) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=WAP) |

## Grasp Data

| Dataset / resource | Source | In project before audit | LeRobot status | Evidence / lookup |
|---|---|---|---|---|
| Grasp-Anything | [§6](https://arxiv.org/html/2607.24744v3#S6) · [source](https://arxiv.org/abs/2309.09818) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=Grasp-Anything) |
| Jacquard | [§6](https://arxiv.org/html/2607.24744v3#S6) · [source](https://arxiv.org/abs/1803.11469) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=Jacquard) |
| MapleGrasp | Companion · [source](https://arxiv.org/abs/2506.06535) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=MapleGrasp) |

## Narrative

| Dataset / resource | Source | In project before audit | LeRobot status | Evidence / lookup |
|---|---|---|---|---|
| DexGloveHOI | [§4](https://arxiv.org/html/2607.24744v3#S4) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=DexGloveHOI) |
| DreamTraj | [§4](https://arxiv.org/html/2607.24744v3#S4) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=DreamTraj) |
| EgoCOT | [§6](https://arxiv.org/html/2607.24744v3#S6) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=EgoCOT) |
| EgoEV-HandPose | [§4](https://arxiv.org/html/2607.24744v3#S4) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=EgoEV-HandPose) |
| Grasp-Anything-6D | [§6](https://arxiv.org/html/2607.24744v3#S6) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=Grasp-Anything-6D) |
| PartNet-Mobility | [§5](https://arxiv.org/html/2607.24744v3#S5) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=PartNet-Mobility) |
| RefGraspNet | [§6](https://arxiv.org/html/2607.24744v3#S6) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=RefGraspNet) |
| ReTouch | [§8](https://arxiv.org/html/2607.24744v3#S8) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=ReTouch) |
| RoboInter1.5 | [§2](https://arxiv.org/html/2607.24744v3#S2) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=RoboInter1.5) |
| RoboMIND-Sim | [§5](https://arxiv.org/html/2607.24744v3#S5) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=RoboMIND-Sim) |
| RoboRefIt | [§6](https://arxiv.org/html/2607.24744v3#S6) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=RoboRefIt) |
| VTLA | [§8](https://arxiv.org/html/2607.24744v3#S8) | No match | No verified release | [Hub search](https://huggingface.co/datasets?search=VTLA) |
