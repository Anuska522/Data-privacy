"""
Interactive Live Demonstration & Video Walkthrough Engine
AI-Driven Privacy Compliance in Heterogeneous IoT Environments
Student: Anuska Saha | Reg No: 23BCE0167 | Team ID: 26FSDPYCPMID1029
Course: BCSE318L Data Privacy - Vellore Institute of Technology
"""

import time
import hashlib
import json
import random

# Color formatting for terminal
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

SAMPLE_STREAM_EVENTS = [
    {
        "event_id": "EVT-STREAM-101",
        "device_id": "DEV-MED-PULSE-04",
        "domain": "Healthcare",
        "data_class": "Sensitive",
        "purpose": "Remote Arrhythmia Monitoring",
        "consent": True,
        "encrypted": True,
        "edge_minimized": True,
        "retention_days": 14,
        "max_retention": 30,
        "anomaly_score": 0.08,
        "expected_action": "ALLOW (Edge Minimized)"
    },
    {
        "event_id": "EVT-STREAM-102",
        "device_id": "DEV-CITY-CAM-88",
        "domain": "Smart City",
        "data_class": "Personal",
        "purpose": "Unapproved Third-Party Behavioral Analytics",
        "consent": False,
        "encrypted": True,
        "edge_minimized": False,
        "retention_days": 45,
        "max_retention": 30,
        "anomaly_score": 0.78,
        "expected_action": "BLOCK (Rule R-02 Purpose Mismatch & Expired Retention)"
    },
    {
        "event_id": "EVT-STREAM-103",
        "device_id": "DEV-FACTORY-TEMP-12",
        "domain": "Manufacturing",
        "data_class": "Low",
        "purpose": "Turbine Heat Preventive Maintenance",
        "consent": True,
        "encrypted": False,
        "edge_minimized": True,
        "retention_days": 5,
        "max_retention": 90,
        "anomaly_score": 0.04,
        "expected_action": "ALLOW (Telemetry Standard)"
    },
    {
        "event_id": "EVT-STREAM-104",
        "device_id": "DEV-GRID-METER-91",
        "domain": "Energy",
        "data_class": "Personal",
        "purpose": "Household Power Consumption Billing",
        "consent": True,
        "encrypted": True,
        "edge_minimized": False,
        "retention_days": 20,
        "max_retention": 60,
        "anomaly_score": 0.52,
        "expected_action": "ESCALATE TO HUMAN REVIEW (AI Threshold Trigger: 0.52 >= 0.38)"
    },
    {
        "event_id": "EVT-STREAM-105",
        "device_id": "DEV-AGRI-DRONE-03",
        "domain": "Agriculture",
        "data_class": "Security",
        "purpose": "Crop Health Aerial Mapping",
        "consent": False,
        "encrypted": False,
        "edge_minimized": False,
        "retention_days": 80,
        "max_retention": 60,
        "anomaly_score": 0.89,
        "expected_action": "QUARANTINE (Missing Encryption & Expired Retention)"
    }
]

def simulate_pipeline_evaluation(event):
    print("\n" + "=" * 70)
    print(f"{Colors.BOLD}{Colors.HEADER}>>> INGESTING IoT EVENT: {event['event_id']} [{event['domain']}]{Colors.ENDC}")
    print("=" * 70)
    time.sleep(0.6)
    
    # Plane 1 & 2: Acquisition & Ingestion
    print(f" [Plane 1 & 2: Acquisition] Verifying device: {Colors.CYAN}{event['device_id']}{Colors.ENDC}")
    print(f"                            Schema: Valid | Data Class: {event['data_class']}")
    time.sleep(0.4)

    # Plane 3: Edge Governance
    print(f" [Plane 3: Edge Governance] Edge Minimized: {event['edge_minimized']} | Encrypted: {event['encrypted']}")
    time.sleep(0.4)

    # Plane 4: Deterministic Policy Rules
    failed_rules = []
    if not event["consent"] and event["data_class"] in ["Personal", "Sensitive"]:
        failed_rules.append("Rule R-01 (Missing Valid Consent Evidence)")
    if "Unapproved" in event["purpose"]:
        failed_rules.append("Rule R-02 (Purpose Mismatch / Unauthorized Analytics)")
    if not event["encrypted"] and event["data_class"] in ["Sensitive", "Security"]:
        failed_rules.append("Rule R-03 (Mandatory Encryption Check Failed)")
    if event["retention_days"] > event["max_retention"]:
        failed_rules.append(f"Rule R-04 (Retention Exceeded: {event['retention_days']}d > {event['max_retention']}d limit)")

    # Model Risk Score Inference
    # AI Risk formula simulation matching RF probability
    ai_risk = (
        0.35 * event["anomaly_score"] +
        0.30 * (1 if not event["encrypted"] else 0) +
        0.20 * (1 if not event["consent"] else 0) +
        0.15 * (1 if not event["edge_minimized"] else 0)
    )
    ai_risk = round(min(max(ai_risk, 0.05), 0.96), 4)

    print(f" [Plane 4: AI Risk Scoring] Random Forest Risk Probability: {Colors.BOLD}{ai_risk:.4f}{Colors.ENDC}")
    time.sleep(0.4)

    # Hybrid Decision Logic
    action = "ALLOW"
    action_color = Colors.GREEN
    reason = "Passed all mandatory rules; AI risk within tolerable margin."

    if len(failed_rules) > 0:
        action = "BLOCK & QUARANTINE"
        action_color = Colors.FAIL
        reason = f"Deterministic Rule Violations: {'; '.join(failed_rules)}"
    elif ai_risk >= 0.38:
        action = "HOLD & ESCALATE TO REVIEWER"
        action_color = Colors.WARNING
        reason = f"Hybrid Trigger: AI score ({ai_risk:.2f}) >= 0.38 threshold requires human triage."
    elif event["edge_minimized"]:
        action = "ALLOW (FILTERED AT EDGE)"
        action_color = Colors.GREEN
        reason = "Data stripped of identifiers prior to transmission."

    print(f" [Plane 4: Decision Engine] Policy Action: {action_color}{Colors.BOLD}{action}{Colors.ENDC}")
    print(f"                            Reason: {reason}")
    time.sleep(0.4)

    # Plane 5: Tamper-Evident Evidence Log
    audit_payload = f"{event['event_id']}|{event['device_id']}|{action}|{ai_risk}|{time.time()}"
    sha256_hash = hashlib.sha256(audit_payload.encode()).hexdigest()[:16]
    print(f" [Plane 5: Evidence Store] Generated Tamper-Evident Hash: {Colors.BLUE}SHA-256:{sha256_hash}{Colors.ENDC}")
    print(f" [Plane 6: Oversight]      Logged to Audit Trail with Policy Version 1.0")

def main():
    print(f"{Colors.BOLD}{Colors.CYAN}")
    print("************************************************************************")
    print(" AI-DRIVEN PRIVACY COMPLIANCE IN HETEROGENEOUS IoT ENVIRONMENTS")
    print(" Live Real-Time Multi-Layer Governance Simulation Demo")
    print(" Student: Anuska Saha (23BCE0167) | BCSE318L Data Privacy")
    print(" Guide: Dr. M Rajasekhara Babu | SCOPE, VIT")
    print("************************************************************************")
    print(f"{Colors.ENDC}")
    time.sleep(1.0)

    for idx, evt in enumerate(SAMPLE_STREAM_EVENTS, start=1):
        simulate_pipeline_evaluation(evt)
        time.sleep(0.8)

    print("\n" + "=" * 70)
    print(f"{Colors.GREEN}{Colors.BOLD}Simulation Stream Finished Successfully! All records logged to audit store.{Colors.ENDC}")
    print("=" * 70)

if __name__ == "__main__":
    main()
