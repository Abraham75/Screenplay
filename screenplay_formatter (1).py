from screenplay_elements import Slugline, Action, Character, Dialogue
from screenplay_utils import validate_element, format_element
from screenplay_pdf import generate_pdf

class ScreenplayFormatter:
    def __init__(self):
        self.elements = []

    def add_element(self, element):
        if validate_element(element):
            formatted = format_element(element)
            self.elements.append(formatted)

    def export_to_pdf(self, filename):
        generate_pdf(self.elements, filename)

if __name__ == "__main__":
    import sys
    output_filename = "screenplay_output.pdf"
    formatter = ScreenplayFormatter()
    formatter.add_element(Slugline("INT. HOUSE - NIGHT"))
    formatter.add_element(Action("The wind blows fiercely through broken windows."))
    formatter.add_element(Character("JOHN"))
    formatter.add_element(Dialogue("I told you this would happen.", parenthetical="(whispering)", vo=True))
    formatter.export_to_pdf(output_filename)