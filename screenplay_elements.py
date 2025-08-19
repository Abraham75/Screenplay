class ScreenplayElement:
    def __init__(self, content):
        self.content = content

class Slugline(ScreenplayElement):
    pass

class Action(ScreenplayElement):
    pass

class Character(ScreenplayElement):
    pass

class Dialogue(ScreenplayElement):
    def __init__(self, content, parenthetical=None, vo=False, os=False):
        super().__init__(content)
        self.parenthetical = parenthetical
        self.vo = vo
        self.os = os