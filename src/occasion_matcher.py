def get_occasion_score(clothing, selected_occasion):

    if selected_occasion in clothing["occasion"]:
        return 100

    return 40


def get_weather_score(clothing, weather):

    if weather == "Hot":
        if clothing["season"] == "Summer":
            return 100
        elif clothing["season"] == "Winter":
            return 30
        else:
            return 70

    if weather == "Cold":
        if clothing["season"] == "Winter":
            return 100
        elif clothing["season"] == "Summer":
            return 30
        else:
            return 70

    return 70


def get_activity_score(clothing, activity):

    if activity in clothing["activity"]:
        return 100

    return 50
def get_style_score(clothing, selected_style):

    if clothing["style"] == selected_style:
        return 100

    return 50