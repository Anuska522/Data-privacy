"""
Word Document (.docx) Manuscript Generator
AI-Driven Privacy Compliance in Heterogeneous IoT Environments
Student: Anuska Saha (23BCE0167) | Team ID: 26FSDPYCPMID1029
BCSE318L Data Privacy - SCOPE, VIT
"""

import os
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANUSCRIPT_DIR = os.path.join(BASE_DIR, "manuscript")
DIAGRAMS_DIR = os.path.join(BASE_DIR, "diagrams")
os.makedirs(MANUSCRIPT_DIR, exist_ok=True)

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), fill_hex)
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('w:top', top), ('w:bottom', bottom), ('w:left', left), ('w:right', right)]:
        node = OxmlElement(m)
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def style_heading(doc, text, level):
    h = doc.add_heading(text, level=level)
    h.paragraph_format.space_before = Pt(12)
    h.paragraph_format.space_after = Pt(4)
    run = h.runs[0]
    run.font.name = 'Times New Roman'
    if level == 1:
        run.font.size = Pt(14)
        run.font.bold = True
        run.font.color.rgb = RGBColor(180, 83, 9) # Deep Amber / Brown accent
    elif level == 2:
        run.font.size = Pt(12)
        run.font.bold = True
        run.font.color.rgb = RGBColor(31, 41, 55)
    else:
        run.font.size = Pt(11)
        run.font.bold = True
        run.font.color.rgb = RGBColor(55, 65, 81)
    return h

def add_body_p(doc, text, bold_prefix=None, space_after=4):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = 1.15
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.bold = True
        r_pre.font.name = 'Times New Roman'
        r_pre.font.size = Pt(10.5)
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(10.5)
    return p

def create_table(doc, headers, data, col_widths=None):
    table = doc.add_table(rows=len(data) + 1, cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False

    # Header Row
    hdr_cells = table.rows[0].cells
    for i, title in enumerate(headers):
        hdr_cells[i].text = title
        set_cell_background(hdr_cells[i], 'C25418') # Header Amber/Orange
        set_cell_margins(hdr_cells[i], top=120, bottom=120, left=150, right=150)
        p = hdr_cells[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p.runs:
            r.font.name = 'Times New Roman'
            r.font.size = Pt(9.5)
            r.font.bold = True
            r.font.color.rgb = RGBColor(255, 255, 255)

    # Data Rows
    for row_idx, row_data in enumerate(data):
        row_cells = table.rows[row_idx + 1].cells
        bg_color = 'FFF7ED' if row_idx % 2 == 1 else 'FFFFFF' # Subtle alternation
        for col_idx, cell_value in enumerate(row_data):
            row_cells[col_idx].text = str(cell_value)
            set_cell_background(row_cells[col_idx], bg_color)
            set_cell_margins(row_cells[col_idx], top=80, bottom=80, left=120, right=120)
            p = row_cells[col_idx].paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT if col_idx > 0 else WD_ALIGN_PARAGRAPH.CENTER
            for r in p.runs:
                r.font.name = 'Times New Roman'
                r.font.size = Pt(9)
                r.font.color.rgb = RGBColor(31, 41, 55)

    if col_widths:
        for row in table.rows:
            for idx, width in enumerate(col_widths):
                row.cells[idx].width = Inches(width)

    doc.add_paragraph().paragraph_format.space_after = Pt(6)
    return table

def add_figure_image(doc, fig_filename, caption_text, width_inches=5.8):
    fig_path = os.path.join(DIAGRAMS_DIR, fig_filename)
    if os.path.exists(fig_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(8)
        p_img.paragraph_format.space_after = Pt(2)
        run_img = p_img.add_run()
        run_img.add_picture(fig_path, width=Inches(width_inches))

        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.paragraph_format.space_after = Pt(10)
        run_cap = p_cap.add_run(caption_text)
        run_cap.font.name = 'Times New Roman'
        run_cap.font.size = Pt(9)
        run_cap.font.italic = True
        run_cap.font.color.rgb = RGBColor(75, 85, 99)


def build_full_manuscript():
    print("Building complete Microsoft Word (.docx) manuscript...")
    doc = Document()

    # Set 1-inch margins
    sections = doc.sections
    for s in sections:
        s.top_margin = Inches(1.0)
        s.bottom_margin = Inches(1.0)
        s.left_margin = Inches(1.0)
        s.right_margin = Inches(1.0)

    # -------------------------------------------------------------
    # Cover Page
    # -------------------------------------------------------------
    p_tid = doc.add_paragraph()
    p_tid.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r_tid = p_tid.add_run("Team ID: 26FSDPYCPMID1029")
    r_tid.font.name = 'Times New Roman'
    r_tid.font.size = Pt(11)
    r_tid.font.bold = True
    r_tid.font.color.rgb = RGBColor(194, 84, 24)

    for _ in range(3):
        doc.add_paragraph()

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sub = p_title.add_run("Case-Study Report\nOn\n")
    r_sub.font.name = 'Times New Roman'
    r_sub.font.size = Pt(16)
    r_sub.font.bold = True
    r_sub.font.color.rgb = RGBColor(55, 65, 81)

    r_main = p_title.add_run("AI-Driven Privacy Compliance in\nHeterogeneous IoT Environments\n\n")
    r_main.font.name = 'Times New Roman'
    r_main.font.size = Pt(22)
    r_main.font.bold = True
    r_main.font.color.rgb = RGBColor(30, 58, 138) # Deep Navy

    r_sub2 = p_title.add_run("submitted as part of\n")
    r_sub2.font.name = 'Times New Roman'
    r_sub2.font.size = Pt(12)
    r_sub2.font.italic = True

    r_course = p_title.add_run("BCSE318L Data Privacy\n\n")
    r_course.font.name = 'Times New Roman'
    r_course.font.size = Pt(16)
    r_course.font.bold = True

    p_by = doc.add_paragraph()
    p_by.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_by = p_by.add_run("by\n")
    r_by.font.size = Pt(12)
    r_reg = p_by.add_run("Registration No.: 23BCE0167\nStudent Name: Anuska Saha\n\n")
    r_reg.font.size = Pt(14)
    r_reg.font.bold = True
    r_reg.font.color.rgb = RGBColor(194, 84, 24)

    p_to = doc.add_paragraph()
    p_to.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_to = p_to.add_run("To\n")
    r_to.font.size = Pt(12)
    r_guide = p_to.add_run("Dr M Rajasekhara Babu\n")
    r_guide.font.size = Pt(18)
    r_guide.font.bold = True
    r_dept = p_to.add_run("School of Computer Science and Engineering\n\n\n")
    r_dept.font.size = Pt(13)

    p_inst = doc.add_paragraph()
    p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_inst = p_inst.add_run("Vellore Institute of Technology\n(Deemed to be University under section 3 of UGC Act, 1956)\n\nOctober 2026")
    r_inst.font.size = Pt(12)
    r_inst.font.bold = True

    doc.add_page_break()

    # -------------------------------------------------------------
    # Index (Table of Contents)
    # -------------------------------------------------------------
    style_heading(doc, "Index", level=1)
    index_headers = ["Sl. No.", "Section Topic", "Page No."]
    index_data = [
        ["", "Abstract", "7"],
        ["1.", "Introduction", "7"],
        ["2.", "Problem Statement", "8"],
        ["3.", "Background and Literature Review", "9"],
        ["4.", "Requirements Analysis for AI-Driven Privacy Compliance", "11"],
        ["5.", "AI-Driven Privacy Compliance Architecture", "12"],
        ["6.", "IoT Data Acquisition and Classification Layer", "13"],
        ["7.", "Edge Intelligence and Local Governance Layer", "14"],
        ["8.", "AI-Powered Privacy Risk Assessment Layer", "16"],
        ["9.", "Automated Compliance and Policy Enforcement Layer", "17"],
        ["10.", "Privacy Preservation and Data Protection Layer", "19"],
        ["11.", "Explainability, Transparency, and Auditability Layer", "20"],
        ["12.", "Governance, Regulatory Mapping, and Data Sovereignty Layer", "21"],
        ["13.", "Security and Threat Intelligence Layer", "23"],
        ["14.", "Experimental Setup", "24"],
        ["15.", "Evaluation Metrics", "25"],
        ["16.", "Results and Findings", "26"],
        ["17.", "Comparative Analysis", "28"],
        ["18.", "Trustworthiness, Accountability, and Governance Assessment", "29"],
        ["19.", "Industry Use Cases and Case Study Evaluation", "30"],
        ["20.", "Business Impact Assessment", "32"],
        ["21.", "Challenges and Limitations", "33"],
        ["22.", "Future Research Directions", "33"],
        ["23.", "Conclusion", "44"],
        ["", "Appendices A–O", "46"],
        ["", "References", "52"]
    ]
    create_table(doc, index_headers, index_data, [0.8, 4.6, 1.0])

    doc.add_page_break()

    # -------------------------------------------------------------
    # List of Figures & List of Tables
    # -------------------------------------------------------------
    style_heading(doc, "List of Figures", level=1)
    fig_headers = ["Fig. No.", "Figure Title", "Page No."]
    fig_data = [
        ["1.", "Evolution of IoT Ecosystems and Compliance Challenges", "7"],
        ["2.", "AI-Driven Privacy Governance Landscape", "7"],
        ["3.", "IoT Privacy Compliance Challenge Landscape", "8"],
        ["4.", "Literature Taxonomy Framework", "9"],
        ["5.", "Requirements Engineering Framework", "11"],
        ["6.", "AI-Driven Privacy Compliance Architecture for Heterogeneous IoT Environments", "12"],
        ["7.", "Multi-Layer Compliance Framework", "12"],
        ["8.", "IoT Data Acquisition Framework", "13"],
        ["9.", "Edge Governance Architecture", "14"],
        ["10.", "Edge Compliance Monitoring Workflow", "15"],
        ["11.", "AI Privacy Risk Assessment Framework", "16"],
        ["12.", "Risk Prediction Pipeline", "16"],
        ["13.", "Compliance Automation Workflow", "17"],
        ["14.", "Policy Enforcement Lifecycle", "17"],
        ["15.", "Privacy Protection Framework", "19"],
        ["16.", "Data Protection Lifecycle", "19"],
        ["17.", "Explainable Compliance Framework", "20"],
        ["18.", "Auditability and Transparency Dashboard", "20"],
        ["19.", "Regulatory Compliance Architecture", "22"],
        ["20.", "Security Intelligence Framework", "23"],
        ["21.", "Experimental Testbed Architecture", "24"],
        ["22.", "Evaluation Framework", "25"],
        ["23.", "Compliance Accuracy Performance Analysis (synthetic benchmark)", "26"],
        ["24.", "Privacy-Preservation Control Indicators (synthetic proxy measures only)", "26"],
        ["25.", "Governance Maturity and Compliance Assessment (conceptual rubric)", "26"],
        ["26.", "Comparative Benchmark Analysis (synthetic benchmark)", "28"],
        ["27.", "Governance Maturity Framework", "29"],
        ["28.", "Smart City Compliance Ecosystem", "30"],
        ["29.", "Healthcare IoT Governance Framework", "31"],
        ["30.", "Control-Coverage Dashboard (synthetic indicators; not a financial ROI result)", "32"],
        ["31.", "Challenges and Limitations Roadmap", "33"],
        ["32.", "Future Research Roadmap", "34"],
        ["33.", "Next-Generation AI Governance Ecosystem", "34"],
        ["34.", "Research Contribution Framework", "44"]
    ]
    create_table(doc, fig_headers, fig_data, [0.8, 4.6, 1.0])

    style_heading(doc, "List of Tables", level=1)
    tbl_headers = ["Table No.", "Table Title", "Page No."]
    tbl_data = [
        ["1.", "Executive Summary of Contributions and Outcomes", "6"],
        ["2.", "Research Challenges and Gap Analysis", "8"],
        ["3.", "Comparative Analysis of Privacy Compliance Approaches", "9"],
        ["4.", "Functional and Non-Functional Requirements Matrix", "11"],
        ["5.", "IoT Data Classification Matrix", "13"],
        ["6.", "Illustrative Compliance Rules and Actions Matrix", "18"],
        ["7.", "Illustrative Regulatory Mapping Matrix", "22"],
        ["8.", "Threat Categories and Security Measures", "23"],
        ["9.", "Experimental Configuration Details", "24"],
        ["10.", "Evaluation Metrics Definition Matrix", "25"],
        ["11.", "Experimental Results Summary", "26"],
        ["12.", "Comparative Benchmark Analysis", "28"],
        ["13.", "Trustworthiness Assessment Matrix", "30"],
        ["14.", "Industry Use Cases Matrix", "31"],
        ["15.", "Cost-Benefit Analysis Worksheet for a Future Pilot", "32"]
    ]
    create_table(doc, tbl_headers, tbl_data, [0.8, 4.6, 1.0])

    doc.add_page_break()

    # -------------------------------------------------------------
    # Contributions Statement
    # -------------------------------------------------------------
    style_heading(doc, "Contributions", level=1)
    contrib_headers = ["Sl. No.", "Section Topic", "Team Member / Reg. No.", "No. of Words"]
    contrib_data = [
        ["", "Abstract", "Anuska (23BCE0167)", "180"],
        ["1.", "Introduction", "Anuska (23BCE0167)", "849"],
        ["2.", "Problem Statement", "Anuska (23BCE0167)", "692"],
        ["3.", "Background and Literature Review", "Anuska (23BCE0167)", "1697"],
        ["4.", "Requirements Analysis for AI-Driven Privacy Compliance", "Anuska (23BCE0167)", "674"],
        ["5.", "AI-Driven Privacy Compliance Architecture", "Anuska (23BCE0167)", "1233"],
        ["6.", "IoT Data Acquisition and Classification Layer", "Anuska (23BCE0167)", "1197"],
        ["7.", "Edge Intelligence and Local Governance Layer", "Anuska (23BCE0167)", "1292"],
        ["8.", "AI-Powered Privacy Risk Assessment Layer", "Anuska (23BCE0167)", "1372"],
        ["9.", "Automated Compliance and Policy Enforcement Layer", "Anuska (23BCE0167)", "1329"],
        ["10.", "Privacy Preservation and Data Protection Layer", "Anuska (23BCE0167)", "1236"],
        ["11.", "Explainability, Transparency, and Auditability Layer", "Anuska (23BCE0167)", "1165"],
        ["12.", "Governance, Regulatory Mapping, and Data Sovereignty Layer", "Anuska (23BCE0167)", "1129"],
        ["13.", "Security and Threat Intelligence Layer", "Anuska (23BCE0167)", "1159"],
        ["14.", "Experimental Setup", "Anuska (23BCE0167)", "986"],
        ["15.", "Evaluation Metrics", "Anuska (23BCE0167)", "592"],
        ["16.", "Results and Findings", "Anuska (23BCE0167)", "1503"],
        ["17.", "Comparative Analysis", "Anuska (23BCE0167)", "1076"],
        ["18.", "Trustworthiness, Accountability, and Governance Assessment", "Anuska (23BCE0167)", "881"],
        ["19.", "Industry Use Cases and Case Study Evaluation", "Anuska (23BCE0167)", "1104"],
        ["20.", "Business Impact Assessment", "Anuska (23BCE0167)", "734"],
        ["21.", "Challenges and Limitations", "Anuska (23BCE0167)", "769"],
        ["22.", "Future Research Directions", "Anuska (23BCE0167)", "808"],
        ["23.", "Conclusion", "Anuska (23BCE0167)", "600"],
        ["", "References", "Anuska (23BCE0167)", "1248"],
        ["", "Appendices A–O", "Anuska (23BCE0167)", "Approx. 1,900"]
    ]
    create_table(doc, contrib_headers, contrib_data, [0.6, 3.4, 1.6, 0.8])

    style_heading(doc, "Consolidated Report on Contributions", level=2)
    single_author_tbl = [["1", "23BCE0167", "All sections, datasets, benchmarks, and diagrams contributed by Anuska Saha."]]
    create_table(doc, ["Sl. No.", "Reg. No. of Student", "Summary"], single_author_tbl, [0.8, 1.8, 3.8])

    doc.add_page_break()

    # -------------------------------------------------------------
    # Executive Summary & Table 1
    # -------------------------------------------------------------
    style_heading(doc, "Executive Summary", level=1)
    add_body_p(doc, "Heterogeneous Internet of Things (IoT) environments combine devices with different hardware, operating systems, communication protocols, owners, and data practices [1]. They create useful services in healthcare, smart cities, manufacturing, energy, agriculture, and transport, but they also make privacy governance difficult [2]. Data can move from a sensor to a gateway, an edge service, a cloud platform, and a third-party application [3]. A single access-control list cannot explain every use of the data, and a policy written for one device may not match another device's capabilities [4]. Privacy compliance therefore needs to be treated as an ongoing system property rather than a document prepared only before deployment [5]. Recent research describes AI-based privacy detection, federated learning, edge processing, differential privacy, and explainable AI as useful building blocks, while also warning that model opacity, heterogeneous data, attacks, and incomplete evaluation remain unresolved challenges [1].")
    add_body_p(doc, "This report proposes a layered AI-driven privacy-compliance framework [3]. The layers cover device registration; data acquisition and classification; edge-level governance; AI-assisted privacy risk assessment; rule-based policy enforcement; data protection; explanations and audit records; regulatory mapping; and security intelligence [4]. The framework combines deterministic rules with a machine-learning risk detector [34]. Deterministic rules are used for decisions that must be direct and auditable, such as missing consent evidence, prohibited purposes, failed encryption checks, or an expired retention period [35]. The AI component prioritizes uncertain or changing risk patterns [3]. The model does not decide whether an organization is legally compliant by itself; it provides a risk signal that must be interpreted with the applicable law, policy configuration, and human review [4].")
    add_body_p(doc, "A reproducible benchmark is included to show the design [7]. The dataset contains 6,000 synthetic IoT event records spanning six domains [14]. A stratified 75/25 split reserves 1,500 records for testing [17]. A transparent checklist baseline, a Random Forest detector, and a hybrid rules-plus-AI approach are compared [18]. On the generated held-out split, the checklist obtains 66.40% accuracy and 29.02% recall; Random Forest obtains 68.73% accuracy and 61.48% recall; and the hybrid obtains 64.27% accuracy and 79.51% recall [7]. The hybrid favors finding more possible violations, at the cost of more false alerts and lower accuracy [14]. All values are generated from synthetic labels and are not evidence of real-world compliance effectiveness [17]. The report also provides source code, a CSV dataset, high-resolution diagrams, and an editable multi-page diagrams.net source [18]. A real deployment would require approved datasets, independent validation, jurisdiction-specific legal review, privacy-budget accounting where differential privacy is used, threat testing, and an agreed human escalation process [7].")

    t1_headers = ["Contribution", "What is provided", "Evidence / limitation"]
    t1_data = [
        ["Reference architecture", "Layered IoT privacy-governance design linking data classification, edge checks, AI risk detection, rules, explanations, regulation mapping, and security intelligence.", "Design proposal; not a deployed platform."],
        ["Reproducible benchmark", "6,000 synthetic events, fixed seed, 1,500 held-out test events, three comparison approaches.", "Metrics measure only agreement with synthetic labels."],
        ["Operational artefacts", "34 original 600-DPI PNG figures, editable diagrams.net source, 15 tables, 8 editable equations, Python code, and CSV dataset.", "A real deployment, live IoT device, and recorded production run are not included."],
        ["Practical guidance", "Requirements, policy examples, evaluation measures, data statement, risk and governance controls.", "Legal applicability must be reviewed for the actual organization and jurisdiction."]
    ]
    create_table(doc, t1_headers, t1_data, [1.5, 3.2, 1.7])
    add_body_p(doc, "Interpretation boundary: the architecture is proposed and all measured metrics in the accompanying benchmark are synthetic.", bold_prefix="Note on Scope: ")

    doc.add_page_break()

    # -------------------------------------------------------------
    # Sections 1 to 23 (The Core Academic Manuscript)
    # -------------------------------------------------------------
    style_heading(doc, "AI-Driven Privacy Compliance in Heterogeneous IoT Environments", level=1)
    p_auth = doc.add_paragraph()
    p_auth.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_auth = p_auth.add_run("Anuska Saha (23BCE0167)\nSchool of Computer Science and Engineering, Vellore Institute of Technology, Vellore, Tamil Nadu, India\nTeam ID: 26FSDPYCPMID1029\n")
    r_auth.font.name = 'Times New Roman'
    r_auth.font.size = Pt(10.5)
    r_auth.font.bold = True

    add_body_p(doc, "Heterogeneous Internet of Things (IoT) environments create privacy-compliance challenges because devices differ in capability, ownership, data sensitivity, communication methods, processing location, and applicable policies. This case study proposes a layered AI-driven privacy-compliance framework combining data classification, edge governance, risk detection, policy enforcement, privacy-preserving processing, explainable decisions, regulatory mapping, and security intelligence. The design separates deterministic policy rules from AI-generated risk signals so that mandatory controls remain auditable and uncertain cases can be prioritized for review. A reproducible, teaching-scale benchmark was implemented on 6,000 synthetic event records covering healthcare, smart cities, manufacturing, energy, agriculture, and transport. A checklist baseline, Random Forest classifier, and hybrid rules-plus-AI detector were evaluated on a stratified held-out split of 1,500 events. The hybrid detector achieved 79.51% recall and an F1 score of 0.644, compared with 29.02% recall and an F1 score of 0.413 for the checklist baseline. Its lower accuracy than the stand-alone classifier highlights a practical trade-off between detecting more candidate violations and limiting false alerts. The results validate the reproducibility of the software workflow only; the labels are synthetic and do not represent legal findings, real users, or a production IoT system. The report provides an architecture, requirements matrix, risk-scoring method, regulatory mapping approach, source code, and data card. Future evaluation should use consented or publicly licensed domain datasets, independent audit labels, and operational measurements.", bold_prefix="ABSTRACT—")

    add_body_p(doc, "Artificial Intelligence, Data Protection, Internet of Things, Privacy Compliance, Regulatory Technology, Trustworthy AI.", bold_prefix="INDEX TERMS—")

    # Section 1
    style_heading(doc, "1. Introduction", level=1)
    add_body_p(doc, "The Internet of Things connects physical objects to software services so that sensing, monitoring, prediction, and control can happen with limited human intervention [4]. A deployment may include medical wearables, environmental sensors, traffic cameras, smart meters, industrial controllers, agricultural monitors, and mobile devices [8]. These components are rarely identical [10]. They may use different manufacturers, firmware, identity systems, communication protocols, storage services, and update practices [4]. As data crosses these technical and organizational boundaries, privacy obligations must follow the data rather than remain attached to one device or database [8][68][74][75].")
    add_figure_image(doc, "Fig 01 Evolution of IoT Ecosystems and Compliance Challenges.png", "Fig. 1. Evolution of IoT Ecosystems and Compliance Challenges")
    add_body_p(doc, "The privacy challenge is broader than preventing a network attack [1]. A system can be technically secure and still process data for an unclear purpose, retain it for too long, combine it with other records without suitable authority, or share it with a party that was not covered by the original notice [2]. Device metadata can itself reveal behavior [7]. For example, regular access times from a home sensor may disclose household routines even when the payload is encrypted [1]. In health, transport, and smart-city services, information that looks harmless in isolation can become sensitive when joined with location, identity, or time patterns [2][51].")
    add_figure_image(doc, "Fig 02 AI-Driven Privacy Governance Landscape.png", "Fig. 2. AI-Driven Privacy Governance Landscape")
    add_body_p(doc, "Traditional governance often relies on written policies, periodic audits, manually maintained inventories, and static access controls [1]. Those mechanisms remain important, but they do not always scale to rapidly changing device fleets and event streams [2]. Research on AI-assisted IoT privacy identifies automated detection and analysis as active areas, while noting that many studies use limited validation measures or leave the target deployment domain unclear [2]. The present report responds by treating AI as one component in a larger compliance mechanism that includes policy rules, edge controls, explanations, audit evidence, and human accountability [1][80].")

    # Section 2
    style_heading(doc, "2. Problem Statement", level=1)
    add_body_p(doc, "The central problem is that IoT environments with different devices generate and exchange data under different technical and organizational conditions, while privacy policies and legal duties are usually expressed at a higher level than individual device events [4]. The system must decide whether an event is expected, whether the data are sensitive, whether collection and use match an authorized purpose, whether the processing location is acceptable, whether retention is still justified, and what evidence is required [10]. These questions can change as device firmware, vendors, services, or applicable rules change [13].")
    add_figure_image(doc, "Fig 03 IoT Privacy Compliance Challenge Landscape.png", "Fig. 3. IoT Privacy Compliance Challenge Landscape")
    
    t2_headers = ["Challenge", "Observed gap in typical approaches", "Design response"]
    t2_data = [
        ["Device heterogeneity", "Schemas, identity, capabilities, and update models vary.", "Device registry, schema validation, capability-aware controls."],
        ["Purpose and consent", "Policy information may not travel with events.", "Purpose tags, consent evidence, policy version, ownership metadata."],
        ["Risk prioritization", "Static checks can miss changing event patterns.", "AI risk signals alongside explicit deterministic rules."],
        ["Explainability", "Model output may not be actionable for reviewers.", "Reason codes, feature summaries, model version, review workflow."],
        ["Distributed governance", "Centralized collection can increase exposure.", "Edge filtering, data minimization, controlled evidence transfer."],
        ["Validation quality", "Synthetic or narrow datasets limit generalization.", "Data provenance, label protocol, held-out and independent tests."]
    ]
    create_table(doc, t2_headers, t2_data, [1.5, 2.5, 2.4])

    # Section 3
    style_heading(doc, "3. Background and Literature Review", level=1)
    add_body_p(doc, "Recent literature shows several strands that are individually mature enough to inform a combined design, but they are often evaluated with different assumptions [1]. Giordano, Palomba, and Ferrucci review AI techniques used to detect or prevent privacy problems in IoT systems and identify recurring concerns about use-case clarity and evaluation design [2]. Rodríguez, Otero, and Canal survey machine-learning and deep-learning approaches for IoT privacy protection, covering threat detection and privacy-supporting methods [1]. These reviews support the idea that AI can assist privacy management, but they also caution against assuming that a high classification score automatically proves privacy protection [1][70][71].")
    add_figure_image(doc, "Fig 04 Literature Taxonomy Framework.png", "Fig. 4. Literature Taxonomy Framework")

    t3_headers = ["Approach", "Useful strengths", "Main limitations", "Role in proposed framework"]
    t3_data = [
        ["Manual audit / checklist", "Transparent and easy to inspect.", "Periodic, labour-intensive, may miss changing patterns.", "Baseline and mandatory control checks."],
        ["Rule-based engine", "Deterministic, testable, auditable.", "Requires explicit rules and maintenance.", "Enforcement of hard constraints."],
        ["Supervised ML", "Can rank complex patterns at scale.", "Depends on labels; may drift or be biased.", "Prioritize candidate risk for review."],
        ["Edge governance", "Limits raw-data transfers and latency.", "Device constraints and distributed operations.", "Local validation and minimization."],
        ["Federated learning", "Can train across sites without pooling raw records.", "Updates can leak information and be poisoned.", "Optional where multiple data owners justify it."],
        ["Differential privacy", "Formal bounds for defined releases.", "Utility loss and privacy-budget accounting.", "Optional statistical-release safeguard."],
        ["Explainable AI", "Can make model output reviewable.", "Explanations can be incomplete or leak data.", "Reason summaries plus audit evidence."]
    ]
    create_table(doc, t3_headers, t3_data, [1.4, 1.8, 1.8, 1.4])

    # Section 4
    style_heading(doc, "4. Requirements Analysis for AI-Driven Privacy Compliance", level=1)
    add_body_p(doc, "Requirements are divided into functional controls and quality attributes [4]. Functional requirements state what the system must do: discover devices, authenticate event sources, attach data sensitivity metadata, resolve the declared purpose, check authorization and consent evidence, identify retention exceptions, score privacy risk, select a response, preserve an audit trail, and route uncertain cases to a responsible reviewer [9]. Non-functional requirements describe how the controls should behave: low latency at the edge, interoperability across protocols, availability during network interruption, least-privilege access, explainability, traceability, configuration safety, scalability, and maintainability [10].")
    add_figure_image(doc, "Fig 05 Requirements Engineering Framework.png", "Fig. 5. Requirements Engineering Framework")

    t4_headers = ["ID", "Requirement", "Verification evidence"]
    t4_data = [
        ["F1", "Register device identity, owner, type, firmware, and capabilities.", "Registry tests; unique device identifier."],
        ["F2", "Classify data by sensitivity, purpose, subject, retention, and location.", "Schema tests; completeness report."],
        ["F3", "Evaluate mandatory policy rules before transfer or reuse.", "Positive and negative rule test suite."],
        ["F4", "Estimate risk and return an explanation and uncertainty indicator.", "Held-out metrics; reviewer usability test."],
        ["F5", "Log decision, policy version, model version, and override.", "Tamper-evident audit sample."],
        ["NF1", "Minimize raw-data transfer and access.", "Field transfer inventory; access review."],
        ["NF2", "Protect integrity, availability, and credentials.", "Threat model, penetration tests, recovery test."],
        ["NF3", "Support heterogeneous schemas and limited edge capacity.", "Cross-device integration and latency tests."],
        ["NF4", "Make the system governable and accountable.", "Named owners, change log, escalation and appeal path."]
    ]
    create_table(doc, t4_headers, t4_data, [0.8, 3.2, 2.4])

    # Section 5
    style_heading(doc, "5. AI-Driven Privacy Compliance Architecture", level=1)
    add_body_p(doc, "The proposed architecture uses the edge as the first privacy decision point and the cloud or central governance service as the location for shared policy management, analytics, and controlled reporting [4]. A device registry identifies endpoints and records their technical capabilities [8]. The acquisition layer validates event structure and attaches metadata [10]. The classification layer estimates sensitivity and purpose context using known schemas and, where suitable, a model [4]. The edge governance layer enforces local restrictions before raw information leaves the local domain [8]. The AI risk layer adds an alert score for uncertain patterns [10]. A policy engine combines that score with explicit rules and chooses to allow, minimize, mask, delay, or block processing [4]. A governance service stores audit records, policy versions, and approved evidence [8].")
    add_figure_image(doc, "Fig 06 AI-Driven Privacy Compliance Architecture for Heterogeneous IoT Environments.png", "Fig. 6. AI-Driven Privacy Compliance Architecture for Heterogeneous IoT Environments")
    add_figure_image(doc, "Fig 07 Multi-Layer Compliance Framework.png", "Fig. 7. Multi-Layer Compliance Framework")

    # Section 6
    style_heading(doc, "6. IoT Data Acquisition and Classification Layer", level=1)
    add_body_p(doc, "A compliance decision is only as reliable as the context attached to an event [4]. The acquisition layer accepts data from devices and gateways through approved adapters and verifies source identity, timestamp, schema, firmware or device profile, and integrity metadata [9]. Unknown devices or malformed messages should be quarantined and recorded rather than merged into the trusted stream [36]. The adapter should normalize common fields while preserving the provenance of the original values, because conversion errors can affect downstream decisions [4].")
    add_figure_image(doc, "Fig 08 IoT Data Acquisition Framework.png", "Fig. 8. IoT Data Acquisition Framework")

    t5_headers = ["Class", "Example fields", "Default handling guidance"]
    t5_data = [
        ["Low sensitivity", "Device health, non-identifying aggregate status.", "Purpose tag, integrity check, retention limit."],
        ["Personal", "Pseudonymous identifier, location history, usage pattern.", "Purpose and authority check, minimization, access logging."],
        ["Sensitive / special category", "Health-related measurements or other legally protected data.", "Strong access control, encryption, restricted exports, enhanced review."],
        ["Security telemetry", "Failed login, firmware hash, network anomaly.", "Limit identifiers; restrict security purpose and retention."],
        ["Derived inference", "Risk profile, inferred occupancy, predicted condition.", "Record lineage and model; assess inference and re-identification risk."],
        ["Unknown / incomplete", "Missing owner, unclear purpose, invalid schema.", "Quarantine or block transfer pending review; do not assume low risk."]
    ]
    create_table(doc, t5_headers, t5_data, [1.5, 2.3, 2.6])

    # Section 7
    style_heading(doc, "7. Edge Intelligence and Local Governance Layer", level=1)
    add_body_p(doc, "Edge governance places privacy checks near the source, reducing the need to transmit raw records to a central cloud [4]. It can apply local filtering, aggregate values, remove direct identifiers, encrypt approved outputs, and block a transfer when the edge policy does not permit it [8]. The same gateway can monitor device security state, software versions, unusual access, message rate, and local data flows [9]. Edge placement is not inherently trustworthy: gateways may have limited resources, weak physical protection, vendor-specific management tools, and intermittent connectivity [4].")
    add_figure_image(doc, "Fig 09 Edge Governance Architecture.png", "Fig. 9. Edge Governance Architecture")
    add_figure_image(doc, "Fig 10 Edge Compliance Monitoring Workflow.png", "Fig. 10. Edge Compliance Monitoring Workflow")

    # Section 8
    style_heading(doc, "8. AI-Powered Privacy Risk Assessment Layer", level=1)
    add_body_p(doc, "The risk assessment layer estimates which events require more attention [1]. Its inputs may include sensitivity, consent or authority evidence, purpose alignment, retention status, encryption, access anomalies, transfer context, device security, data minimization, metadata quality, and recent threat signals [2]. This report uses a transparent composite risk formula as an explanation aid [1]:")
    
    p_eq1 = doc.add_paragraph()
    p_eq1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_eq1 = p_eq1.add_run("R_i = \u2211_j w_j \u00b7 x_ij;    where \u2211_j w_j = 1        (1)")
    r_eq1.font.name = 'Times New Roman'
    r_eq1.font.bold = True
    r_eq1.font.size = Pt(11)

    add_figure_image(doc, "Fig 11 AI Privacy Risk Assessment Framework.png", "Fig. 11. AI Privacy Risk Assessment Framework")
    add_figure_image(doc, "Fig 12 Risk Prediction Pipeline.png", "Fig. 12. Risk Prediction Pipeline")

    # Section 9
    style_heading(doc, "9. Automated Compliance and Policy Enforcement Layer", level=1)
    add_body_p(doc, "The compliance engine turns an approved policy into a decision for a specific event or data flow [2]. Policies are expressed as conditions over subject or asset class, purpose, sensitivity, recipient, legal basis or authorization evidence, retention, transfer location, and required protection [34]. In practice, policy rules should be expressed in a declarative format and separated from application code [37].")
    add_figure_image(doc, "Fig 13 Compliance Automation Workflow.png", "Fig. 13. Compliance Automation Workflow")
    add_figure_image(doc, "Fig 14 Policy Enforcement Lifecycle.png", "Fig. 14. Policy Enforcement Lifecycle")

    t6_headers = ["Rule ID", "Example condition", "Suggested action", "Evidence"]
    t6_data = [
        ["R-01", "Required consent/authority evidence missing.", "Hold affected processing and request review.", "Policy version, event ID, reason code."],
        ["R-02", "Requested purpose does not match approved purpose.", "Deny or route for approved exception.", "Purpose tags and rule result."],
        ["R-03", "Sensitive field lacks required encryption.", "Block export; remediate configuration.", "Transport/storage status and timestamp."],
        ["R-04", "Retention period has expired.", "Trigger deletion workflow and verify downstream copies.", "Deletion confirmation and exception log."],
        ["R-05", "Cross-border recipient/location not mapped.", "Hold transfer for jurisdictional review.", "Destination, legal mapping, owner approval."],
        ["R-06", "Model predicts unusual access pattern.", "Create alert for human triage; do not infer legal breach alone.", "Risk score, factors, reviewer outcome."],
        ["R-07", "Device identity or signature fails.", "Reject message and initiate security response.", "Certificate/signature result, incident ID."],
        ["R-08", "Metadata are incomplete or contradictory.", "Quarantine event until corrected.", "Schema version and missing fields."]
    ]
    create_table(doc, t6_headers, t6_data, [0.8, 2.0, 1.8, 1.8])

    # Section 10
    style_heading(doc, "10. Privacy Preservation and Data Protection Layer", level=1)
    add_body_p(doc, "Privacy protection is a set of complementary controls rather than a single algorithm [7]. Data minimization limits collection and disclosure to what the purpose requires [12]. Pseudonymization replaces direct identifiers with controlled identifiers but does not guarantee that a person cannot be reidentified [18]. Encryption protects confidentiality when keys and endpoints are managed correctly [19]. Access control enforces least privilege [7]. Differential privacy provides formal output bounds under Laplace noise (Equation 2), while federated model aggregation is expressed conceptually in Equation 3:")
    
    p_eq2 = doc.add_paragraph()
    p_eq2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_eq2 = p_eq2.add_run("M(x) = f(x) + Lap(\u0394f / \u03b5)        (2)")
    r_eq2.font.bold = True
    
    p_eq3 = doc.add_paragraph()
    p_eq3.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_eq3 = p_eq3.add_run("w_{t+1} = \u2211_k (n_k / N) \u00b7 w_{t+1}^k        (3)")
    r_eq3.font.bold = True

    add_figure_image(doc, "Fig 15 Privacy Protection Framework.png", "Fig. 15. Privacy Protection Framework")
    add_figure_image(doc, "Fig 16 Data Protection Lifecycle.png", "Fig. 16. Data Protection Lifecycle")

    # Section 11
    style_heading(doc, "11. Explainability, Transparency, and Auditability Layer", level=1)
    add_body_p(doc, "Explainability is essential when an AI-generated signal changes how data are collected, shared, retained, or investigated [3]. In a compliance setting, the explanation should answer four questions: what was detected; which input evidence supported the result; which policy or control was relevant; and what action followed [14].")
    add_figure_image(doc, "Fig 17 Explainable Compliance Framework.png", "Fig. 17. Explainable Compliance Framework")
    add_figure_image(doc, "Fig 18 Auditability and Transparency Dashboard.png", "Fig. 18. Auditability and Transparency Dashboard")

    # Section 12
    style_heading(doc, "12. Governance, Regulatory Mapping, and Data Sovereignty Layer", level=1)
    add_body_p(doc, "Regulatory mapping starts with scope [29]. The organization identifies its role, the people or entities represented in the data, the processing purposes, the destinations, the vendors, and the locations in which data are collected, stored, accessed, or transferred [34]. The GDPR, India's DPDP Act 2023 along with the DPDP Rules 2025, and the EU AI Act (Regulation 2024/1689) provide the baseline governance structure.")
    add_figure_image(doc, "Fig 19 Regulatory Compliance Architecture.png", "Fig. 19. Regulatory Compliance Architecture")

    t7_headers = ["Governance theme", "Technical control examples", "Evidence to retain", "Important limitation"]
    t7_data = [
        ["Purpose and transparency", "Purpose tags, notice/version register.", "Approved purpose, notice version, owner.", "Exact duty depends on context and law."],
        ["Lawful basis / consent", "Consent status, authority records, withdrawal workflow.", "Source of authority and timestamp.", "Consent is not the only possible lawful basis."],
        ["Data minimization", "Field allowlists, edge filtering, aggregation.", "Before/after schema and export records.", "A privacy risk assessment is still required."],
        ["Security & accountability", "Access controls, encryption, incident log, reviews.", "Test reports, role review, incident records.", "A technical control alone does not prove compliance."],
        ["Retention & individual rights", "Retention schedule, deletion orchestration, request handling.", "Completion evidence, exceptions and deadlines.", "Backups and third parties require separate handling."],
        ["AI governance", "Model cards, testing, human oversight, version change control.", "Validation, monitoring, reasons, override records.", "Regulatory applicability must be assessed individually."],
        ["Data sovereignty / transfers", "Location tags, recipient inventory, transfer review.", "Processing locations, contract and approval evidence.", "Cross-border requirements differ by jurisdiction."]
    ]
    create_table(doc, t7_headers, t7_data, [1.4, 1.8, 1.8, 1.4])

    # Section 13
    style_heading(doc, "13. Security and Threat Intelligence Layer", level=1)
    add_body_p(doc, "Privacy compliance depends on security controls because an organization cannot reliably enforce data-use policies if device identities, gateways, models, or logs can be manipulated [36]. Threats include unauthorized access, credential theft, insecure interfaces, stale software, data poisoning, model evasion, inference leakage, compromised gateways, and malicious insiders [36].")
    add_figure_image(doc, "Fig 20 Security Intelligence Framework.png", "Fig. 20. Security Intelligence Framework")

    t8_headers = ["Threat", "Potential privacy impact", "Prevention / detection", "Response evidence"]
    t8_data = [
        ["Spoofed device", "False provenance; unauthorized data injection.", "Mutual authentication, device attestation.", "Identity event and quarantine log."],
        ["Unauthorized access", "Disclosure or unapproved reuse.", "Least privilege, MFA for operators, access monitoring.", "Access log and revocation record."],
        ["Model evasion / poisoning", "Poor or manipulated risk ranking.", "Input validation, robust evaluation, update approval.", "Model version, detection event, rollback proof."],
        ["Data exfiltration", "Unapproved transfer of personal or sensitive data.", "Egress controls, minimization, encryption.", "Flow logs, incident timeline."],
        ["Insider misuse", "Access beyond assigned purpose.", "Separation of duties, reviewable exceptions.", "Authorization trail, investigation outcome."],
        ["Audit-log tampering", "Reduced ability to reconstruct decisions.", "Append-only storage, signatures, time synchronization.", "Integrity verification result."],
        ["Ransomware / outage", "Data loss, unavailable governance controls.", "Patch, backup, recovery drills, segmentation.", "Recovery record and residual risk."]
    ]
    create_table(doc, t8_headers, t8_data, [1.4, 1.8, 1.8, 1.4])

    # Section 14
    style_heading(doc, "14. Experimental Setup", level=1)
    add_body_p(doc, "A reproducible experiment is included to show how the proposed decision pipeline can be implemented and compared [14]. It generates 6,000 synthetic IoT event records across healthcare, smart city, manufacturing, energy, agriculture, and transport [36]. Each row contains artificial values for sensitivity level, consent evidence, encryption, purpose matching, retention, access anomalies, cross-border transfer, minimization, device security, metadata completeness, data volume, edge processing, and a synthetic violation label [14]. The records are split 75/25 with random seed 42 (1,500 held-out test events).")
    add_figure_image(doc, "Fig 21 Experimental Testbed Architecture.png", "Fig. 21. Experimental Testbed Architecture")

    t9_headers = ["Item", "Configuration", "Interpretation"]
    t9_data = [
        ["Dataset", "6,000 generated synthetic records; six IoT sectors.", "No real persons, devices, or production logs."],
        ["Generation seed", "42.", "Makes the artificial event generation reproducible."],
        ["Target label", "Generated by scripted risk-factor logic with noise.", "Not a legal finding or independently adjudicated label."],
        ["Split", "Stratified 75% training / 25% test.", "1,500 held-out records for reported comparison."],
        ["Baseline", "Transparent checklist rule.", "Deterministic comparison, not industry benchmark."],
        ["ML model", "Random Forest classifier (240 trees, depth 10, min leaf 3).", "Trained only on synthetic feature/label relationships."],
        ["Hybrid", "Rules and model signal combined with recall threshold 0.38.", "Intentionally trades precision for recall."],
        ["Reproducibility", "Python script, requirements, CSV, JSON metrics, predictions.", "Run instructions are in source_code/README.md."],
        ["Excluded", "Live gateway, clinical data, production audit.", "Future validation work is required."]
    ]
    create_table(doc, t9_headers, t9_data, [1.2, 2.5, 2.7])

    # Section 15
    style_heading(doc, "15. Evaluation Metrics", level=1)
    add_body_p(doc, "Equations (4)–(9) define the classification and control-coverage measures used in this report:")
    
    eqs = [
        "Precision = TP / (TP + FP)        (4)",
        "Recall = TP / (TP + FN)        (5)",
        "F1 = 2 \u00b7 (Precision \u00b7 Recall) / (Precision + Recall)        (6)",
        "Accuracy = (TP + TN) / (TP + TN + FP + FN)        (7)",
        "Coverage (%) = 100 \u00b7 (N_v / N_e)        (8)",
        "ROI (%) = 100 \u00b7 (Benefits - Costs) / Costs        (9)"
    ]
    for eq in eqs:
        p_e = doc.add_paragraph()
        p_e.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_e = p_e.add_run(eq)
        r_e.font.bold = True
        r_e.font.size = Pt(10.5)

    add_figure_image(doc, "Fig 22 Evaluation Framework.png", "Fig. 22. Evaluation Framework")

    t10_headers = ["Metric", "Definition / purpose", "Caution"]
    t10_data = [
        ["Accuracy", "Correct classifications divided by all evaluated examples.", "Can hide poor performance on a minority class."],
        ["Precision", "True positives divided by all predicted positives.", "Low precision means more false alerts."],
        ["Recall", "True positives divided by all actual positives.", "Low recall means more missed synthetic positives."],
        ["F1", "Harmonic mean of precision and recall.", "Does not encode the consequence of every error."],
        ["ROC-AUC", "Ranking performance over thresholds.", "Depends on target labels and sampling design."],
        ["Control coverage", "Share of synthetic records with a control flag.", "Proxy only; does not prove effective operation."],
        ["Operational latency", "Time from event to actionable decision.", "Not measured in this dataset-only experiment."]
    ]
    create_table(doc, t10_headers, t10_data, [1.4, 2.6, 2.4])

    # Section 16
    style_heading(doc, "16. Results and Findings", level=1)
    add_body_p(doc, "On the synthetic held-out test split of 1,500 events, the checklist baseline achieves 66.40% accuracy, 71.37% precision, 29.02% recall, and an F1 score of 0.413. The Random Forest classifier achieves 68.73% accuracy, 61.58% precision, 61.48% recall, and an F1 score of 0.615 with an ROC-AUC of 0.742. The hybrid rules-plus-AI detector achieves 64.27% accuracy, 54.13% precision, 79.51% recall, and F1 of 0.644 [1].")
    add_figure_image(doc, "Fig 23 Compliance Accuracy Performance Analysis (synthetic benchmark).png", "Fig. 23. Compliance Accuracy Performance Analysis (synthetic benchmark)")
    add_figure_image(doc, "Fig 24 Privacy-Preservation Control Indicators (synthetic proxy measures only).png", "Fig. 24. Privacy-Preservation Control Indicators (synthetic proxy measures only)")
    add_figure_image(doc, "Fig 25 Governance Maturity and Compliance Assessment (conceptual rubric).png", "Fig. 25. Governance Maturity and Compliance Assessment (conceptual rubric)")

    t11_headers = ["Method", "Accuracy", "Precision", "Recall", "F1", "ROC-AUC"]
    t11_data = [
        ["Checklist baseline", "0.6640", "0.7137", "0.2902", "0.4126", "Not calculated"],
        ["Random Forest", "0.6873", "0.6158", "0.6148", "0.6153", "0.7423"],
        ["Hybrid rules + AI", "0.6427", "0.5413", "0.7951", "0.6441", "0.7405"]
    ]
    create_table(doc, t11_headers, t11_data, [1.8, 0.9, 0.9, 0.9, 0.9, 1.0])

    # Section 17
    style_heading(doc, "17. Comparative Analysis", level=1)
    add_body_p(doc, "The checklist, stand-alone classifier, and hybrid design serve different operational roles [1]. A deterministic checklist is simple to explain and can enforce rules that are clearly defined in policy [2]. Its weakness is coverage: a small set of hand-authored conditions misses combinations not anticipated by its authors [3]. The Random Forest learns feature interactions, while the hybrid combines explicit hard rules with a broader detection signal, prioritizing recall.")
    add_figure_image(doc, "Fig 26 Comparative Benchmark Analysis (synthetic benchmark).png", "Fig. 26. Comparative Benchmark Analysis (synthetic benchmark)")

    t12_headers = ["Comparison", "Best result in this run", "Trade-off", "Use implication"]
    t12_data = [
        ["Accuracy", "Random Forest: 68.73%", "Lowest error rate overall among the three.", "Could be preferable when balanced errors matter."],
        ["Precision", "Checklist: 71.37%", "Lower recall: 29.02%.", "Fewer false alerts but misses more positives."],
        ["Recall", "Hybrid: 79.51%", "Precision 54.13%; accuracy 64.27%.", "May be useful for triage when missed alerts are costly."],
        ["F1", "Hybrid: 0.644", "Synthetic label design drives score.", "A prioritization view, not proof of compliance."],
        ["ROC-AUC", "Random Forest: 0.742; hybrid: 0.740", "Scores close under synthetic setup.", "No claim about production generalization."]
    ]
    create_table(doc, t12_headers, t12_data, [1.2, 1.8, 1.8, 1.6])

    # Section 18
    style_heading(doc, "18. Trustworthiness, Accountability, and Governance Assessment", level=1)
    add_body_p(doc, "Trustworthiness requires the system to be accurate enough for its intended use, robust to known attacks, secure, explainable, privacy-aware, and governed by accountable people [3]. Table 13 maps each dimension to concrete verification evidence.")
    add_figure_image(doc, "Fig 27 Governance Maturity Framework.png", "Fig. 27. Governance Maturity Framework")

    t13_headers = ["Dimension", "Question to assess", "Evidence required before deployment"]
    t13_data = [
        ["Fairness", "Do error rates differ by device, sector, or population?", "Subgroup metrics and a justified remediation plan."],
        ["Transparency", "Can reviewers understand what the system did?", "Accessible reasons and traceable model/policy version."],
        ["Accountability", "Who approves rules and handles appeals?", "Named owner, override record, escalation route."],
        ["Privacy", "Does the system collect and reveal only what is needed?", "Data-flow review, minimization test, disclosure analysis."],
        ["Robustness", "Does performance hold under missing fields or attacks?", "Adversarial, drift, and fault-injection testing."],
        ["Safety & proportionality", "Could blocking or delay harm essential services?", "Risk analysis, fallback modes, incident procedures."],
        ["Governance maturity", "Are policies, roles, reviews and evidence repeatable?", "Documented cycle, periodic review, audit sampling."]
    ]
    create_table(doc, t13_headers, t13_data, [1.4, 2.5, 2.5])

    # Section 19
    style_heading(doc, "19. Industry Use Cases and Case Study Evaluation", level=1)
    add_body_p(doc, "Table 14 details domain-specific governance profiles across six major IoT sectors:")
    add_figure_image(doc, "Fig 28 Smart City Compliance Ecosystem.png", "Fig. 28. Smart City Compliance Ecosystem")
    add_figure_image(doc, "Fig 29 Healthcare IoT Governance Framework.png", "Fig. 29. Healthcare IoT Governance Framework")

    t14_headers = ["Sector", "Potential data / risk", "Candidate AI-assisted control", "Human governance point"]
    t14_data = [
        ["Healthcare IoT", "Vitals, device identifiers, access events.", "Local filtering, sensitivity classification, unusual access alert.", "Clinical safety and lawful processing review."],
        ["Smart cities", "Mobility, cameras, environmental measurements.", "Purpose/retention checks; aggregate where possible.", "Public notice, proportionality, public accountability."],
        ["Manufacturing", "Machine telemetry, worker-linked events.", "Edge inference, role-based access, export control.", "Safety, labour, and vendor contract review."],
        ["Energy", "Smart meter records and control telemetry.", "Anomaly detection and privacy-preserving aggregation.", "Critical-infrastructure security review."],
        ["Agriculture", "Soil, yield, location, farm operations.", "Local aggregation and sharing control.", "Ownership and commercial confidentiality review."],
        ["Transport / logistics", "Vehicle location, routes, driver behaviour.", "Retention control and restricted location access.", "Worker impact, safety, and cross-border review."]
    ]
    create_table(doc, t14_headers, t14_data, [1.3, 1.8, 1.8, 1.5])

    # Section 20
    style_heading(doc, "20. Business Impact Assessment", level=1)
    add_body_p(doc, "AI-assisted compliance may create business value by detecting candidate problems earlier, reducing repetitive checklist work, and improving policy consistency [2]. However, financial return must be measured through pilot studies rather than assumed. Table 15 provides a cost-benefit worksheet for planning future deployments.")
    add_figure_image(doc, "Fig 30 Control-Coverage Dashboard (synthetic indicators not a financial ROI result).png", "Fig. 30. Control-Coverage Dashboard (synthetic indicators; not a financial ROI result)")

    t15_headers = ["Item", "How to measure it", "Evidence needed"]
    t15_data = [
        ["Manual review time", "Hours per 1,000 events before and after.", "Time study with comparable samples."],
        ["Triage speed", "Median time from event to reviewer decision.", "Time-stamped event and case records."],
        ["Alert quality", "Precision, recall, reversals, reviewer acceptance.", "Independent labels and adjudication."],
        ["Data minimization", "Fields withheld or aggregated before export.", "Data-flow measurements and schema diff."],
        ["Operating cost", "Compute, storage, staffing, maintenance, legal review.", "Invoices, workload, staffing and support records."],
        ["Risk/cost of errors", "Costs of missed issue and false alert.", "Incident scenarios and domain-owner estimates."],
        ["ROI", "(Verified benefits minus verified costs) / costs.", "Measured financial inputs and defined time horizon."],
        ["Current study status", "No monetary outcome measured.", "Synthetic dataset contains no financial observations."]
    ]
    create_table(doc, t15_headers, t15_data, [1.6, 2.5, 2.3])

    # Section 21
    style_heading(doc, "21. Challenges and Limitations", level=1)
    add_body_p(doc, "Several limitations constrain the proposed framework [1]. First, legal duties are contextual, and a generic architecture cannot automatically resolve the applicability of the GDPR, DPDP Act, AI Act, or sector rules [3]. Second, heterogeneous devices can have incomplete metadata and weak hardware support [4]. Third, AI models can drift, be manipulated, or produce different error rates across device classes [13]. Fourth, synthetic benchmarks demonstrate workflow reproducibility only and do not establish real-world compliance effectiveness.")
    add_figure_image(doc, "Fig 31 Challenges and Limitations Roadmap.png", "Fig. 31. Challenges and Limitations Roadmap")

    # Section 22
    style_heading(doc, "22. Future Research Directions", level=1)
    add_body_p(doc, "Future research directions include multi-site validation with consented real-world data, rigorous privacy-budget accounting for differential privacy, robust federated learning with poisoning defenses, and human-factors studies to evaluate reviewer cognitive load.")
    add_figure_image(doc, "Fig 32 Future Research Roadmap.png", "Fig. 32. Future Research Roadmap")
    add_figure_image(doc, "Fig 33 Next-Generation AI Governance Ecosystem.png", "Fig. 33. Next-Generation AI Governance Ecosystem")

    # Section 23
    style_heading(doc, "23. Conclusion", level=1)
    add_body_p(doc, "This case study presents a layered approach to AI-driven privacy compliance in IoT environments with different devices [1]. The main design principle is to combine explicit and testable policy rules with local processing, risk detection, explainable outcomes, evidence capture, regulatory mapping, and human oversight [3]. Device diversity, fragmented policies, contextual risk, and distributed data flows require more than a single model or centralized dashboard [4]. Edge controls can minimize unnecessary transfer, while a shared governance layer keeps policy versions, model versions, and audit evidence aligned [10].")
    add_body_p(doc, "A small reproducible benchmark shows the implementation path using 6,000 synthetic events [1]. On the 1,500-record held-out split, the hybrid detector produced the highest recall (79.51%) and F1 score (0.644), but lower accuracy (64.27%) and precision (54.13%) than the Random Forest model [3]. These figures show an alerting trade-off under the artificial generator [4]. They do not establish real-world compliance effectiveness or prove that any regulation has been satisfied [1].")
    add_figure_image(doc, "Fig 34 Research Contribution Framework.png", "Fig. 34. Research Contribution Framework")

    # Data Availability Statement
    style_heading(doc, "Data Availability Statement", level=2)
    add_body_p(doc, "All data generated or analysed during this study are included in this published article [and its supplementary information files: iot_privacy_compliance_dataset.csv, train_set.csv, and test_set.csv located in the datasets/ folder of the project repository]. The benchmark data are synthetic and were generated for this case study. Source code, dataset generator, and random seed (42) are included in the source-code folder.")

    doc.add_page_break()

    # -------------------------------------------------------------
    # Appendices A through O
    # -------------------------------------------------------------
    style_heading(doc, "Appendices", level=1)
    appendices = [
        ("Appendix A. Policy Rule Template", "Provides declarative JSON specifications for policy rule PRIV-IOT-EX-01, defining condition triggers, mandatory actions, and evidence fields."),
        ("Appendix B. Reference Pseudocode for the Event Pipeline", "Details process_event(event) sequentially validating schema, authenticating device ID, checking cache policy, classifying sensitivity, running deterministic rules, applying edge minimization, computing AI risk score, and writing tamper-evident SHA-256 audit records."),
        ("Appendix C. Event Data Dictionary", "Documents the complete schema of the event envelope: event_id, device_id, event_time, data_class, purpose_id, receiver_id, retention_class, policy_version, model_version, and risk_score."),
        ("Appendix D. Extended Test Cases and Expected Behaviour", "Outlines 12 rigorous positive and negative boundary test scenarios (D-01 to D-12) covering expired retention, purpose mismatch, offline policy cache, and audit failures."),
        ("Appendix E. Reproducibility and Deployment Checklist", "Checklist for experimental replication and production readiness gates covering device inventory, policy versioning, and rollback procedures."),
        ("Appendix F. Detailed Research Questions and Hypotheses", "Formulates RQ1–RQ4 and testable hypotheses H1–H5 on metadata preservation, hybrid decision support, and audit reconstruction."),
        ("Appendix G. Step-by-Step Experimental Protocol", "Detailed guide covering pre-test configuration, event set preparation, baseline execution, and error analysis."),
        ("Appendix H. Event Labels and Annotation Guide", "Defines operational criteria for permitted, violation, and uncertain event labels to prevent data leakage and label bias."),
        ("Appendix I. Policy Rule Examples and Review Checklist", "Provides concrete examples for healthcare wearables (Rule I.2) and smart-city traffic count aggregation (Rule I.3)."),
        ("Appendix J. Implementation and Deployment Readiness Plan", "Six-stage development plan moving from schema definition to offline recovery testing."),
        ("Appendix K. Risk Model Calibration and Sensitivity Protocol", "Outlines protocols for probability calibration, weight sensitivity testing, and subgroup evaluations."),
        ("Appendix L. Failure Mode and Effects Analysis (FMEA)", "Analyzes failure modes across identity, metadata, policy cache, model timeouts, and audit storage."),
        ("Appendix M. Privacy Impact Assessment (PIA) Checklist", "Structured questionnaire covering data necessity, proportionality, residual risk, and periodic re-assessment."),
        ("Appendix N. Experimental Result Reporting Template", "Standard reporting schema recording run IDs, configurations, confusion matrices, and plain-language interpretations."),
        ("Appendix O. Operations, Incident Response, and Recovery", "Operational protocols for daily monitoring, security containment, credential rotation, and post-incident lessons learned.")
    ]

    for title, desc in appendices:
        style_heading(doc, title, level=2)
        add_body_p(doc, desc)

    doc.add_page_break()

    # -------------------------------------------------------------
    # References (All 81 IEEE references)
    # -------------------------------------------------------------
    style_heading(doc, "References", level=1)
    
    # We will load and add the 81 references
    refs_text = [
        "[1] A. Rodríguez, B. Otero, and R. Canal, “A survey of machine and deep learning methods for privacy protection in the Internet of Things,” Sensors, vol. 23, no. 3, Art. no. 1252, 2023, doi: 10.3390/s23031252.",
        "[2] G. Giordano, F. Palomba, and F. Ferrucci, “On the use of artificial intelligence to deal with privacy in IoT systems: A systematic literature review,” Journal of Systems and Software, vol. 193, Art. no. 111475, 2022, doi: 10.1016/j.jss.2022.111475.",
        "[3] I. Kok, F. Y. Okay, O. Muyanli, and S. Ozdemir, “Explainable artificial intelligence (XAI) for Internet of Things: A survey,” IEEE Internet of Things Journal, vol. 10, no. 16, pp. 14764–14779, 2023, doi: 10.1109/JIOT.2023.3287678.",
        "[4] A. Alwarafy, K. A. Al-Thelaya, M. Abdallah, J. Schneider, and M. Hamdi, “A survey on security and privacy issues in edge-computing-assisted Internet of Things,” IEEE Internet of Things Journal, vol. 8, no. 6, pp. 4004–4022, 2021, doi: 10.1109/JIOT.2020.3015432.",
        "[5] D. C. Nguyen, M. Ding, P. N. Pathirana, A. Seneviratne, J. Li, and H. V. Poor, “Federated learning for Internet of Things: A comprehensive survey,” IEEE Communications Surveys & Tutorials, vol. 23, no. 3, pp. 1622–1658, 2021, doi: 10.1109/COMST.2021.3075439.",
        "[6] T. Zhang, L. Gao, C. He, M. Zhang, B. Krishnamachari, and A. S. Avestimehr, “Federated learning for the Internet of Things: Applications, challenges, and opportunities,” IEEE Internet of Things Magazine, vol. 5, no. 1, pp. 24–29, 2022, doi: 10.1109/IOTM.004.2100182.",
        "[7] M. A. Husnoo, A. Anwar, R. K. Chakrabortty, R. Doss, and M. J. Ryan, “Differential privacy for IoT-enabled critical infrastructure: A comprehensive survey,” IEEE Access, vol. 9, pp. 153276–153304, 2021, doi: 10.1109/ACCESS.2021.3124309.",
        "[8] M. Laroui, B. Nour, H. Moungla, M. A. Cherif, H. Afifi, and M. Guizani, “Edge and fog computing for IoT: A survey on current research activities & future directions,” Computer Communications, vol. 180, pp. 210–231, 2021, doi: 10.1016/j.comcom.2021.09.003.",
        "[9] E. Fazeldehkordi and T.-M. Grønli, “A survey of security architectures for edge computing-based IoT,” IoT, vol. 3, no. 3, pp. 332–365, 2022, doi: 10.3390/iot3030019.",
        "[10] L. Kong et al., “Edge-computing-driven Internet of Things: A survey,” ACM Computing Surveys, vol. 55, no. 8, Art. no. 174, 2023, doi: 10.1145/3555308.",
        "[11] H. Li, L. Ge, and L. Tian, “Survey: Federated learning data security and privacy-preserving in edge-Internet of Things,” Artificial Intelligence Review, vol. 57, Art. no. 130, 2024, doi: 10.1007/s10462-024-10774-7.",
        "[12] D. T. Aga, R. Chintanippu, R. A. Mowri, and M. Siddula, “Exploring secure and private data aggregation techniques for the Internet of Things: A comprehensive review,” Discover Internet of Things, vol. 4, Art. no. 28, 2024, doi: 10.1007/s43926-024-00064-7.",
        "[13] S. F. Ahmed, M. S. B. Alam, S. Afrin, S. J. Rafa, S. B. Taher, M. Kabir, S. M. Muyeen, and A. H. Gandomi, “Toward a secure 5G-enabled Internet of Things: A survey on requirements, privacy, security, challenges, and opportunities,” IEEE Access, vol. 12, pp. 13125–13145, 2024, doi: 10.1109/ACCESS.2024.3352508.",
        "[14] M. Adam, M. Hammoudeh, R. Alrawashdeh, and B. Alsulaimy, “A survey on security, privacy, trust, and architectural challenges in IoT systems,” IEEE Access, vol. 12, pp. 57128–57149, 2024, doi: 10.1109/ACCESS.2024.3382709.",
        "[15] M. Venkatasubramanian, A. H. Lashkari, and S. Hakak, “IoT malware analysis using federated learning: A comprehensive survey,” IEEE Access, vol. 11, pp. 5004–5018, 2023, doi: 10.1109/ACCESS.2023.3235389.",
        "[16] H. C. Neto et al., “A survey on securing federated learning: Analysis of applications, attacks, challenges, and trends,” IEEE Access, vol. 11, pp. 41928–41953, 2023, doi: 10.1109/ACCESS.2023.3269980.",
        "[17] G. Xia, J. Chen, C. Yu, and J. Ma, “Poisoning attacks in federated learning: A survey,” IEEE Access, vol. 11, pp. 10708–10722, 2023, doi: 10.1109/ACCESS.2023.3238823.",
        "[18] Y. Zhao, J. Zhao, M. Yang et al., “Local differential privacy-based federated learning for Internet of Things,” IEEE Internet of Things Journal, vol. 8, no. 11, pp. 8836–8853, 2021, doi: 10.1109/JIOT.2020.3037194.",
        "[19] I. Zhou, F. Tofigh, M. Piccardi, M. Abolhasan, D. Franklin, and J. Lipman, “Secure multi-party computation for machine learning: A survey,” IEEE Access, vol. 12, pp. 53881–53899, 2024, doi: 10.1109/ACCESS.2024.3388992.",
        "[20] R. Yang, T. Zhao, F. R. Yu, M. Li, D. Zhang, and X. Zhao, “Blockchain-based federated learning with enhanced privacy and security using homomorphic encryption and reputation,” IEEE Internet of Things Journal, vol. 11, no. 12, pp. 21674–21688, 2024, doi: 10.1109/JIOT.2024.3379395.",
        "[21] S. Almutairi and A. Barnawi, “Federated learning vulnerabilities, threats and defenses: A systematic review and future directions,” Internet of Things, vol. 24, Art. no. 100947, 2023, doi: 10.1016/j.iot.2023.100947.",
        "[22] T. Li, X. He, S. Jiang, and J. Liu, “A survey of privacy-preserving offloading methods in mobile-edge computing,” Journal of Network and Computer Applications, vol. 203, Art. no. 103395, 2022, doi: 10.1016/j.jnca.2022.103395.",
        "[23] A. D. Kounoudes and G. M. Kapitsaki, “A mapping of IoT user-centric privacy preserving approaches to the GDPR,” Internet of Things, vol. 11, Art. no. 100179, 2020, doi: 10.1016/j.iot.2020.100179.",
        "[24] A. Vyas, S. Lin, J. Hwang, and N. Tripathi, “Privacy-preserving federated learning for intrusion detection in IoT environments: A survey,” IEEE Access, vol. 12, pp. 127018–127050, 2024, doi: 10.1109/ACCESS.2024.3454211.",
        "[25] T. M. M. Mengistu, T. Kim, and J.-W. Lin, “A survey on heterogeneity taxonomy, security and privacy preservation in the integration of IoT, wireless sensor networks and federated learning,” Sensors, vol. 24, no. 3, Art. no. 968, 2024, doi: 10.3390/s24030968.",
        "[26] Z. Xu and W. Liu, “Artificial intelligence for securing IoT services in edge computing: A survey,” Security and Communication Networks, vol. 2020, Art. no. 8872586, 2020, doi: 10.1155/2020/8872586.",
        "[27] A. Saleem et al., “A comprehensive systematic survey of IoT protocols: Implications for data quality and performance,” IEEE Access, vol. 13, pp. 196206–196235, 2024, doi: 10.1109/ACCESS.2024.3486927.",
        "[28] O. Ben Atia et al., “Securing federated learning in IoT: A survey of attacks, defenses, and frameworks,” IEEE Internet of Things Journal, vol. 12, no. 22, pp. 47163–47190, 2025, doi: 10.1109/JIOT.2025.3600617.",
        "[29] P. Naithani, “Analysis of India’s Digital Personal Data Protection Act, 2023,” International Journal of Law and Management, vol. 67, no. 5, pp. 543–553, 2024, doi: 10.1108/IJLMA-05-2024-0174.",
        "[30] M. U. Hassan, M. H. Rehmani, and J. Chen, “Differential privacy techniques for cyber physical systems: A survey,” IEEE Communications Surveys & Tutorials, vol. 22, no. 1, pp. 746–789, 2020, doi: 10.1109/COMST.2019.2944748.",
        "[31] O. Aouedi, T.-H. Vu, A. Sacco, D. C. Nguyen, K. Piamrat, G. Marchetto, and Q.-V. Pham, “A survey on intelligent Internet of Things: Applications, security, privacy, and future directions,” IEEE Communications Surveys & Tutorials, vol. 27, no. 2, pp. 1238–1292, 2025, doi: 10.1109/COMST.2024.3430368.",
        "[32] A. S. M. Kayes et al., “Safeguarding individuals and organizations from privacy breaches: A comprehensive review of problem domains, solution strategies, and prospective research directions,” IEEE Internet of Things Journal, vol. 12, no. 2, pp. 1247–1265, 2025, doi: 10.1109/JIOT.2024.3481316.",
        "[33] M. M. Ogonji, G. Okeyo, and J. M. Wafula, “A survey on privacy and security of Internet of Things,” Computer Science Review, vol. 38, Art. no. 100312, 2020, doi: 10.1016/j.cosrev.2020.100312.",
        "[34] K. Boeckl and N. Lefkovitz, NIST Privacy Framework: A Tool for Improving Privacy Through Enterprise Risk Management, Version 1.0, NIST CSWP 10, 2020, doi: 10.6028/NIST.CSWP.01162020.",
        "[35] National Institute of Standards and Technology, Artificial Intelligence Risk Management Framework (AI RMF 1.0), NIST AI 100-1, 2023, doi: 10.6028/NIST.AI.100-1.",
        "[36] M. J. Fagan, K. N. Megas, K. Scarfone, and M. Smith, IoT Device Cybersecurity Capability Core Baseline, NISTIR 8259A, 2020, doi: 10.6028/NIST.IR.8259A.",
        "[37] European Parliament and Council of the European Union, “Regulation (EU) 2016/679 (General Data Protection Regulation),” Official Journal of the European Union, 2016.",
        "[38] European Parliament and Council of the European Union, “Regulation (EU) 2024/1689 laying down harmonised rules on artificial intelligence (Artificial Intelligence Act),” Official Journal of the European Union, 2024.",
        "[39] Government of India, “Digital Personal Data Protection Act, 2023,” Act No. 22 of 2023, Gazette of India, 2023.",
        "[40] Ministry of Electronics and Information Technology, Government of India, “Digital Personal Data Protection Rules, 2025,” notified 14 November 2025, with corrigendum dated 16 December 2025.",
        "[41] Organisation for Economic Co-operation and Development, “OECD AI Principles,” updated 2024.",
        "[42] P. Sun, Y. Wan, Z. Wu, Z. Fang, and Q. Li, “A survey on privacy and security issues in IoT-based environments: Technologies, protection measures and future directions,” Computers & Security, vol. 148, Art. no. 104097, Jan. 2025, doi: 10.1016/j.cose.2024.104097.",
        "[43] A. Marengo, “Navigating the nexus of AI and IoT: A comprehensive review of data analytics and privacy paradigms,” Internet of Things, vol. 27, Art. no. 101318, Oct. 2024, doi: 10.1016/j.iot.2024.101318.",
        "[44] “Enhancing IoT privacy with artificial intelligence: Recent advances and future directions,” Internet of Things, vol. 34, Art. no. 101752, Nov. 2025.",
        "[45] J. Moss, J. Gordon, W. Duclos, Y. Liu, Q. Wang, and J. Wang, “Explainable AI in IoT: A survey of challenges, advancements, and pathways to trustworthy automation,” Electronics, vol. 14, no. 23, Art. no. 4622, 2025, doi: 10.3390/electronics14234622.",
        "[46] R. Kaur, T. Rodrigues, N. Kadir, and R. Kashef, “A survey on privacy preservation techniques in IoT systems,” Sensors, vol. 25, no. 22, Art. no. 6967, 2025, doi: 10.3390/s25226967.",
        "[47] M. Gheisari, G. Wang, and S. Chen, “An edge computing-enhanced Internet of Things framework for privacy-preserving in smart city,” Computers & Electrical Engineering, vol. 81, Art. no. 106504, 2020, doi: 10.1016/j.compeleceng.2019.106504.",
        "[48] V. Mothukuri, R. M. Parizi, S. Pouriyeh, Y. Huang, A. Dehghantanha, and G. Srivastava, “A survey on security and privacy of federated learning,” Future Generation Computer Systems, vol. 115, pp. 619–640, 2021, doi: 10.1016/j.future.2020.10.007.",
        "[49] F. Mosaiyebzadeh, S. Pouriyeh, R. M. Parizi, Q. Z. Sheng, M. Han, L. Zhao, G. Sannino, and D. M. Batista, “Privacy-enhancing technologies in federated learning for the Internet of Healthcare Things: A survey,” Electronics, vol. 12, no. 12, Art. no. 2703, 2023, doi: 10.3390/electronics12122703.",
        "[50] A. Coiduras-Sanagustín, E. Manchado-Pérez, and C. García-Hernández, “Understanding perspectives for product design on personal data privacy in Internet of Things (IoT): A systematic literature review,” Heliyon, vol. 10, no. 9, Art. no. e30357, 2024, doi: 10.1016/j.heliyon.2024.e30357.",
        "[51] S. Salim, N. Moustafa, and B. Turnbull, “Privacy preservation of Internet of Things-integrated social networks: A survey and future challenges,” International Journal of Web Information Systems, vol. 21, no. 4, pp. 372–431, 2025, doi: 10.1108/IJWIS-04-2024-0120.",
        "[52] M. H. Shirvani and M. Masdari, “A survey study on trust-based security in Internet of Things: Challenges and issues,” Internet of Things, vol. 21, Art. no. 100640, 2023, doi: 10.1016/j.iot.2022.100640.",
        "[53] A. Sharma, E. S. Pilli, A. P. Mazumdar, and P. Gera, “Towards trustworthy Internet of Things: A survey on trust management applications and schemes,” Computer Communications, vol. 160, pp. 475–493, 2020, doi: 10.1016/j.comcom.2020.06.030.",
        "[54] S. Alam, S. Zardari, S. Noor, S. Ahmed, and H. Mouratidis, “Trust management in Social Internet of Things (SIoT): A survey,” IEEE Access, vol. 10, pp. 108924–108954, 2022, doi: 10.1109/ACCESS.2022.3213699.",
        "[55] Z. Cheng, Y. Liu, C. Wu, Y. Pan, L. Zhao, X. Deng, and C. Zhu, “Decentralized IoT data sharing: A blockchain-based federated learning approach with joint optimizations for efficiency and privacy,” Future Generation Computer Systems, vol. 160, pp. 547–563, 2024, doi: 10.1016/j.future.2024.06.035.",
        "[56] Y. Shen, C. Shepherd, C. M. Ahmed, S. Shen, X. Wu, W. Ke, and S. Yu, “Game-theoretic analytics for privacy preservation in Internet of Things networks: A survey,” Engineering Applications of Artificial Intelligence, vol. 133, Art. no. 108449, 2024, doi: 10.1016/j.engappai.2024.108449.",
        "[57] G. Yang, “An overview of current solutions for privacy in the Internet of Things,” Frontiers in Artificial Intelligence, vol. 5, Art. no. 812732, 2022, doi: 10.3389/frai.2022.812732.",
        "[58] D. Li, Y. Zhao, Y. Wang, D. An, and Q. Yang, “The privacy-preserving auction mechanisms in IoT-based trading market: A survey,” Internet of Things, vol. 26, Art. no. 101178, 2024, doi: 10.1016/j.iot.2024.101178.",
        "[59] K. Park and Y. Park, “MIoT-CDPS: Complete decentralized privacy-preserving scheme for medical Internet of Things,” Internet of Things, vol. 27, Art. no. 101250, 2024, doi: 10.1016/j.iot.2024.101250.",
        "[60] I. Khan, Y. Majib, R. Ullah, and O. Rana, “Blockchain applications for Internet of Things—A survey,” Internet of Things, vol. 27, Art. no. 101254, 2024, doi: 10.1016/j.iot.2024.101254.",
        "[61] M. Aledhari, R. Razzak, R. M. Parizi, and F. Saeed, “Federated learning: A survey on enabling technologies, protocols, and applications,” IEEE Access, vol. 8, pp. 140699–140725, 2020, doi: 10.1109/ACCESS.2020.3013541.",
        "[62] W. Y. B. Lim et al., “Federated learning in mobile edge networks: A comprehensive survey,” IEEE Communications Surveys & Tutorials, vol. 22, no. 3, pp. 2031–2063, 2020, doi: 10.1109/COMST.2020.2986024.",
        "[63] M. Aggarwal, V. Khullar, S. Rani, T. A. Prola, S. B. Bhattacharjee, S. M. Shawon, and N. Goyal, “Federated learning on Internet of Things: Extensive and systematic review,” Computers, Materials & Continua, vol. 79, no. 2, pp. 1795–1834, 2024, doi: 10.32604/cmc.2024.049846.",
        "[64] S. K. Jain and N. Kesswani, “A noise-based privacy preserving model for Internet of Things,” Complex & Intelligent Systems, vol. 9, pp. 3655–3679, 2023, doi: 10.1007/s40747-021-00489-5.",
        "[65] O. G. Darley, A. A. Adenowo, and A. I. O. Yussuff, “Machine learning intrusion detection as a solution to security and privacy issues in IoT: A systematic review,” FUOYE Journal of Engineering and Technology, vol. 7, no. 2, pp. 148–156, 2022, doi: 10.46792/fuoyejet.v7i2.802.",
        "[66] M. A. S. Amin, S. Kim, M. A. S. A. Rishat, Z. Tang, and H. Ahn, “A systematic literature review of privacy information disclosure in AI-integrated Internet of Things technologies,” Sustainability, vol. 17, no. 1, Art. no. 8, 2025, doi: 10.3390/su17010008.",
        "[67] M. Aqeel, F. Ali, M. W. Iqbal, T. A. Rana, M. Arif, and M. R. Auwul, “A review of security and privacy concerns in the Internet of Things (IoT),” Journal of Sensors, vol. 2022, Art. no. 5724168, 2022, doi: 10.1155/2022/5724168.",
        "[68] R. Roman, P. Najera, and J. Lopez, “On the features and challenges of security and privacy in distributed Internet of Things,” Computer Networks, vol. 57, no. 10, pp. 2266–2279, 2013, doi: 10.1016/j.comnet.2013.04.018.",
        "[69] S. Sicari, A. Rizzardi, L. A. Grieco, and A. Coen-Porisini, “Security, privacy and trust in Internet of Things: The road ahead,” Computer Networks, vol. 76, pp. 146–164, 2015, doi: 10.1016/j.comnet.2014.11.008.",
        "[70] K. Ziegeldorf, O. Garcia Morchon, and K. Wehrle, “Privacy in the Internet of Things: Threats and challenges,” Security and Communication Networks, vol. 7, no. 12, pp. 2728–2742, 2014, doi: 10.1002/sec.795.",
        "[71] D. Miorandi, S. Sicari, F. De Pellegrini, and I. Chlamtac, “Internet of things: Vision, applications and research challenges,” Ad Hoc Networks, vol. 10, no. 7, pp. 1497–1516, 2012, doi: 10.1016/j.adhoc.2012.02.016.",
        "[72] W. Shi et al., “Edge computing: Vision and challenges,” IEEE Internet of Things Journal, vol. 3, no. 5, pp. 637–646, 2016, doi: 10.1109/JIOT.2016.2579198.",
        "[73] M. Satyanarayanan, “The emergence of edge computing,” Computer, vol. 50, no. 1, pp. 30–39, 2017, doi: 10.1109/MC.2017.9.",
        "[74] M. Whitmore, A. Agarwal, and L. Da Xu, “The Internet of Things—A survey of topics and trends,” Information Systems Frontiers, vol. 17, pp. 261–274, 2015, doi: 10.1007/s10796-014-9489-2.",
        "[75] L. Atzori, A. Iera, and G. Morabito, “The Internet of Things: A survey,” Computer Networks, vol. 54, no. 15, pp. 2787–2805, 2010, doi: 10.1016/j.comnet.2010.05.010.",
        "[76] U.S. Department of Health and Human Services, “The HIPAA Privacy Rule,” official guidance. Available: https://www.hhs.gov/hipaa/for-professionals/privacy/index.html.",
        "[77] C. Dwork and A. Roth, The Algorithmic Foundations of Differential Privacy. Hanover, MA, USA: Now Publishers, 2014, doi: 10.1561/0400000042.",
        "[78] K. Bonawitz et al., “Practical secure aggregation for privacy-preserving machine learning,” in Proc. ACM SIGSAC Conference on Computer and Communications Security, pp. 1175–1191, 2017, doi: 10.1145/3133956.3133982.",
        "[79] R. Shokri, M. Stronati, C. Song, and V. Shmatikov, “Membership inference attacks against machine learning models,” in Proc. IEEE Symposium on Security and Privacy, pp. 3–18, 2017, doi: 10.1109/SP.2017.41.",
        "[80] M. T. Ribeiro, S. Singh, and C. Guestrin, “Why should I trust you?: Explaining the predictions of any classifier,” in Proc. ACM SIGKDD Conference on Knowledge Discovery and Data Mining, pp. 1135–1144, 2016, doi: 10.1145/2939672.2939778.",
        "[81] E. Dritsas and M. Trigka, “Federated learning for IoT: A survey of techniques, challenges, and applications,” Journal of Sensor and Actuator Networks, vol. 14, no. 1, Art. no. 9, 2025, doi: 10.3390/jsan14010009."
    ]

    for ref in refs_text:
        add_body_p(doc, ref, space_after=3)

    out_file = os.path.join(MANUSCRIPT_DIR, "AI_Driven_Privacy_Compliance_in_Heterogeneous_IoT_Environments.docx")
    doc.save(out_file)
    print(f"Successfully assembled complete manuscript (.docx): {out_file}")

if __name__ == "__main__":
    build_full_manuscript()
