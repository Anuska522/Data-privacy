# Execution Video Walkthrough Screenplay

**Course:** BCSE318L Data Privacy  
**Project:** AI-Driven Privacy Compliance in Heterogeneous IoT Environments  
**Author / Presenter:** Anuska Saha (Registration No: 23BCE0167)  
**Team ID:** 26FSDPYCPMID1029  
**Faculty / Guide:** Dr. M Rajasekhara Babu, SCOPE, VIT  
**Target Video Duration:** 5 to 7 Minutes  

---

## Video Recording Plan & Scene Breakdown

### Scene 1: Introduction & Title Slide (0:00 – 1:00)
- **On Screen:** Title page of your case-study report (`AI_Driven_Privacy_Compliance_in_Heterogeneous_IoT_Environments.docx` or presentation slide).
- **Narration:**
  > *"Good day, respected Professor and evaluators. My name is Anuska Saha, registration number 23BCE0167, Team ID 26FSDPYCPMID1029. Today I am presenting my case-study research and practical implementation on 'AI-Driven Privacy Compliance in Heterogeneous IoT Environments' for BCSE318L Data Privacy under the guidance of Dr. M Rajasekhara Babu.*
  > 
  > *Heterogeneous IoT devices—ranging from healthcare wearables to smart-city cameras and industrial sensors—generate massive streams of contextual data. Traditional static compliance checklists fail to scale. My research introduces a layered, six-plane compliance architecture combining deterministic policy rules, local edge minimization, explainable AI risk scoring, and tamper-evident audit trails, mapped to the GDPR and India’s DPDP Act, 2023 with its 2025 Rules."*

---

### Scene 2: Architectural Framework & 6 Logical Planes (1:00 – 2:15)
- **On Screen:** Open `diagrams/Fig 06 AI-Driven Privacy Compliance Architecture for Heterogeneous IoT Environments.png`.
- **Narration:**
  > *"As shown in Figure 6 of my manuscript, the proposed framework is organized into six distinct planes:
  > 1. The Device & Sensor Plane: for authenticated hardware onboarding and attestation.
  > 2. The Acquisition Plane: verifying schema integrity and attaching sensitivity tags.
  > 3. The Edge Governance Plane: enforcing local data minimization and privacy filtering before sensitive data leaves local gateways.
  > 4. The Compliance & AI Risk Plane: where deterministic rules handle hard stops like missing consent, while an AI risk model prioritizes anomalous access patterns.
  > 5. The Evidence Plane: maintaining tamper-evident audit logs with cryptographic hash pointers.
  > 6. The Oversight Plane: ensuring human-in-the-loop accountability for ambiguous edge cases."*

---

### Scene 3: Reproducible Benchmark Execution (2:15 – 3:45)
- **On Screen:** Open VS Code / Terminal in `source_code/`.
- **Command Run:**
  ```bash
  python benchmark_pipeline.py
  ```
- **Narration:**
  > *"Now, let us examine the experimental pipeline. As required by the project rubric, I have developed a reproducible software benchmark on a dataset of 6,000 synthetic IoT events across six domains: Healthcare, Smart Cities, Manufacturing, Energy, Agriculture, and Transport.
  > 
  > Running `python benchmark_pipeline.py` executes a stratified 75/25 train-test split with fixed seed 42. It evaluates three distinct detection approaches on the 1,500 held-out test events:
  > - The Checklist baseline achieves 66.40% accuracy and 71.37% precision, but its recall is limited to 29.02% because manual rules miss complex patterns.
  > - The supervised Random Forest classifier achieves 68.73% accuracy and 61.48% recall with an ROC-AUC of 0.7423.
  > - The Hybrid Rules + AI approach achieves the highest recall at 79.51% and an F1 score of 0.6441.
  > 
  > This highlights the key engineering trade-off: the hybrid approach captures substantially more potential violations at the cost of a controlled increase in false alerts, which are then routed to human triage."*

---

### Scene 4: Inspection of Generated Publication Diagrams (3:45 – 4:45)
- **On Screen:** Open the `diagrams/` folder showing `Fig 23`, `Fig 24`, `Fig 26`, and `all_diagrams.drawio`.
- **Narration:**
  > *"The pipeline automatically synthesizes all 34 figures in high-resolution 600 DPI, strictly adhering to the submission guidelines:
  > - Figure 23 illustrates the metric trajectory across Accuracy, Precision, Recall, and F1.
  > - Figure 24 demonstrates the control indicators in the synthetic corpus: 78.7% encryption, 67.2% data minimization, and 82.0% valid consent.
  > - Figure 26 presents the radar chart comparing the multi-dimensional profiles of each algorithm.
  > 
  > Furthermore, an editable multi-page Draw.io source file, `all_diagrams.drawio`, is provided so that all architectural diagrams remain inspectable and fully editable."*

---

### Scene 5: Live Streaming Compliance Simulation (4:45 – 6:00)
- **On Screen:** Run the interactive streaming simulation:
  ```bash
  python interactive_demo.py
  ```
- **Narration:**
  > *"To demonstrate how this operates in a live deployment, I will now run `python interactive_demo.py`.
  > 
  > Here we observe real-time IoT events being ingested:
  > - Event 101 from a healthcare pulse monitor: valid consent and encryption are verified; local edge minimization is applied; and the event is safely permitted.
  > - Event 102 from a smart-city camera: the purpose is tagged as unapproved third-party analytics with an expired retention period. The deterministic policy engine immediately triggers Rule R-02 and Rule R-04, blocking the transfer and writing a tamper-evident SHA-256 hash to the audit log.
  > - Event 104 from an energy smart meter: all hard rules pass, but the Random Forest model detects an elevated access anomaly score of 0.52. Because this exceeds our 0.38 hybrid threshold, the event is held for human reviewer triage rather than blindly blocked.
  > 
  > This confirms how deterministic rules and AI triage complement each other without allowing AI to silently bypass mandatory legal duties."*

---

### Scene 6: Conclusion & Deliverables Summary (6:00 – 6:30)
- **On Screen:** Show the project folder containing `datasets/`, `source_code/`, `diagrams/`, `execution_videos/`, and `manuscript/`.
- **Narration:**
  > *"In conclusion, all deliverables specified by the course rubric have been produced: the complete manuscript, the 6,000-event synthetic dataset and dataset card, the full reproducible Python source code ready for GitHub, 34 600-DPI diagrams with editable Draw.io sources, and this recorded execution video.
  > 
  > Thank you very much for your time and guidance."*
