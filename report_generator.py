from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4

def generate_pdf(data):

    file_path = "AI_Resume_Report.pdf"
    doc = SimpleDocTemplate(file_path, pagesize=A4)
    elements = []

    styles = getSampleStyleSheet()
    normal_style = styles["Normal"]

    elements.append(Paragraph("<b>AI Resume Analysis Report</b>", styles["Title"]))
    elements.append(Spacer(1, 0.3 * inch))

    elements.append(Paragraph(f"<b>ATS Score:</b> {data['ats_score']}/100", normal_style))
    elements.append(Paragraph(f"<b>Resume Strength Score:</b> {data['resume_score']}/100", normal_style))
    elements.append(Spacer(1, 0.2 * inch))

    elements.append(Paragraph("<b>Detected Skills:</b>", normal_style))
    elements.append(Paragraph(", ".join(data["skills"]), normal_style))
    elements.append(Spacer(1, 0.2 * inch))

    elements.append(Paragraph("<b>Suitable Job Roles:</b>", normal_style))
    elements.append(Paragraph(", ".join(data["job_roles"]), normal_style))
    elements.append(Spacer(1, 0.2 * inch))

    elements.append(Paragraph("<b>Tasks Candidate Can Perform:</b>", normal_style))
    elements.append(Paragraph(", ".join(data["tasks"]), normal_style))
    elements.append(Spacer(1, 0.2 * inch))

    elements.append(Paragraph("<b>Career Recommendations:</b>", normal_style))
    elements.append(Paragraph(data["recommendations"], normal_style))

    doc.build(elements)

    return file_path
