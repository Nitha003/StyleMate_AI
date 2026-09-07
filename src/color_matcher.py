COLOR_COMPATIBILITY = {
    "Black": ["White", "Blue", "Red", "Green", "Yellow", "Grey", "Brown", "Orange", "Pink", "Purple"],
    "White": ["Black", "Blue", "Red", "Green", "Yellow", "Grey", "Brown", "Orange", "Pink", "Purple"],
    "Blue": ["Black", "White", "Grey", "Brown"],
    "Red": ["Black", "White", "Grey", "Blue"],
    "Green": ["Black", "White", "Brown", "Grey"],
    "Yellow": ["Black", "White", "Blue", "Grey"],
    "Grey": ["Black", "White", "Blue", "Red", "Green", "Purple"],
    "Brown": ["White", "Blue", "Green", "Black"],
    "Orange": ["Black", "White", "Blue"],
    "Pink": ["Black", "White", "Grey", "Blue"],
    "Purple": ["Black", "White", "Grey"]
}


def get_color_score(color1, color2):

    if color1 == color2:
        return 70

    if color2 in COLOR_COMPATIBILITY.get(color1, []):
        return 90

    return 40