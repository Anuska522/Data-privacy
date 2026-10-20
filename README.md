# AI-Driven Privacy Compliance in Heterogeneous IoT Environments

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Course: BCSE318L Data Privacy](https://img.shields.io/badge/Course-BCSE318L%20Data%20Privacy-orange.svg)](https://vit.ac.in/)

**Author:** Anuska Saha  
**Registration Number:** 23BCE0167  
**Team ID:** 26FSDPYCPMID1029  
**Faculty / Guide:** Dr. M Rajasekhara Babu  
**Institution:** School of Computer Science and Engineering (SCOPE), Vellore Institute of Technology (VIT)  

---

## 📌 Executive Summary

Heterogeneous Internet of Things (IoT) deployments—encompassing healthcare telemetry, smart-city cameras, industrial controllers, smart meters, agriculture sensors, and connected logistics—face severe compliance bottlenecks under evolving privacy regulations such as the **General Data Protection Regulation (GDPR)**, **EU AI Act (2024/1689)**, and **India's Digital Personal Data Protection (DPDP) Act, 2023 with its 2025 Rules**.

This repository provides the complete implementation package, reproducible synthetic benchmark, and publication artifacts for a **6-plane governance framework** that integrates:
- Deterministic policy rules for non-negotiable constraints (consent, encryption, retention, purpose validation).
- Edge-based local data minimization and filtering before raw data egress.
- Explainable AI (Random Forest) risk scoring for anomaly triage.
- Tamper-evident cryptographic audit records (SHA-256).
- Human-in-the-loop oversight workflows.

---

## 🏗 System Architecture (Six Logical Planes)

```text
+-----------------------------------------------------------------------------------+
|  [6] OVERSIGHT PLANE: Human Reviewers, DPO Triage, Incident Response & Appeals    |
+-----------------------------------------------------------------------------------+
                                          ▲
+-----------------------------------------------------------------------------------+
|  [5] EVIDENCE PLANE: Tamper-Evident SHA-256 Logs, Data Lineage & Audit Registry   |
+-----------------------------------------------------------------------------------+
                                          ▲
+-----------------------------------------------------------------------------------+
|  [4] COMPLIANCE & AI RISK PLANE: Deterministic Rules Engine + Supervised RF Model |
+-----------------------------------------------------------------------------------+
                                          ▲
+-----------------------------------------------------------------------------------+
|  [3] EDGE GOVERNANCE PLANE: Local Minimization, Filtering & Signed Policy Cache   |
+-----------------------------------------------------------------------------------+
                                          ▲
+-----------------------------------------------------------------------------------+
|  [2] ACQUISITION PLANE: Schema Validation, Authenticated Ingest, Sensitivity Tags |
+-----------------------------------------------------------------------------------+
                                          ▲
+-----------------------------------------------------------------------------------+
|  [1] DEVICE & SENSOR PLANE: Device Identity, Attestation & Cross-Domain Telemetry |
+-----------------------------------------------------------------------------------+
```

---

## 📊 Experimental Results (N=6,000 Synthetic Events, 1,500 Held-Out Test Set)

Evaluated on 1,500 held-out test events with fixed random seed 42 across 6 IoT domains:

| Method | Accuracy | Precision | Recall | F1-Score | ROC-AUC | Decision Role |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Checklist baseline** | 66.40% | **71.37%** | 29.02% | 0.4126 | *N/A* | Strict enforcement of hard stops |
| **Random Forest** | **68.73%** | 61.58% | 61.48% | 0.6153 | **0.7423** | Statistical outlier detection |
| **Hybrid rules + AI** | 64.27% | 54.13% | **79.51%** | **0.6441** | 0.7405 | Triage & high-recall candidate flagging |

---

## 📁 Repository Structure

- **`manuscript/`**: Complete 71-page formatted academic manuscript (`.docx`) with 15 tables, 600-DPI figures, and 81 IEEE references.
- **`diagrams/`**: 34 high-resolution 600 DPI diagrams (`.png`) and editable multi-page Draw.io source (`all_diagrams.drawio`).
- **`source_code/`**:
  - `benchmark_pipeline.py`: Main reproducible benchmark pipeline reproducing exact reported metrics.
  - `interactive_demo.py`: Live terminal event stream compliance simulation.
  - `generate_all_architectural_figures.py`: 600 DPI diagram synthesizer.
  - `requirements.txt`: Python package manifest.
- **`datasets/`**:
  - `iot_privacy_compliance_dataset.csv`: Full synthetic 6,000 events dataset.
  - `train_set.csv` & `test_set.csv`: Stratified 75/25 train and test partitions.
  - `DATASET_CARD.md`: Feature definitions, provenance, and Data Availability Statement.
- **`execution_videos/`**: Video demonstration narration screenplay and Windows recording guide.
- **`results/`**: Benchmark metrics JSON, prediction outputs, and feature importance rankings.

---

## 🚀 Quickstart & Reproduction

```bash
# 1. Install dependencies
pip install -r source_code/requirements.txt

# 2. Run the benchmark pipeline
cd source_code
python benchmark_pipeline.py

# 3. Run the live interactive simulation
python interactive_demo.py
```

---

## 📜 Ethical & Data Availability Statement

All data analyzed during this study are synthetic and provided in the `datasets/` folder. No real patient data, personal telemetry, or proprietary corporate logs were used.
>>>>>>> 5620a4a (Initial commit: AI-Driven Privacy Compliance in Heterogeneous IoT Environments complete deliverables)
