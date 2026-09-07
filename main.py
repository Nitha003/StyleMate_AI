import json
import sys


sys.path.append("src")

from outfit_generator import generate_outfit
from recommendation_explainer import explain_outfit


with open("data/wardrobe.json", "r") as file:
    data = json.load(file)

if isinstance(data, list):
    wardrobe = data
else:
    wardrobe = data["items"]

print("===== StyleMate Outfit Recommendation =====")

occasion = input(
    "Enter occasion (College/Office/Casual/Formal): "
).strip().title()

weather = input(
    "Enter weather (Hot/Cold/Normal): "
).strip().title()

activity = input(
    "Enter activity (Regular/Outdoor): "
).strip().title()

style = input(
    "Enter style (Casual/Formal/Sporty/Traditional): "
).strip().title()
outfits = generate_outfit(
    wardrobe,
    occasion,
    weather,
    activity,
    style
)


print("\n===== TOP 3 OUTFITS =====")


for i, outfit in enumerate(outfits[:3], start=1):

    print(f"\nOutfit {i}")
    print("------------------")

    print(
        "Top:",
        outfit["top"]["name"]
    )

    print(
        "Bottom:",
        outfit["bottom"]["name"]
    )

    print(
        "Shoes:",
        outfit["shoes"]["name"]
    )

    print(
        "Score:",
        outfit["score"]
    )

    reasons = explain_outfit(
        outfit["top"],
        outfit["bottom"],
        outfit["shoes"],
        occasion,
        weather,
        activity,
        style
    )

    print("\nWhy this outfit?")

    for reason in reasons:
        print("✓", reason)