
COLOR_MAP = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}

def color_code(color):
    if color not in COLOR_MAP:
        raise ValueError(f"Invalid color: {color}")
    return COLOR_MAP[color]

def colors():
    return list(COLOR_MAP.keys())
