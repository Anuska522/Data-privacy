# Dataset Card: Synthetic IoT Privacy Compliance Dataset (N=6,000)

**Project Title:** AI-Driven Privacy Compliance in Heterogeneous IoT Environments  
**Course:** BCSE318L Data Privacy  
**Student Name:** Anuska Saha  
**Registration Number:** 23BCE0167  
**Team ID:** 26FSDPYCPMID1029  
**Faculty / Guide:** Dr. M Rajasekhara Babu, School of Computer Science and Engineering (SCOPE), VIT  

---

## 1. Dataset Overview

This dataset contains **6,000 synthetic IoT event records** engineered specifically to benchmark privacy compliance verification, edge governance, and AI-assisted risk detection pipelines across heterogeneous IoT ecosystems.

- **Total Records:** 6,000 events
- **Format:** Comma-Separated Values (`.csv`)
- **Random Seed:** 42 (Fully deterministic and reproducible)
- **Train/Test Split:** Stratified 75% Training (4,500 records) and 25% Held-out Testing (1,500 records)
- **Violation Prevalence:** 40.67% (2,440 positive violation events across the full corpus; exactly 610 positive violation events in the 1,500 held-out test set)

---

## 2. Sectoral Representation

Events are stratified across six major IoT deployment domains:
1. **Healthcare IoT (20%):** Medical wearables, bedside monitors, telemetry devices.
2. **Smart Cities (20%):** Traffic cameras, air-quality sensors, smart lighting, public transport.
3. **Manufacturing (18%):** Industrial robotics, machine vibration sensors, worker activity monitors.
4. **Energy & Utilities (16%):** Smart grid meters, power distribution monitors, substation telemetry.
5. **Agriculture (14%):** Soil moisture sensors, automated drones, irrigation controllers.
6. **Connected Transport (12%):** Fleet trackers, vehicle telematics, road-side infrastructure.

---

## 3. Schema & Feature Definitions

| Field Name | Type | Description | Values / Range |
| :--- | :--- | :--- | :--- |
| `event_id` | String | Unique trace identifier for event lifecycle | `EVT-00001` to `EVT-06000` |
| `domain` | Categorical | Target IoT domain | Healthcare, Smart City, Manufacturing, Energy, Agriculture, Transport |
| `data_class` | Categorical | Data classification category | Low, Personal, Sensitive, Security, Derived |
| `sensitivity_num` | Float | Numerical sensitivity score derived from data class | `0.1` (Low), `0.45` (Personal), `0.5` (Derived), `0.6` (Security), `0.85` (Sensitive) |
| `has_consent` | Binary | Valid consent or legal authority token present | `1` (Present, ~82.0%), `0` (Missing/Withdrawn) |
| `is_encrypted` | Binary | Cryptographic transport/at-rest encryption applied | `1` (Encrypted, ~78.7%), `0` (Plaintext) |
| `is_minimized` | Binary | Edge data filtering / field stripping performed | `1` (Minimized, ~67.2%), `0` (Raw payload) |
| `edge_processed` | Binary | Processing executed locally at edge gateway | `1` (Edge, ~51.2%), `0` (Direct cloud export) |
| `metadata_completeness`| Float | Proportion of required envelope metadata fields present | `[0.0, 1.0]` (Mean ~0.898) |
| `device_security_score`| Float | Device posture / firmware integrity / attestation rating | `[0.0, 1.0]` (Mean ~0.725) |
| `purpose_matched` | Binary | Declared processing purpose matches registered policy | `1` (Matched, ~82.0%), `0` (Purpose drift) |
| `retention_valid` | Binary | Event age is within authorized retention duration | `1` (Valid, ~88.0%), `0` (Expired) |
| `cross_border` | Binary | Data transfer traverses jurisdictional boundary | `1` (Cross-border, ~28.0%), `0` (Domestic) |
| `access_anomaly_score` | Float | Outlier score based on historic access baseline | `[0.0, 1.0]` (Beta distributed) |
| `data_volume_kb` | Float | Size of payload in Kilobytes | `[5.0, 1500.0+]` KB |
| `violation_label` | Binary | Ground-truth privacy non-compliance label | `1` (Violation candidate), `0` (Compliant) |

---

## 4. Ethical, Privacy, and Data Availability Statement

### Ethical Consideration & Patient Privacy
- **Zero Real-World PII:** No actual patient records, medical sensor traces, personal citizen telemetry, employee logs, or proprietary network captures are included.
- **De-identification Boundary:** All device identifiers, domain tags, and timestamps are generated synthetically by `source_code/benchmark_pipeline.py`.
- **Compliance with Institutional Guidelines:** This research complies with the privacy guidelines of VIT, the European Union GDPR (2016/679), and India’s Digital Personal Data Protection (DPDP) Act, 2023 along with the notified DPDP Rules, 2025.

### Official Data Availability Statement
> *"All data generated or analysed during this study are included in this published article [and its supplementary information files: `iot_privacy_compliance_dataset.csv`, `train_set.csv`, and `test_set.csv` in the `datasets/` repository folder]. The benchmark dataset is synthetic and fully reproducible via the provided Python scripts."*
