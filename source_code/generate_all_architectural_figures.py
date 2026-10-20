"""
High-Resolution 600 DPI Diagram Generator for all 34 Figures
Course: BCSE318L Data Privacy
Author: Anuska Saha (Reg No: 23BCE0167)
"""

import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIAGRAMS_DIR = os.path.join(BASE_DIR, "diagrams")
os.makedirs(DIAGRAMS_DIR, exist_ok=True)

def create_flow_diagram(filename, title, boxes, arrows=None, figsize=(8, 4.5)):
    """
    Renders clean, modern, publication-grade architectural diagrams at 600 DPI.
    boxes: list of dicts with 'text', 'xy' (center x,y), 'w', 'h', 'color', 'text_color'
    arrows: list of tuples ((x1,y1), (x2,y2), 'optional label')
    """
    fig, ax = plt.subplots(figsize=figsize, dpi=600)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")

    # Title banner
    ax.text(5.0, 5.55, title, ha="center", va="center", fontsize=11, fontweight="bold", color="#1f2937")

    # Render boxes
    for b in boxes:
        x, y = b['xy']
        w, h = b.get('w', 2.2), b.get('h', 1.0)
        bg = b.get('color', '#e0f2fe')
        ec = b.get('border', '#0284c7')
        tc = b.get('text_color', '#0f172a')
        fs = b.get('fontsize', 9)

        rect = patches.FancyBboxPatch(
            (x - w/2, y - h/2), w, h,
            boxstyle="round,pad=0.2,rounding_size=0.15",
            facecolor=bg, edgecolor=ec, linewidth=1.5
        )
        ax.add_patch(rect)
        ax.text(x, y, b['text'], ha="center", va="center", fontsize=fs, fontweight="bold", color=tc, wrap=True)

    # Render arrows
    if arrows:
        for a in arrows:
            p1, p2 = a[0], a[1]
            lbl = a[2] if len(a) > 2 else ""
            ax.annotate(
                lbl, xy=p2, xytext=p1,
                arrowprops=dict(facecolor="#475569", edgecolor="#475569", arrowstyle="->", lw=1.5),
                ha="center", va="bottom", fontsize=8, color="#334155"
            )

    fig.tight_layout()
    out_path = os.path.join(DIAGRAMS_DIR, filename)
    fig.savefig(out_path, dpi=600, bbox_inches="tight")
    plt.close(fig)


def generate_all_figures():
    # -----------------------------------------------------------------
    # Fig 01: Evolution of IoT Ecosystems and Compliance Challenges
    # -----------------------------------------------------------------
    create_flow_diagram(
        "Fig 01 Evolution of IoT Ecosystems and Compliance Challenges.png",
        "Evolution of IoT Ecosystems and Governance Complexity",
        [
            {'text': "Standalone\nSensing Nodes\n(Local Storage)", 'xy': (1.6, 2.7), 'w': 2.0, 'h': 1.4, 'color': '#f1f5f9', 'border': '#94a3b8'},
            {'text': "Connected IoT\nGateways\n(Ad-hoc Rules)", 'xy': (5.0, 2.7), 'w': 2.2, 'h': 1.4, 'color': '#e0e7ff', 'border': '#6366f1'},
            {'text': "Heterogeneous Edge-Cloud\nAI-Governed Ecosystem\n(Continuous Compliance)", 'xy': (8.4, 2.7), 'w': 2.5, 'h': 1.5, 'color': '#dcfce7', 'border': '#22c55e'}
        ],
        [
            ((2.7, 2.7), (3.8, 2.7), "Connectivity Expansion"),
            ((6.2, 2.7), (7.0, 2.7), "Regulatory Evolution (DPDP/GDPR)")
        ]
    )

    # -----------------------------------------------------------------
    # Fig 02: AI-Driven Privacy Governance Landscape
    # -----------------------------------------------------------------
    create_flow_diagram(
        "Fig 02 AI-Driven Privacy Governance Landscape.png",
        "AI-Driven Privacy Governance Landscape",
        [
            {'text': "IoT Event Stream\n(Sensors/Actuators)", 'xy': (2.0, 3.8), 'w': 2.2, 'h': 1.1, 'color': '#f0fdf4', 'border': '#16a34a'},
            {'text': "Context & Metadata\n(Purpose/Consent)", 'xy': (5.0, 3.8), 'w': 2.2, 'h': 1.1, 'color': '#eff6ff', 'border': '#2563eb'},
            {'text': "AI Risk Analysis\n(Anomaly/Scoring)", 'xy': (8.0, 3.8), 'w': 2.2, 'h': 1.1, 'color': '#fef3c7', 'border': '#d97706'},
            {'text': "Policy Engine\n(Deterministic Rules)", 'xy': (2.5, 1.8), 'w': 2.4, 'h': 1.1, 'color': '#fae8ff', 'border': '#a855f7'},
            {'text': "Human Oversight\n(Auditor / Triage)", 'xy': (5.5, 1.8), 'w': 2.2, 'h': 1.1, 'color': '#fee2e2', 'border': '#dc2626'},
            {'text': "Audit Evidence\n(Immutable Log)", 'xy': (8.2, 1.8), 'w': 2.0, 'h': 1.1, 'color': '#f1f5f9', 'border': '#64748b'}
        ],
        [
            ((3.2, 3.8), (3.8, 3.8)),
            ((6.2, 3.8), (6.8, 3.8)),
            ((8.0, 3.2), (8.0, 2.4)),
            ((5.5, 3.2), (5.5, 2.4)),
            ((3.8, 1.8), (4.3, 1.8)),
            ((6.7, 1.8), (7.1, 1.8))
        ]
    )

    # -----------------------------------------------------------------
    # Fig 03: IoT Privacy Compliance Challenge Landscape
    # -----------------------------------------------------------------
    create_flow_diagram(
        "Fig 03 IoT Privacy Compliance Challenge Landscape.png",
        "Key Challenges in Heterogeneous IoT Privacy Compliance",
        [
            {'text': "Device Diversity\n(Firmware/Sensors)", 'xy': (2.0, 4.0), 'w': 2.3, 'h': 1.1, 'color': '#fee2e2', 'border': '#ef4444'},
            {'text': "Fragmented Policies\n(Multiple Vendors)", 'xy': (5.0, 4.0), 'w': 2.3, 'h': 1.1, 'color': '#fef3c7', 'border': '#f59e0b'},
            {'text': "Sensitive & Contextual\nTelemetry Flows", 'xy': (8.0, 4.0), 'w': 2.3, 'h': 1.1, 'color': '#fee2e2', 'border': '#ef4444'},
            {'text': "Cross-Border Flows\n& Jurisdiction Shift", 'xy': (2.5, 2.0), 'w': 2.4, 'h': 1.1, 'color': '#e0e7ff', 'border': '#6366f1'},
            {'text': "Limited Edge Resources\n(Compute/Battery)", 'xy': (5.5, 2.0), 'w': 2.3, 'h': 1.1, 'color': '#f1f5f9', 'border': '#64748b'},
            {'text': "Weak Auditability\n& Black-Box Risk", 'xy': (8.2, 2.0), 'w': 2.2, 'h': 1.1, 'color': '#fef3c7', 'border': '#f59e0b'}
        ]
    )

    # -----------------------------------------------------------------
    # Fig 04: Literature Taxonomy Framework
    # -----------------------------------------------------------------
    create_flow_diagram(
        "Fig 04 Literature Taxonomy Framework.png",
        "Literature Taxonomy: Converging Pillars of IoT Privacy",
        [
            {'text': "Privacy Engineering\n(Minimization/PETs)", 'xy': (2.0, 3.8), 'w': 2.4, 'h': 1.1, 'color': '#e0f2fe', 'border': '#0284c7'},
            {'text': "Federated Learning\n(Distributed Training)", 'xy': (5.0, 3.8), 'w': 2.4, 'h': 1.1, 'color': '#f3e8ff', 'border': '#9333ea'},
            {'text': "Differential Privacy\n(Formal ε-bounds)", 'xy': (8.0, 3.8), 'w': 2.4, 'h': 1.1, 'color': '#fef9c3', 'border': '#ca8a04'},
            {'text': "Explainable AI (XAI)\n(Feature Attribution)", 'xy': (2.5, 2.0), 'w': 2.4, 'h': 1.1, 'color': '#dcfce7', 'border': '#16a34a'},
            {'text': "RegTech Governance\n(GDPR / DPDP Rules)", 'xy': (5.5, 2.0), 'w': 2.4, 'h': 1.1, 'color': '#fee2e2', 'border': '#dc2626'},
            {'text': "Edge & Gateway Security\n(NIST Baseline)", 'xy': (8.2, 2.0), 'w': 2.2, 'h': 1.1, 'color': '#f1f5f9', 'border': '#475569'}
        ]
    )

    # -----------------------------------------------------------------
    # Fig 05: Requirements Engineering Framework
    # -----------------------------------------------------------------
    create_flow_diagram(
        "Fig 05 Requirements Engineering Framework.png",
        "Requirements Engineering Sequence (Traceability Pipeline)",
        [
            {'text': "Stakeholder & Legal\nDrivers (GDPR/DPDP)", 'xy': (1.8, 3.0), 'w': 2.2, 'h': 1.3, 'color': '#eff6ff', 'border': '#3b82f6'},
            {'text': "Functional & NF\nRequirements (F1-NF4)", 'xy': (4.4, 3.0), 'w': 2.2, 'h': 1.3, 'color': '#f0fdf4', 'border': '#22c55e'},
            {'text': "Traceable Controls\n(Deterministic Rules)", 'xy': (7.0, 3.0), 'w': 2.2, 'h': 1.3, 'color': '#fef3c7', 'border': '#f59e0b'},
            {'text': "Verification & Test\n(Positive/Negative)", 'xy': (9.2, 3.0), 'w': 1.5, 'h': 1.3, 'color': '#fae8ff', 'border': '#a855f7'}
        ],
        [
            ((2.9, 3.0), (3.3, 3.0)),
            ((5.5, 3.0), (5.9, 3.0)),
            ((8.1, 3.0), (8.4, 3.0))
        ]
    )

    # -----------------------------------------------------------------
    # Fig 06: AI-Driven Privacy Compliance Architecture (6 Planes)
    # -----------------------------------------------------------------
    create_flow_diagram(
        "Fig 06 AI-Driven Privacy Compliance Architecture for Heterogeneous IoT Environments.png",
        "Core Reference Architecture (Six Logical Planes)",
        [
            {'text': "[1] Device & Sensor Plane\nRegistration, Identity, Local Telemetry", 'xy': (5.0, 4.8), 'w': 6.5, 'h': 0.8, 'color': '#f1f5f9', 'border': '#64748b'},
            {'text': "[2] Acquisition Plane: Schema Validation, Context Attaching", 'xy': (5.0, 3.9), 'w': 6.5, 'h': 0.7, 'color': '#e0f2fe', 'border': '#0284c7'},
            {'text': "[3] Edge Governance: Minimization, Local Hard Rules, Cache", 'xy': (5.0, 3.0), 'w': 6.5, 'h': 0.7, 'color': '#dcfce7', 'border': '#16a34a'},
            {'text': "[4] Compliance & AI Risk Plane: Rules Engine, RF Risk Model", 'xy': (5.0, 2.1), 'w': 6.5, 'h': 0.7, 'color': '#fef3c7', 'border': '#d97706'},
            {'text': "[5] Evidence Plane: Tamper-Evident Audit Records & Lineage", 'xy': (5.0, 1.2), 'w': 6.5, 'h': 0.7, 'color': '#f3e8ff', 'border': '#9333ea'},
            {'text': "[6] Oversight Plane: Human Reviewers, Incident Response, DPO", 'xy': (5.0, 0.4), 'w': 6.5, 'h': 0.6, 'color': '#fee2e2', 'border': '#dc2626'}
        ],
        [
            ((5.0, 4.4), (5.0, 4.25)),
            ((5.0, 3.55), (5.0, 3.35)),
            ((5.0, 2.65), (5.0, 2.45)),
            ((5.0, 1.75), (5.0, 1.55)),
            ((5.0, 0.85), (5.0, 0.7))
        ],
        figsize=(8, 5.5)
    )

    # -----------------------------------------------------------------
    # Fig 07: Multi-Layer Compliance Framework
    # -----------------------------------------------------------------
    create_flow_diagram(
        "Fig 07 Multi-Layer Compliance Framework.png",
        "Multi-Layer Compliance Evaluation Framework",
        [
            {'text': "Layer 1: Acquisition\n(Schema & Auth)", 'xy': (1.8, 3.8), 'w': 2.2, 'h': 1.1, 'color': '#e0f2fe', 'border': '#0284c7'},
            {'text': "Layer 2: Classification\n(Sensitivity & Purpose)", 'xy': (5.0, 3.8), 'w': 2.4, 'h': 1.1, 'color': '#eff6ff', 'border': '#2563eb'},
            {'text': "Layer 3: Edge Controls\n(Local Minimization)", 'xy': (8.2, 3.8), 'w': 2.2, 'h': 1.1, 'color': '#dcfce7', 'border': '#16a34a'},
            {'text': "Layer 4: AI Risk Scoring\n(Anomaly Prioritization)", 'xy': (1.8, 1.8), 'w': 2.2, 'h': 1.1, 'color': '#fef3c7', 'border': '#d97706'},
            {'text': "Layer 5: Policy Enforcement\n(Action: Allow/Hold/Block)", 'xy': (5.0, 1.8), 'w': 2.4, 'h': 1.1, 'color': '#fae8ff', 'border': '#a855f7'},
            {'text': "Layer 6: Explainability & Audit\n(Reason Code + Tamper-Log)", 'xy': (8.2, 1.8), 'w': 2.4, 'h': 1.1, 'color': '#f1f5f9', 'border': '#475569'}
        ],
        [
            ((2.9, 3.8), (3.8, 3.8)),
            ((6.2, 3.8), (7.1, 3.8)),
            ((8.2, 3.25), (8.2, 2.35)),
            ((7.0, 1.8), (6.2, 1.8)),
            ((3.8, 1.8), (2.9, 1.8))
        ]
    )

    # -----------------------------------------------------------------
    # Fig 08: IoT Data Acquisition Framework
    # -----------------------------------------------------------------
    create_flow_diagram(
        "Fig 08 IoT Data Acquisition Framework.png",
        "IoT Data Ingestion, Normalization, and Verification",
        [
            {'text': "Device Registry\n(Known Profile)", 'xy': (2.0, 3.8), 'w': 2.2, 'h': 1.1, 'color': '#f1f5f9', 'border': '#64748b'},
            {'text': "Authenticated Ingest\n(Mutual TLS / Token)", 'xy': (5.0, 3.8), 'w': 2.4, 'h': 1.1, 'color': '#e0f2fe', 'border': '#0284c7'},
            {'text': "Schema Validator\n(Malformed Reject)", 'xy': (8.0, 3.8), 'w': 2.2, 'h': 1.1, 'color': '#fee2e2', 'border': '#ef4444'},
            {'text': "Sensitivity Tagging\n(Low/Personal/Sensitive)", 'xy': (3.5, 1.8), 'w': 2.6, 'h': 1.1, 'color': '#fef3c7', 'border': '#d97706'},
            {'text': "Metadata Store\n(Trace Envelope attached)", 'xy': (6.8, 1.8), 'w': 2.6, 'h': 1.1, 'color': '#dcfce7', 'border': '#16a34a'}
        ],
        [
            ((3.1, 3.8), (3.8, 3.8)),
            ((6.2, 3.8), (6.9, 3.8)),
            ((8.0, 3.25), (6.8, 2.35)),
            ((5.5, 1.8), (4.8, 1.8))
        ]
    )

    # -----------------------------------------------------------------
    # Fig 09: Edge Governance Architecture
    # -----------------------------------------------------------------
    create_flow_diagram(
        "Fig 09 Edge Governance Architecture.png",
        "Edge Intelligence and Local Governance Architecture",
        [
            {'text': "Raw Sensor Stream\n(High Frequency)", 'xy': (1.8, 3.0), 'w': 2.2, 'h': 1.3, 'color': '#f1f5f9', 'border': '#64748b'},
            {'text': "Edge Policy Cache\n(Signed Bundle + TTL)", 'xy': (4.5, 4.0), 'w': 2.3, 'h': 1.1, 'color': '#e0f2fe', 'border': '#0284c7'},
            {'text': "Local Enforcement\n(Minimization / Masking)", 'xy': (4.5, 2.0), 'w': 2.3, 'h': 1.1, 'color': '#dcfce7', 'border': '#16a34a'},
            {'text': "Cloud Governance Sync\n(Summaries & Audits)", 'xy': (7.8, 3.0), 'w': 2.3, 'h': 1.3, 'color': '#f3e8ff', 'border': '#9333ea'}
        ],
        [
            ((2.9, 3.4), (3.35, 3.8)),
            ((2.9, 2.6), (3.35, 2.2)),
            ((5.65, 3.8), (6.65, 3.3)),
            ((5.65, 2.2), (6.65, 2.7))
        ]
    )

    # -----------------------------------------------------------------
    # Fig 10: Edge Compliance Monitoring Workflow
    # -----------------------------------------------------------------
    create_flow_diagram(
        "Fig 10 Edge Compliance Monitoring Workflow.png",
        "Step-by-Step Edge Monitoring Workflow",
        [
            {'text': "1. Receive Event", 'xy': (1.5, 3.0), 'w': 1.7, 'h': 1.0, 'color': '#eff6ff', 'border': '#3b82f6'},
            {'text': "2. Validate Identity", 'xy': (3.4, 3.0), 'w': 1.7, 'h': 1.0, 'color': '#eff6ff', 'border': '#3b82f6'},
            {'text': "3. Check Consent", 'xy': (5.3, 3.0), 'w': 1.7, 'h': 1.0, 'color': '#eff6ff', 'border': '#3b82f6'},
            {'text': "4. Score Risk", 'xy': (7.2, 3.0), 'w': 1.6, 'h': 1.0, 'color': '#fef3c7', 'border': '#d97706'},
            {'text': "5. Action & Log", 'xy': (9.0, 3.0), 'w': 1.6, 'h': 1.0, 'color': '#dcfce7', 'border': '#16a34a'}
        ],
        [
            ((2.35, 3.0), (2.55, 3.0)),
            ((4.25, 3.0), (4.45, 3.0)),
            ((6.15, 3.0), (6.4, 3.0)),
            ((8.0, 3.0), (8.2, 3.0))
        ]
    )

    # -----------------------------------------------------------------
    # Fig 11: AI Privacy Risk Assessment Framework
    # -----------------------------------------------------------------
    create_flow_diagram(
        "Fig 11 AI Privacy Risk Assessment Framework.png",
        "Risk Assessment Component Interaction",
        [
            {'text': "Context Extraction\n(Sensitivity, Recipient)", 'xy': (2.0, 3.8), 'w': 2.4, 'h': 1.1, 'color': '#e0f2fe', 'border': '#0284c7'},
            {'text': "Threat & Exposure\n(Security State, Route)", 'xy': (5.0, 3.8), 'w': 2.4, 'h': 1.1, 'color': '#fee2e2', 'border': '#ef4444'},
            {'text': "Impact Estimator\n(Harm to Data Subject)", 'xy': (8.0, 3.8), 'w': 2.4, 'h': 1.1, 'color': '#fee2e2', 'border': '#dc2626'},
            {'text': "Likelihood Estimator\n(RF Risk Signal)", 'xy': (3.5, 1.8), 'w': 2.6, 'h': 1.1, 'color': '#fef3c7', 'border': '#d97706'},
            {'text': "Mitigation Choice\n(Allow/Hold/Block)", 'xy': (7.0, 1.8), 'w': 2.6, 'h': 1.1, 'color': '#dcfce7', 'border': '#16a34a'}
        ],
        [
            ((3.2, 3.8), (3.8, 3.8)),
            ((6.2, 3.8), (6.8, 3.8)),
            ((4.8, 1.8), (5.7, 1.8)),
            ((5.0, 3.25), (4.0, 2.35)),
            ((8.0, 3.25), (7.0, 2.35))
        ]
    )

    # -----------------------------------------------------------------
    # Fig 12: Risk Prediction Pipeline
    # -----------------------------------------------------------------
    create_flow_diagram(
        "Fig 12 Risk Prediction Pipeline.png",
        "Synthetic Data & Model Inference Pipeline",
        [
            {'text': "Synthetic IoT\nData Ingestion", 'xy': (1.8, 3.0), 'w': 2.0, 'h': 1.2, 'color': '#f1f5f9', 'border': '#64748b'},
            {'text': "Feature\nEngineering\n(12 Attributes)", 'xy': (4.2, 3.0), 'w': 2.0, 'h': 1.2, 'color': '#eff6ff', 'border': '#3b82f6'},
            {'text': "Model Inference\n(Random Forest\n240 Trees)", 'xy': (6.7, 3.0), 'w': 2.2, 'h': 1.2, 'color': '#fef3c7', 'border': '#d97706'},
            {'text': "Hybrid Policy\nEnforcement\n(Rules + Threshold)", 'xy': (9.1, 3.0), 'w': 1.6, 'h': 1.2, 'color': '#dcfce7', 'border': '#16a34a'}
        ],
        [
            ((2.8, 3.0), (3.2, 3.0)),
            ((5.2, 3.0), (5.6, 3.0)),
            ((7.8, 3.0), (8.3, 3.0))
        ]
    )

    # -----------------------------------------------------------------
    # Fig 13: Compliance Automation Workflow
    # -----------------------------------------------------------------
    create_flow_diagram(
        "Fig 13 Compliance Automation Workflow.png",
        "Automated Compliance Engine Decision Workflow",
        [
            {'text': "Policy Authoring\n(Legal mapping)", 'xy': (1.8, 3.8), 'w': 2.2, 'h': 1.1, 'color': '#f3e8ff', 'border': '#9333ea'},
            {'text': "Machine Rules\n(JSON Conditions)", 'xy': (5.0, 3.8), 'w': 2.4, 'h': 1.1, 'color': '#eff6ff', 'border': '#2563eb'},
            {'text': "Event Evaluation\n(Pre-execution check)", 'xy': (8.2, 3.8), 'w': 2.2, 'h': 1.1, 'color': '#fef3c7', 'border': '#d97706'},
            {'text': "Action Selection\n(Allow/Minimize/Block)", 'xy': (2.5, 1.8), 'w': 2.5, 'h': 1.1, 'color': '#dcfce7', 'border': '#16a34a'},
            {'text': "Audit Log\n(Tamper-proof trace)", 'xy': (5.5, 1.8), 'w': 2.2, 'h': 1.1, 'color': '#f1f5f9', 'border': '#64748b'},
            {'text': "Policy Feedback\n(Reviewer revisions)", 'xy': (8.2, 1.8), 'w': 2.2, 'h': 1.1, 'color': '#fee2e2', 'border': '#dc2626'}
        ],
        [
            ((2.9, 3.8), (3.8, 3.8)),
            ((6.2, 3.8), (7.1, 3.8)),
            ((8.2, 3.25), (8.2, 2.35)),
            ((7.1, 1.8), (6.6, 1.8)),
            ((4.4, 1.8), (3.75, 1.8))
        ]
    )

    # -----------------------------------------------------------------
    # Fig 14: Policy Enforcement Lifecycle
    # -----------------------------------------------------------------
    create_flow_diagram(
        "Fig 14 Policy Enforcement Lifecycle.png",
        "Continuous Policy Governance Lifecycle",
        [
            {'text': "1. Draft & Legal Map", 'xy': (2.0, 4.0), 'w': 2.2, 'h': 1.0, 'color': '#eff6ff', 'border': '#3b82f6'},
            {'text': "2. Unit & Stress Test", 'xy': (5.0, 4.0), 'w': 2.2, 'h': 1.0, 'color': '#eff6ff', 'border': '#3b82f6'},
            {'text': "3. Sign & Approve", 'xy': (8.0, 4.0), 'w': 2.2, 'h': 1.0, 'color': '#dcfce7', 'border': '#16a34a'},
            {'text': "4. Deploy to Edge Cache", 'xy': (8.0, 2.0), 'w': 2.4, 'h': 1.0, 'color': '#fef3c7', 'border': '#d97706'},
            {'text': "5. Real-Time Evaluation", 'xy': (5.0, 2.0), 'w': 2.4, 'h': 1.0, 'color': '#dcfce7', 'border': '#16a34a'},
            {'text': "6. Monitor, Audit & Retire", 'xy': (2.0, 2.0), 'w': 2.4, 'h': 1.0, 'color': '#fee2e2', 'border': '#dc2626'}
        ],
        [
            ((3.1, 4.0), (3.9, 4.0)),
            ((6.1, 4.0), (6.9, 4.0)),
            ((8.0, 3.5), (8.0, 2.5)),
            ((6.8, 2.0), (6.2, 2.0)),
            ((3.8, 2.0), (3.2, 2.0))
        ]
    )

    # -----------------------------------------------------------------
    # Fig 15: Privacy Protection Framework
    # -----------------------------------------------------------------
    create_flow_diagram(
        "Fig 15 Privacy Protection Framework.png",
        "Defense-in-Depth Privacy Preserving Controls",
        [
            {'text': "Data Minimization\n(Field Filtering)", 'xy': (2.0, 3.8), 'w': 2.4, 'h': 1.1, 'color': '#dcfce7', 'border': '#16a34a'},
            {'text': "Pseudonymization\n(Tokenization)", 'xy': (5.0, 3.8), 'w': 2.4, 'h': 1.1, 'color': '#e0f2fe', 'border': '#0284c7'},
            {'text': "Encryption\n(TLS / AES-256)", 'xy': (8.0, 3.8), 'w': 2.4, 'h': 1.1, 'color': '#fef3c7', 'border': '#d97706'},
            {'text': "Access Control\n(Least Privilege / RBAC)", 'xy': (2.5, 2.0), 'w': 2.5, 'h': 1.1, 'color': '#fae8ff', 'border': '#a855f7'},
            {'text': "Retention Limitation\n(Auto-Deletion)", 'xy': (5.5, 2.0), 'w': 2.4, 'h': 1.1, 'color': '#fee2e2', 'border': '#dc2626'},
            {'text': "Audit Sharing\n(Lineage Records)", 'xy': (8.2, 2.0), 'w': 2.2, 'h': 1.1, 'color': '#f1f5f9', 'border': '#64748b'}
        ]
    )

    # -----------------------------------------------------------------
    # Fig 16: Data Protection Lifecycle
    # -----------------------------------------------------------------
    create_flow_diagram(
        "Fig 16 Data Protection Lifecycle.png",
        "Full Telemetry Lifecycle from Collection to Disposal",
        [
            {'text': "1. Collect Lawfully\n(Notice & Consent)", 'xy': (1.8, 3.8), 'w': 2.2, 'h': 1.1, 'color': '#eff6ff', 'border': '#3b82f6'},
            {'text': "2. Classify Context\n(Sensitivity Tag)", 'xy': (5.0, 3.8), 'w': 2.2, 'h': 1.1, 'color': '#e0f2fe', 'border': '#0284c7'},
            {'text': "3. Process Locally\n(Edge Filter/Mask)", 'xy': (8.2, 3.8), 'w': 2.2, 'h': 1.1, 'color': '#dcfce7', 'border': '#16a34a'},
            {'text': "4. Store Securely\n(Encrypted at Rest)", 'xy': (8.2, 1.8), 'w': 2.2, 'h': 1.1, 'color': '#fef3c7', 'border': '#d97706'},
            {'text': "5. Share Minimally\n(Approved Receivers)", 'xy': (5.0, 1.8), 'w': 2.2, 'h': 1.1, 'color': '#fae8ff', 'border': '#a855f7'},
            {'text': "6. Delete or Retain\n(Certified Purge)", 'xy': (1.8, 1.8), 'w': 2.2, 'h': 1.1, 'color': '#fee2e2', 'border': '#dc2626'}
        ],
        [
            ((2.9, 3.8), (3.9, 3.8)),
            ((6.1, 3.8), (7.1, 3.8)),
            ((8.2, 3.25), (8.2, 2.35)),
            ((7.1, 1.8), (6.1, 1.8)),
            ((3.9, 1.8), (2.9, 1.8))
        ]
    )

    # -----------------------------------------------------------------
    # Fig 17: Explainable Compliance Framework
    # -----------------------------------------------------------------
    create_flow_diagram(
        "Fig 17 Explainable Compliance Framework.png",
        "Traceable Decision & Explanation Pipeline",
        [
            {'text': "Model Output\n(Raw Risk Probability)", 'xy': (2.0, 3.8), 'w': 2.4, 'h': 1.1, 'color': '#fef3c7', 'border': '#d97706'},
            {'text': "Reason Codes\n(Missing Consent, Retention)", 'xy': (5.0, 3.8), 'w': 2.4, 'h': 1.1, 'color': '#eff6ff', 'border': '#2563eb'},
            {'text': "Evidence Links\n(Event ID, Policy Ver)", 'xy': (8.0, 3.8), 'w': 2.4, 'h': 1.1, 'color': '#dcfce7', 'border': '#16a34a'},
            {'text': "Confidence Level\n& Uncertainty Flag", 'xy': (2.5, 1.8), 'w': 2.4, 'h': 1.1, 'color': '#fae8ff', 'border': '#a855f7'},
            {'text': "Reviewer Feedback\n(Approve/Override)", 'xy': (5.5, 1.8), 'w': 2.4, 'h': 1.1, 'color': '#fee2e2', 'border': '#dc2626'},
            {'text': "Model Governance\n(Audit Register)", 'xy': (8.2, 1.8), 'w': 2.2, 'h': 1.1, 'color': '#f1f5f9', 'border': '#64748b'}
        ]
    )

    # -----------------------------------------------------------------
    # Fig 18: Auditability and Transparency Dashboard
    # -----------------------------------------------------------------
    create_flow_diagram(
        "Fig 18 Auditability and Transparency Dashboard.png",
        "Auditability and Transparency Dashboard (User Interface Mock-up)",
        [
            {'text': "Current Risk Meter\n[High / Medium / Low]", 'xy': (2.0, 3.8), 'w': 2.5, 'h': 1.2, 'color': '#fee2e2', 'border': '#ef4444'},
            {'text': "Policy Decisions\n[Allowed: 964 | Flagged: 536]", 'xy': (5.0, 3.8), 'w': 2.8, 'h': 1.2, 'color': '#dcfce7', 'border': '#16a34a'},
            {'text': "Control Status\n[TLS: OK | Encrypt: OK]", 'xy': (8.0, 3.8), 'w': 2.5, 'h': 1.2, 'color': '#e0f2fe', 'border': '#0284c7'},
            {'text': "Data Access Log\n[Event Provenance & Hash]", 'xy': (2.0, 1.8), 'w': 2.5, 'h': 1.2, 'color': '#f1f5f9', 'border': '#64748b'},
            {'text': "Exceptions & Overrides\n[Authorized DPO Actions]", 'xy': (5.0, 1.8), 'w': 2.8, 'h': 1.2, 'color': '#fef3c7', 'border': '#f59e0b'},
            {'text': "Review Queue\n[Triage SLA < 15 min]", 'xy': (8.0, 1.8), 'w': 2.5, 'h': 1.2, 'color': '#fae8ff', 'border': '#a855f7'}
        ]
    )

    # -----------------------------------------------------------------
    # Fig 19: Regulatory Compliance Architecture
    # -----------------------------------------------------------------
    create_flow_diagram(
        "Fig 19 Regulatory Compliance Architecture.png",
        "Multi-Jurisdiction Regulatory Mapping Architecture",
        [
            {'text': "Jurisdiction Profile\n(EU / India / Global)", 'xy': (1.8, 3.8), 'w': 2.2, 'h': 1.1, 'color': '#eff6ff', 'border': '#3b82f6'},
            {'text': "Obligation Catalogue\n(GDPR, DPDP, AI Act)", 'xy': (5.0, 3.8), 'w': 2.4, 'h': 1.1, 'color': '#f3e8ff', 'border': '#9333ea'},
            {'text': "Control Mapping\n(Field & Rule Binding)", 'xy': (8.2, 3.8), 'w': 2.2, 'h': 1.1, 'color': '#dcfce7', 'border': '#16a34a'},
            {'text': "Device Policy Bundle\n(Distributed to Edge)", 'xy': (2.5, 1.8), 'w': 2.5, 'h': 1.1, 'color': '#fef3c7', 'border': '#d97706'},
            {'text': "Evidence Register\n(Compliance Proofs)", 'xy': (5.5, 1.8), 'w': 2.4, 'h': 1.1, 'color': '#f1f5f9', 'border': '#64748b'},
            {'text': "Periodic Legal Review\n(Regulatory Updates)", 'xy': (8.2, 1.8), 'w': 2.2, 'h': 1.1, 'color': '#fee2e2', 'border': '#dc2626'}
        ]
    )

    # -----------------------------------------------------------------
    # Fig 20: Security Intelligence Framework
    # -----------------------------------------------------------------
    create_flow_diagram(
        "Fig 20 Security Intelligence Framework.png",
        "Security & Threat Intelligence Integration",
        [
            {'text': "Threat Feeds\n(CVEs, Malicious IPs)", 'xy': (1.8, 3.8), 'w': 2.2, 'h': 1.1, 'color': '#fee2e2', 'border': '#ef4444'},
            {'text': "Device Telemetry\n(Firmware / Heartbeat)", 'xy': (5.0, 3.8), 'w': 2.4, 'h': 1.1, 'color': '#eff6ff', 'border': '#3b82f6'},
            {'text': "Anomaly Detection\n(Traffic / Access Outliers)", 'xy': (8.2, 3.8), 'w': 2.2, 'h': 1.1, 'color': '#fef3c7', 'border': '#d97706'},
            {'text': "Vulnerability Context\n(Device Profiling)", 'xy': (2.5, 1.8), 'w': 2.5, 'h': 1.1, 'color': '#fae8ff', 'border': '#a855f7'},
            {'text': "Containment Action\n(Isolate / Revoke Key)", 'xy': (5.5, 1.8), 'w': 2.4, 'h': 1.1, 'color': '#fee2e2', 'border': '#dc2626'},
            {'text': "Incident Record\n(Forensic Timeline)", 'xy': (8.2, 1.8), 'w': 2.2, 'h': 1.1, 'color': '#f1f5f9', 'border': '#64748b'}
        ]
    )

    # -----------------------------------------------------------------
    # Fig 21: Experimental Testbed Architecture
    # -----------------------------------------------------------------
    create_flow_diagram(
        "Fig 21 Experimental Testbed Architecture.png",
        "Synthetic Experimental Testbed & Reproducibility Pipeline",
        [
            {'text': "Synthetic Generator\n(6,000 IoT Events)", 'xy': (1.8, 3.8), 'w': 2.2, 'h': 1.1, 'color': '#f1f5f9', 'border': '#64748b'},
            {'text': "6 IoT Domains\n(Stratified 75/25 Split)", 'xy': (5.0, 3.8), 'w': 2.4, 'h': 1.1, 'color': '#eff6ff', 'border': '#3b82f6'},
            {'text': "Train / Test Split\n(Fixed Seed = 42)", 'xy': (8.2, 3.8), 'w': 2.2, 'h': 1.1, 'color': '#e0f2fe', 'border': '#0284c7'},
            {'text': "Baseline + RF + Hybrid\n(3 Detectors)", 'xy': (2.5, 1.8), 'w': 2.5, 'h': 1.1, 'color': '#fef3c7', 'border': '#d97706'},
            {'text': "Metrics Engine\n(Acc, Prec, Rec, F1, AUC)", 'xy': (5.5, 1.8), 'w': 2.4, 'h': 1.1, 'color': '#dcfce7', 'border': '#16a34a'},
            {'text': "CSV + Figures\n(600 DPI Outputs)", 'xy': (8.2, 1.8), 'w': 2.2, 'h': 1.1, 'color': '#fae8ff', 'border': '#a855f7'}
        ]
    )

    # -----------------------------------------------------------------
    # Fig 22: Evaluation Framework
    # -----------------------------------------------------------------
    create_flow_diagram(
        "Fig 22 Evaluation Framework.png",
        "Comprehensive Evaluation Metric Dimensions",
        [
            {'text': "Detection Quality\n(Precision, Recall, F1)", 'xy': (2.0, 3.8), 'w': 2.4, 'h': 1.1, 'color': '#dcfce7', 'border': '#16a34a'},
            {'text': "Privacy Controls\n(Minimization, Encryption)", 'xy': (5.0, 3.8), 'w': 2.5, 'h': 1.1, 'color': '#e0f2fe', 'border': '#0284c7'},
            {'text': "Explainability\n(Reason Code Fidelity)", 'xy': (8.0, 3.8), 'w': 2.4, 'h': 1.1, 'color': '#fae8ff', 'border': '#a855f7'},
            {'text': "Operational Cost\n(Latency, Alert Volume)", 'xy': (2.5, 1.8), 'w': 2.5, 'h': 1.1, 'color': '#fee2e2', 'border': '#dc2626'},
            {'text': "Governance Maturity\n(Audit Traceability)", 'xy': (5.5, 1.8), 'w': 2.4, 'h': 1.1, 'color': '#fef3c7', 'border': '#d97706'},
            {'text': "Reproducibility\n(Seed, Schema, Code)", 'xy': (8.2, 1.8), 'w': 2.2, 'h': 1.1, 'color': '#f1f5f9', 'border': '#64748b'}
        ]
    )

    # -----------------------------------------------------------------
    # Fig 27: Governance Maturity Framework
    # -----------------------------------------------------------------
    create_flow_diagram(
        "Fig 27 Governance Maturity Framework.png",
        "Organizational Governance Maturity Levels (Levels 1 to 5)",
        [
            {'text': "Level 1: Initial\n(Ad-hoc, No formal policy)", 'xy': (1.5, 3.0), 'w': 1.7, 'h': 1.2, 'color': '#fee2e2', 'border': '#ef4444'},
            {'text': "Level 2: Repeatable\n(Basic Checklists)", 'xy': (3.3, 3.0), 'w': 1.7, 'h': 1.2, 'color': '#fef3c7', 'border': '#f59e0b'},
            {'text': "Level 3: Defined\n(Standard Rule Engine)", 'xy': (5.1, 3.0), 'w': 1.7, 'h': 1.2, 'color': '#eff6ff', 'border': '#3b82f6'},
            {'text': "Level 4: Managed\n(AI Triage + Audits)", 'xy': (6.9, 3.0), 'w': 1.7, 'h': 1.2, 'color': '#dcfce7', 'border': '#16a34a'},
            {'text': "Level 5: Optimized\n(Continuous Adaptation)", 'xy': (8.7, 3.0), 'w': 1.7, 'h': 1.2, 'color': '#f3e8ff', 'border': '#9333ea'}
        ],
        [
            ((2.35, 3.0), (2.45, 3.0)),
            ((4.15, 3.0), (4.25, 3.0)),
            ((5.95, 3.0), (6.05, 3.0)),
            ((7.75, 3.0), (7.85, 3.0))
        ]
    )

    # -----------------------------------------------------------------
    # Fig 28: Smart City Compliance Ecosystem
    # -----------------------------------------------------------------
    create_flow_diagram(
        "Fig 28 Smart City Compliance Ecosystem.png",
        "Smart City Multi-Source Governance Ecosystem",
        [
            {'text': "Traffic Sensors &\nCameras", 'xy': (1.8, 3.8), 'w': 2.2, 'h': 1.1, 'color': '#eff6ff', 'border': '#3b82f6'},
            {'text': "Environmental\nMonitors", 'xy': (1.8, 1.8), 'w': 2.2, 'h': 1.1, 'color': '#eff6ff', 'border': '#3b82f6'},
            {'text': "Edge Gateways\n(Local Aggregation)", 'xy': (4.8, 2.8), 'w': 2.2, 'h': 1.3, 'color': '#dcfce7', 'border': '#16a34a'},
            {'text': "City Data Platform\n(Purpose-Bound)", 'xy': (7.8, 3.8), 'w': 2.3, 'h': 1.1, 'color': '#fef3c7', 'border': '#d97706'},
            {'text': "Public Audit &\nTransparency Portal", 'xy': (7.8, 1.8), 'w': 2.3, 'h': 1.1, 'color': '#f1f5f9', 'border': '#64748b'}
        ],
        [
            ((2.9, 3.8), (3.7, 3.2)),
            ((2.9, 1.8), (3.7, 2.4)),
            ((5.9, 3.2), (6.65, 3.8)),
            ((5.9, 2.4), (6.65, 1.8))
        ]
    )

    # -----------------------------------------------------------------
    # Fig 29: Healthcare IoT Governance Framework
    # -----------------------------------------------------------------
    create_flow_diagram(
        "Fig 29 Healthcare IoT Governance Framework.png",
        "Healthcare IoT Governance Architecture",
        [
            {'text': "Wearable / Clinical\nSensors", 'xy': (1.8, 3.0), 'w': 2.2, 'h': 1.3, 'color': '#fee2e2', 'border': '#ef4444'},
            {'text': "Local Filtering &\nEmergency Bypass", 'xy': (4.5, 3.8), 'w': 2.2, 'h': 1.1, 'color': '#dcfce7', 'border': '#16a34a'},
            {'text': "Care-Context Policy\n(Strict Need-to-Know)", 'xy': (4.5, 2.0), 'w': 2.3, 'h': 1.1, 'color': '#fef3c7', 'border': '#d97706'},
            {'text': "Secure Clinical\nService (EHR)", 'xy': (7.5, 3.8), 'w': 2.2, 'h': 1.1, 'color': '#eff6ff', 'border': '#3b82f6'},
            {'text': "Consent & Audit\nRegistry", 'xy': (7.5, 2.0), 'w': 2.2, 'h': 1.1, 'color': '#f3e8ff', 'border': '#9333ea'}
        ],
        [
            ((2.9, 3.3), (3.4, 3.8)),
            ((2.9, 2.7), (3.35, 2.0)),
            ((5.6, 3.8), (6.4, 3.8)),
            ((5.65, 2.0), (6.4, 2.0))
        ]
    )

    # -----------------------------------------------------------------
    # Fig 31: Challenges and Limitations Roadmap
    # -----------------------------------------------------------------
    create_flow_diagram(
        "Fig 31 Challenges and Limitations Roadmap.png",
        "Identified Limitations and Concrete Mitigation Paths",
        [
            {'text': "Challenge: Data Drift\n& Spurious Patterns", 'xy': (2.0, 3.8), 'w': 2.5, 'h': 1.1, 'color': '#fee2e2', 'border': '#dc2626'},
            {'text': "Challenge: Device &\nResource Limits", 'xy': (5.0, 3.8), 'w': 2.5, 'h': 1.1, 'color': '#fee2e2', 'border': '#dc2626'},
            {'text': "Challenge: False Alert\nFatigue", 'xy': (8.0, 3.8), 'w': 2.5, 'h': 1.1, 'color': '#fee2e2', 'border': '#dc2626'},
            {'text': "Mitigation: Periodic\nRetraining & Drift Check", 'xy': (2.0, 1.8), 'w': 2.5, 'h': 1.1, 'color': '#dcfce7', 'border': '#16a34a'},
            {'text': "Mitigation: Tiered Rules\n& Lightweight Gateway", 'xy': (5.0, 1.8), 'w': 2.5, 'h': 1.1, 'color': '#dcfce7', 'border': '#16a34a'},
            {'text': "Mitigation: Hybrid Rules\n+ Action Escalation", 'xy': (8.0, 1.8), 'w': 2.5, 'h': 1.1, 'color': '#dcfce7', 'border': '#16a34a'}
        ],
        [
            ((2.0, 3.25), (2.0, 2.35)),
            ((5.0, 3.25), (5.0, 2.35)),
            ((8.0, 3.25), (8.0, 2.35))
        ]
    )

    # -----------------------------------------------------------------
    # Fig 32: Future Research Roadmap
    # -----------------------------------------------------------------
    create_flow_diagram(
        "Fig 32 Future Research Roadmap.png",
        "Future Research Roadmap & Milestones",
        [
            {'text': "Phase 1: Multi-Site\nEvaluation (Real Data)", 'xy': (1.8, 3.8), 'w': 2.3, 'h': 1.1, 'color': '#eff6ff', 'border': '#3b82f6'},
            {'text': "Phase 2: Privacy-Budget\nAccounting (DP ε-bounds)", 'xy': (5.0, 3.8), 'w': 2.4, 'h': 1.1, 'color': '#f3e8ff', 'border': '#9333ea'},
            {'text': "Phase 3: Robust Federated\nLearning (Poison-defense)", 'xy': (8.2, 3.8), 'w': 2.3, 'h': 1.1, 'color': '#fef3c7', 'border': '#d97706'},
            {'text': "Phase 4: Formal Policy\nVerification & Logic Checks", 'xy': (3.0, 1.8), 'w': 2.6, 'h': 1.1, 'color': '#dcfce7', 'border': '#16a34a'},
            {'text': "Phase 5: Human Factors &\nReviewer Cognitive Load", 'xy': (7.0, 1.8), 'w': 2.6, 'h': 1.1, 'color': '#fee2e2', 'border': '#dc2626'}
        ]
    )

    # -----------------------------------------------------------------
    # Fig 33: Next-Generation AI Governance Ecosystem
    # -----------------------------------------------------------------
    create_flow_diagram(
        "Fig 33 Next-Generation AI Governance Ecosystem.png",
        "Next-Generation AI Governance Ecosystem",
        [
            {'text': "Autonomous\nCompliance Agents", 'xy': (2.0, 3.8), 'w': 2.4, 'h': 1.1, 'color': '#f3e8ff', 'border': '#9333ea'},
            {'text': "Privacy-Aware\nDigital Twins", 'xy': (5.0, 3.8), 'w': 2.4, 'h': 1.1, 'color': '#eff6ff', 'border': '#2563eb'},
            {'text': "Continuous Policy\nRegression Testing", 'xy': (8.0, 3.8), 'w': 2.4, 'h': 1.1, 'color': '#dcfce7', 'border': '#16a34a'},
            {'text': "Cross-Border\nSovereignty Controls", 'xy': (3.5, 1.8), 'w': 2.5, 'h': 1.1, 'color': '#fef3c7', 'border': '#d97706'},
            {'text': "Human-in-the-Loop\nAccountability Matrix", 'xy': (7.0, 1.8), 'w': 2.5, 'h': 1.1, 'color': '#fee2e2', 'border': '#dc2626'}
        ]
    )

    # -----------------------------------------------------------------
    # Fig 34: Research Contribution Framework
    # -----------------------------------------------------------------
    create_flow_diagram(
        "Fig 34 Research Contribution Framework.png",
        "Research Contribution & Artifact Mapping Framework",
        [
            {'text': "Literature Synthesis\n(81 Key References)", 'xy': (1.8, 3.8), 'w': 2.2, 'h': 1.1, 'color': '#f1f5f9', 'border': '#64748b'},
            {'text': "Layered Architecture\n(6 Logical Planes)", 'xy': (5.0, 3.8), 'w': 2.3, 'h': 1.1, 'color': '#eff6ff', 'border': '#3b82f6'},
            {'text': "Risk Scoring Model\n(Calibrated Equations)", 'xy': (8.2, 3.8), 'w': 2.2, 'h': 1.1, 'color': '#fef3c7', 'border': '#d97706'},
            {'text': "Synthetic Benchmark\n(6,000 Events, N=1500 Test)", 'xy': (1.8, 1.8), 'w': 2.3, 'h': 1.1, 'color': '#dcfce7', 'border': '#16a34a'},
            {'text': "Implementation Package\n(Code, Dataset, Diagrams)", 'xy': (5.0, 1.8), 'w': 2.3, 'h': 1.1, 'color': '#fae8ff', 'border': '#a855f7'},
            {'text': "Limitations & Roadmap\n(Transparent Boundary)", 'xy': (8.2, 1.8), 'w': 2.2, 'h': 1.1, 'color': '#fee2e2', 'border': '#dc2626'}
        ]
    )

    print("All 34 high-resolution 600 DPI diagrams have been successfully synthesized!")

if __name__ == "__main__":
    generate_all_figures()
