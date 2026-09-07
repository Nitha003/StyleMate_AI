def explain_outfit(
    top,
    bottom,
    shoes,
    occasion,
    weather,
    activity,
    style
):

    reasons = []

    # Occasion
    if occasion in top["occasion"]:
        reasons.append(
            f"{top['name']} is suitable for {occasion.lower()}."
        )

    # Weather
    if weather == "Hot":
        if top["season"] == "Summer":
            reasons.append(
                f"{top['name']} is suitable for hot weather."
            )

    elif weather == "Cold":
        if top["season"] == "Winter":
            reasons.append(
                f"{top['name']} is suitable for cold weather."
            )

    # Activity
    if activity in top["activity"]:
        reasons.append(
            f"The outfit is suitable for {activity.lower()} activity."
        )

    # Style
    if top["style"] == style:
        reasons.append(
            f"The outfit matches your {style.lower()} style."
        )

    # Color
    if top["color"] != bottom["color"]:
        reasons.append(
            f"{top['color']} and {bottom['color']} work well together."
        )

    if bottom["color"] != shoes["color"]:
        reasons.append(
            f"{bottom['color']} and {shoes['color']} create a balanced color combination."
        )

    return reasons