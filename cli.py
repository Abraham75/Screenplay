import argparse
from screenplay_formatter import ScreenplayFormatter
from screenplay_elements import Slugline, Action, Character, Dialogue

def main():
    parser = argparse.ArgumentParser(description="Screenplay Formatter CLI")
    parser.add_argument("output", help="Output PDF filename")
    args = parser.parse_args()

    formatter = ScreenplayFormatter()
    formatter.add_element(Slugline("EXT. PARK - DAY"))
    formatter.add_element(Action("Children are playing. Dogs bark in the distance."))
    formatter.add_element(Character("MOTHER"))
    formatter.add_element(Dialogue("Time to go home, kids!", parenthetical="(yelling)", os=True))

    formatter.export_to_pdf(args.output)

if __name__ == "__main__":
    main()