from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

pdfmetrics.registerFont(TTFont("Courier", "Courier.ttf"))

def generate_pdf(elements, filename):
    doc = SimpleDocTemplate(filename, pagesize=letter,
                            leftMargin=1.5*inch, rightMargin=1*inch,
                            topMargin=1*inch, bottomMargin=1*inch)
    styles = getSampleStyleSheet()
    styles["Normal"].fontName = "Courier"
    styles["Normal"].fontSize = 12

    story = []
    for element in elements:
        story.append(Paragraph(element.replace("\t", "&nbsp;&nbsp;&nbsp;&nbsp;").replace("\n", "<br />"), styles["Normal"]))
        story.append(Spacer(1, 12))  # double space

    doc.build(story)