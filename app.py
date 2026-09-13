# pyrefly: ignore [missing-import]
from flask import Flask, request, jsonify
import sys

sys.path.append("src")

from outfit_generator import generate_outfit
from recommendation_explainer import explain_outfit


app = Flask(__name__)


@app.route("/recommend", methods=["POST"])
def recommend():

    data = request.get_json()

    # Get wardrobe
    wardrobe_data = data.get("wardrobe", {})
    wardrobe = wardrobe_data.get("items", [])

    # Get user preferences
    preferences = data.get("preferences", {})

    occasion = preferences.get("occasion", "Casual").strip().title()
    weather = preferences.get("weather", "Normal").strip().title()
    activity = preferences.get("activity", "Regular").strip().title()
    style = preferences.get("style", "Casual").strip().title()

    # Generate outfits
    outfits = generate_outfit(
        wardrobe,
        occasion,
        weather,
        activity,
        style
    )

    # No outfits available
    if not outfits:
        return jsonify({
            "success": False,
            "message": "Not enough clothing items to create an outfit."
        })

    # Top 3 recommendations
    recommendations = []

    for outfit in outfits[:3]:

        reasons = explain_outfit(
            outfit["top"],
            outfit["bottom"],
            outfit["shoes"],
            occasion,
            weather,
            activity,
            style
        )

        recommendations.append({
            "top": outfit["top"]["name"],
            "bottom": outfit["bottom"]["name"],
            "shoes": outfit["shoes"]["name"],
            "score": outfit["score"],
            "reasons": reasons
        })

    return jsonify({
        "success": True,
        "preferences": {
            "occasion": occasion,
            "weather": weather,
            "activity": activity,
            "style": style
        },
        "recommendations": recommendations
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)