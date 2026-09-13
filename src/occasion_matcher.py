def get_occasion_score(clothing, selected_occasion):

    if clothing["occasion"].lower() == selected_occasion.lower():
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

    if clothing["activity"].lower() == activity.lower():
        return 100

    return 50


def get_style_score(clothing, selected_style):

    if clothing["style"].lower() == selected_style.lower():
        return 100

    return 50