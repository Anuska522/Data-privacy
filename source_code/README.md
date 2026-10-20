# AI-Driven Privacy Compliance in Heterogeneous IoT Environments
### Course: BCSE318L Data Privacy | Case-Study Report Implementation Package
**Author:** Anuska Saha (Registration No: 23BCE0167)  
**Team ID:** 26FSDPYCPMID1029  
**Faculty / Guide:** Dr. M Rajasekhara Babu  
**School:** School of Computer Science and Engineering (SCOPE), Vellore Institute of Technology (VIT)  

---

## 1. Project Overview

This repository houses the reproducible experimental pipeline, synthetic benchmark dataset (N=6,000), 600 DPI publication-grade architectural diagrams, and interactive compliance simulation for the case-study report titled:
> **"AI-Driven Privacy Compliance in Heterogeneous IoT Environments"**

The project proposes a **6-plane governance architecture** (Device, Acquisition, Edge Governance, Compliance & AI Risk, Evidence, Oversight) that couples deterministic policy constraints with supervised machine-learning risk signals to ensure automated, auditable, and regulatory-compliant data handling across diverse IoT ecosystems (Healthcare, Smart Cities, Manufacturing, Energy, Agriculture, Transport).

---

## 2. Directory Structure

```text
data_privacy_project_part_2/
├── datasets/
│   ├── iot_privacy_compliance_dataset.csv  # Full 6,000 synthetic IoT events
│   ├── train_set.csv                      # Stratified training partition (4,500 rows)
│   ├── test_set.csv                       # Stratified held-out test partition (1,500 rows)
│   └── DATASET_CARD.md                    # Comprehensive data dictionary & ethical statement
├── source_code/
│   ├── benchmark_pipeline.py              # Main reproducible benchmark & evaluation script
│   ├── interactive_demo.py                # Live terminal streaming simulation for demo/video
│   ├── generate_all_architectural_figures.py # 600 DPI diagram synthesizer
│   ├── generate_drawio.py                 # Multi-page Draw.io XML generator
│   ├── requirements.txt                   # Dependency manifest
│   └── README.md                          # Execution & replication guide
├── diagrams/
│   ├── Fig 01 ... Fig 34 (.png)           # 34 original 600 DPI figures
│   └── all_diagrams.drawio                # Editable Draw.io / Diagrams.net source
├── execution_videos/
│   ├── DEMO_WALKTHROUGH_SCRIPT.md         # Video narration script with timestamps
│   └── RECORDING_GUIDELINES.md            # Video recording checklist
├── results/
│   ├── experiment_metrics.json            # Model performance JSON
│   ├── held_out_test_predictions.csv      # Test predictions with probability scores
│   └── rf_feature_importances.csv         # Random Forest feature rankings
└── manuscript/
    └── AI_Driven_Privacy_Compliance_in_Heterogeneous_IoT_Environments.docx # Complete report
```

---

## 3. Environment Setup & Installation

Clone this repository and set up a Python virtual environment:

```bash
# Clone the repository (replace with your repo URL once uploaded to GitHub)
git clone https://github.com/anuska-saha/iot-privacy-compliance-framework.git
cd iot-privacy-compliance-framework

# Install dependencies
pip install -r source_code/requirements.txt
```

---

## 4. Reproducing the Synthetic Benchmark

Run the main benchmark pipeline to execute the stratified train/test split, train the Random Forest model, evaluate the Checklist baseline and Hybrid detector, and generate all performance charts:

```bash
cd source_code
python benchmark_pipeline.py
```

### Verified Benchmark Output (Matching Manuscript Table 11):

| Method | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Checklist baseline** | 0.6640 (66.40%) | 0.7137 (71.37%) | 0.2902 (29.02%) | 0.4126 (0.413) | *Not calculated* |
| **Random Forest** | 0.6873 (68.73%) | 0.6158 (61.58%) | 0.6148 (61.48%) | 0.6153 (0.615) | 0.7423 |
| **Hybrid rules + AI** | 0.6427 (64.27%) | 0.5413 (54.13%) | 0.7951 (79.51%) | 0.6441 (0.644) | 0.7405 |

---

## 5. Running the Interactive Demo for Video Recording

To record the execution video required by course deliverables, launch the interactive live streaming simulation:

```bash
cd source_code
python interactive_demo.py
```

This streams sample IoT events across Healthcare, Smart Cities, Manufacturing, Energy, and Agriculture, demonstrating:
1. Multi-attribute schema and identity verification
2. Edge data minimization and cryptographic validation
3. Deterministic policy enforcement (Rules R-01 to R-08)
4. Supervised AI risk probability prediction
5. Graduated action selection (`ALLOW`, `HOLD FOR REVIEW`, `BLOCK & QUARANTINE`)
6. Generation of tamper-evident SHA-256 audit hashes.

---

## 6. Pushing to GitHub (Deliverable Compliance)

To publish this source code folder onto GitHub as recommended in the course guidelines:

```bash
git init
git add .
git commit -m "Initial release: AI-Driven Privacy Compliance Framework deliverables"
git branch -M main
git remote add origin https://github.com/<your-username>/<your-repo-name>.git
git push -u origin main
```

---

## 7. Data Availability Statement

All synthetic data generated and analyzed during this study are included in the `datasets/` folder:
- `datasets/iot_privacy_compliance_dataset.csv`
- `datasets/train_set.csv`
- `datasets/test_set.csv`
- `datasets/DATASET_CARD.md`

No real personal data or patient records were collected or distributed.
