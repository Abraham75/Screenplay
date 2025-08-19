def validate_element(element):
    return hasattr(element, 'content') and isinstance(element.content, str)

def format_element(element):
    if element.__class__.__name__ == "Slugline":
        return f"\n\n{element.content.upper()}\n"
    elif element.__class__.__name__ == "Action":
        return f"{element.content}\n"
    elif element.__class__.__name__ == "Character":
        return f"\n\t\t\t\t\t{element.content.upper()}\n"
    elif element.__class__.__name__ == "Dialogue":
        formatted = ""
        if element.parenthetical:
            formatted += f"\t\t\t\t({element.parenthetical})\n"
        vo_os = ""
        if element.vo:
            vo_os = " (V.O.)"
        elif element.os:
            vo_os = " (O.S.)"
        formatted += f"\t\t\t{element.content}{vo_os}\n"
        return formatted
    else:
        return f"{element.content}\n"