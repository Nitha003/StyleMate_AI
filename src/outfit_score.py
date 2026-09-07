from color_matcher import get_color_score

from occasion_matcher import (
    get_occasion_score,
    get_weather_score,
    get_activity_score,
    get_style_score
)


def calculate_outfit_score(
    top,
    bottom,
    shoes,
    occasion,
    weather,
    activity,
    style
):

    color_score_1 = get_color_score(
        top["color"],
        bottom["color"]
    )

    color_score_2 = get_color_score(
        bottom["color"],
        shoes["color"]
    )

    color_score = (
        color_score_1 + color_score_2
    ) / 2

    occasion_score = (
        get_occasion_score(top, occasion) +
        get_occasion_score(bottom, occasion) +
        get_occasion_score(shoes, occasion)
    ) / 3

    weather_score = (
        get_weather_score(top, weather) +
        get_weather_score(bottom, weather) +
        get_weather_score(shoes, weather)
    ) / 3

    activity_score = (
        get_activity_score(top, activity) +
        get_activity_score(bottom, activity) +
        get_activity_score(shoes, activity)
    ) / 3

    style_score = (
        get_style_score(top, style) +
        get_style_score(bottom, style) +
        get_style_score(shoes, style)
    ) / 3

    final_score = (
        color_score * 0.20 +
        occasion_score * 0.25 +
        weather_score * 0.20 +
        activity_score * 0.15 +
        style_score * 0.20
    )

    return round(final_score, 2)