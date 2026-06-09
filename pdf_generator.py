from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(report_text, filename):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    elements = []

    title = Paragraph(
        "AI Resume Analyzer Report",
        styles['Title']
    )

    elements.append(title)

    elements.append(Spacer(1, 20))

    for line in report_text.split("\n"):

        p = Paragraph(
            line,
            styles['Normal']
        )

        elements.append(p)

        elements.append(Spacer(1, 5))

    doc.build(elements)

    return filename