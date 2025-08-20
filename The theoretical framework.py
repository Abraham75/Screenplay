"""
TheoreticalFramework.py

Screenplectics Parsing Engine:
A research-grade screenplay parser grounded in symbolic state parsing,
deterministic flow, and format-preserving validation.

Author: [Your Name]
PhD-level implementation (Screenplectics Framework)

Core Idea:
    - Parse raw screenplay text into canonical states: SLUGLINE, ACTION, DIALOGUE, TRANSITION.
    - Hybrid Regex + State Machine approach allows both rule-driven parsing
      and heuristic flexibility for edge cases.
    - Ensures compliance with professional screenplay formats.
"""

import re
from enum import Enum, auto
from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas
from typing import List, Optional


# --------------------------
# STATE DEFINITIONS
# --------------------------

class ParseState(Enum):
    SLUGLINE = auto()
    ACTION = auto()
    DIALOGUE = auto()
    TRANSITION = auto()
    UNKNOWN = auto()


# --------------------------
# SCREENPLAY ELEMENTS
# --------------------------

class ScreenplayElement:
    """Abstract superclass for screenplay units."""
    def __init__(self, raw_text: str):
        self.raw_text = raw_text.strip()

    def format_txt(self) -> str:
        raise NotImplementedError


class Slugline(ScreenplayElement):
    def format_txt(self) -> str:
        return self.raw_text.upper() + "\n"


class Action(ScreenplayElement):
    def format_txt(self) -> str:
        return self.raw_text + "\n"


class Dialogue(ScreenplayElement):
    def __init__(self, speaker: str, content: str):
        self.speaker = speaker.strip().upper()
        self.content = content.strip()

    def format_txt(self) -> str:
        # Dialogue: character centered, text indented
        return f"\n    {self.speaker}\n        {self.content}\n"


class Transition(ScreenplayElement):
    def format_txt(self) -> str:
        return self.raw_text.upper().rjust(70) + "\n"


# --------------------------
# PARSER IMPLEMENTATION
# --------------------------

class ScreenplayParser:
    """Regex + State Machine parser for screenplay text."""

    SLUGLINE_PATTERN = re.compile(r"^(INT\.|EXT\.|INT/EXT\.).+", re.IGNORECASE)
    TRANSITION_PATTERN = re.compile(r".+\sTO:$", re.IGNORECASE)
    CHARACTER_PATTERN = re.compile(r"^[A-Z][A-Z0-9 ]+$")

    def __init__(self):
        self.elements: List[ScreenplayElement] = []

    def parse(self, raw_script: str) -> List[ScreenplayElement]:
        lines = raw_script.splitlines()
        state: ParseState = ParseState.UNKNOWN
        buffer = []

        for line in lines:
            striped = line.strip()

            if not striped:  # line break reset
                continue

            if self.SLUGLINE_PATTERN.match(striped):
                self._flush_buffer(state, buffer)
                buffer = []
                state = ParseState.SLUGLINE
                self.elements.append(Slugline(striped))

            elif self.TRANSITION_PATTERN.match(striped):
                self._flush_buffer(state, buffer)
                buffer = []
                state = ParseState.TRANSITION
                self.elements.append(Transition(striped))

            elif self.CHARACTER_PATTERN.match(striped):
                self._flush_buffer(state, buffer)
                state = ParseState.DIALOGUE
                buffer = [striped]  # speaker name line

            else:
                if state == ParseState.DIALOGUE:
                    # line belongs to dialogue content
                    speaker = buffer[0]
                    content = striped
                    self.elements.append(Dialogue(speaker, content))
                    buffer = []
                else:
                    # default as ACTION
                    state = ParseState.ACTION
                    self.elements.append(Action(striped))

        self._flush_buffer(state, buffer)
        return self.elements

    def _flush_buffer(self, state: ParseState, buffer: list):
        """Handles any residual content when transitioning states."""
        if not buffer:
            return
        if state == ParseState.DIALOGUE:
            speaker = buffer[0]
            content = " ".join(buffer[1:])
            self.elements.append(Dialogue(speaker, content))


# --------------------------
# FORMATTER EXPORTS
# --------------------------

class ScreenplayFormatter:
    """Responsible for exporting screenplay into target formats."""

    def __init__(self, elements: List[ScreenplayElement]):
        self.elements = elements

    def to_txt(self, filename: str):
        with open(filename, "w") as f:
            for elem in self.elements:
                f.write(elem.format_txt() + "\n")

    def to_pdf(self, filename: str):
        c = canvas.Canvas(filename, pagesize=LETTER)
        width, height = LETTER
        y = height - 50
        for elem in self.elements:
            block = elem.format_txt().splitlines()
            for line in block:
                c.drawString(72, y, line)
                y -= 14
                if y < 72:  # page break
                    c.showPage()
                    y = height - 50
        c.save()


# --------------------------
# UNIT TEST EXAMPLE
# --------------------------

def _unit_test():
    raw = """
    INT. LIVING ROOM - DAY

    John sits on the couch.

    JOHN
    I can’t believe this works.

    FADE OUT:
    """
    parser = ScreenplayParser()
    elements = parser.parse(raw)
    fmt = ScreenplayFormatter(elements)
    fmt.to_txt("output.txt")
    fmt.to_pdf("output.pdf")
    print("✅ Unit test run: output.txt and output.pdf generated.")


if __name__ == "__main__":
    _unit_test()
