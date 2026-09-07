from itertools import product
from outfit_score import calculate_outfit_score


def generate_outfit(
    wardrobe,
    occasion,
    weather,
    activity,
    style
):

    tops = [
        item for item in wardrobe
        if item["category"] == "Tops"
    ]

    bottoms = [
        item for item in wardrobe
        if item["category"] == "Bottoms"
    ]

    shoes = [
        item for item in wardrobe
        if item["category"] == "Shoes"
    ]

    outfits = []

    for top, bottom, shoe in product(
        tops,
        bottoms,
        shoes
    ):

        score = calculate_outfit_score(
            top,
            bottom,
            shoe,
            occasion,
            weather,
            activity,
            style
        )

        outfits.append({
            "top": top,
            "bottom": bottom,
            "shoes": shoe,
            "score": score
        })

    outfits.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return outfits