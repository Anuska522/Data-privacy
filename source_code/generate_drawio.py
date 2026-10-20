"""
Generator for all_diagrams.drawio (Multi-Page XML for Diagrams.net / Draw.io)
Course: BCSE318L Data Privacy
Author: Anuska Saha (Reg No: 23BCE0167)
"""

import os
import xml.etree.ElementTree as ET

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIAGRAMS_DIR = os.path.join(BASE_DIR, "diagrams")

DIAGRAM_TITLES = [
    "Fig 01 Evolution of IoT Ecosystems and Compliance Challenges",
    "Fig 02 AI-Driven Privacy Governance Landscape",
    "Fig 03 IoT Privacy Compliance Challenge Landscape",
    "Fig 04 Literature Taxonomy Framework",
    "Fig 05 Requirements Engineering Framework",
    "Fig 06 AI-Driven Privacy Compliance Architecture for Heterogeneous IoT Environments",
    "Fig 07 Multi-Layer Compliance Framework",
    "Fig 08 IoT Data Acquisition Framework",
    "Fig 09 Edge Governance Architecture",
    "Fig 10 Edge Compliance Monitoring Workflow",
    "Fig 11 AI Privacy Risk Assessment Framework",
    "Fig 12 Risk Prediction Pipeline",
    "Fig 13 Compliance Automation Workflow",
    "Fig 14 Policy Enforcement Lifecycle",
    "Fig 15 Privacy Protection Framework",
    "Fig 16 Data Protection Lifecycle",
    "Fig 17 Explainable Compliance Framework",
    "Fig 18 Auditability and Transparency Dashboard",
    "Fig 19 Regulatory Compliance Architecture",
    "Fig 20 Security Intelligence Framework",
    "Fig 21 Experimental Testbed Architecture",
    "Fig 22 Evaluation Framework",
    "Fig 23 Compliance Accuracy Performance Analysis",
    "Fig 24 Privacy-Preservation Control Indicators",
    "Fig 25 Governance Maturity and Compliance Assessment",
    "Fig 26 Comparative Benchmark Analysis",
    "Fig 27 Governance Maturity Framework",
    "Fig 28 Smart City Compliance Ecosystem",
    "Fig 29 Healthcare IoT Governance Framework",
    "Fig 30 Control-Coverage Dashboard",
    "Fig 31 Challenges and Limitations Roadmap",
    "Fig 32 Future Research Roadmap",
    "Fig 33 Next-Generation AI Governance Ecosystem",
    "Fig 34 Research Contribution Framework"
]

def generate_drawio_xml():
    mxfile = ET.Element("mxfile", host="app.diagrams.net", modified="2026-10-20T15:00:00.000Z", agent="Antigravity", version="24.0.0", type="device")
    
    for idx, title in enumerate(DIAGRAM_TITLES):
        diagram = ET.SubElement(mxfile, "diagram", id=f"diag-{idx+1}", name=title)
        mxGraphModel = ET.SubElement(diagram, "mxGraphModel", dx="1000", dy="600", grid="1", gridSize="10", guides="1", tooltips="1", connect="1", arrows="1", fold="1", page="1", pageScale="1", pageWidth="827", pageHeight="1169", math="0", shadow="0")
        root = ET.SubElement(mxGraphModel, "root")
        ET.SubElement(root, "mxCell", id="0")
        ET.SubElement(root, "mxCell", id="1", parent="0")

        # Title Cell
        ET.SubElement(root, "mxCell", id=f"title-{idx}", value=f"&lt;b&gt;{title}&lt;/b&gt;", style="text;html=1;align=center;verticalAlign=middle;resizable=0;points=[];autosize=1;strokeColor=none;fillColor=none;fontSize=14;fontColor=#1e293b;", vertex="1", parent="1")
        ET.SubElement(root[-1], "mxGeometry", x="150", y="40", width="500", height="30", as_="geometry")

        # 3 Structured Layer Boxes representing the core architecture
        layers = [
            ("Input & Ingestion Layer", "#e0f2fe", "#0284c7", 80),
            ("Processing, Governance & Risk Assessment", "#fef3c7", "#d97706", 180),
            ("Enforcement, Audit & Output Plane", "#dcfce7", "#16a34a", 280)
        ]

        for l_idx, (l_name, bg, border, y_pos) in enumerate(layers):
            cell_id = f"box-{idx}-{l_idx}"
            cell = ET.SubElement(root, "mxCell", id=cell_id, value=f"&lt;b&gt;{l_name}&lt;/b&gt;", style=f"rounded=1;whiteSpace=wrap;html=1;fillColor={bg};strokeColor={border};strokeWidth=2;fontSize=12;fontColor=#0f172a;", vertex="1", parent="1")
            ET.SubElement(cell, "mxGeometry", x="200", y=str(y_pos), width="400", height="60", as_="geometry")

            if l_idx > 0:
                edge_id = f"edge-{idx}-{l_idx}"
                edge = ET.SubElement(root, "mxCell", id=edge_id, style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#475569;strokeWidth=2;", edge="1", parent="1", source=f"box-{idx}-{l_idx-1}", target=cell_id)
                ET.SubElement(edge, "mxGeometry", relative="1", as_="geometry")

    tree = ET.ElementTree(mxfile)
    ET.indent(tree, space="  ", level=0)
    out_file = os.path.join(DIAGRAMS_DIR, "all_diagrams.drawio")
    tree.write(out_file, encoding="utf-8", xml_declaration=True)
    print(f"Generated editable diagrams source: {out_file}")

if __name__ == "__main__":
    generate_drawio_xml()
