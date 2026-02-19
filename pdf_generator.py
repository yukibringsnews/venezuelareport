from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Image
from reportlab.platypus import PageBreak
from reportlab.lib.pagesizes import A4
import os


def generate_pdf(report_text, filename="report.pdf"):

    doc = SimpleDocTemplate(
        filename,
        pagesize=A4
    )

    elements = []

    styles = getSampleStyleSheet()

    normal_style = styles["Normal"]

    # Suddivide testo in paragrafi
    paragraphs = report_text.split("\n")

    for p in paragraphs:
        if p.strip() == "":
            elements.append(Spacer(1, 0.2 * inch))
        else:
            elements.append(Paragraph(p, normal_style))
            elements.append(Spacer(1, 0.2 * inch))

    doc.build(elements)

    return filename
