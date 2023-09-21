#!venv/bin/python3

"""
Pull data from a PurpleAir sensor and augment it with AQI
"""

import json
import os
import sys

import dotenv
import requests


dotenv.load_dotenv()


def sensor_data(sensor_id):
    headers = {
        "X-API-Key": os.getenv('PURPLEAIR_READ_KEY'),
    }
    r = requests.get(
        f'https://api.purpleair.com/v1/sensors/{sensor_id}',
        headers=headers)
    if r.status_code == 200:
        return r.json()
    # TODO: error handling
    # print(json.dumps(r.json(), indent=2))
    return {
        "error": r.status_code,
    }


def correct(pm25, rh):
    # EPA corrections for PurpleAir pm2.5 sensor values
    # See references in the README

    if False:
        # 2019 US-wide correction
        return 5.75 - (0.085 * rh) + (0.52 * pm25)

    if True:
        # 2021 correction for fire and smoke
        # TODO: triple-check these numbers against the PDF
        if pm25 < 30:
            return 5.75 - (0.0862 * rh) + (0.524 * pm25)
        elif pm25 < 50:
            weight = (pm25 / 20) - (30 / 20)
            return (
                5.75 - (0.0862 * rh) +
                ((0.786 * weight) + (0.524 * (1 - weight))) * pm25
            )
        elif pm25 < 210:
            return 5.75 - (0.0862 * rh) + (0.786 * pm25)
        elif pm25 < 260:
            weight = (pm25 / 50) - (210 / 50)
            return (
                (0.0862 * rh) * (1 - weight) +
                ((0.69 * weight) + (0.786 * (1 - weight))) * pm25 +
                (2.966 * weight) + (5.75 * (1 - weight)) +
                (8.84 * pow(10, -4)) * pow(pm25, 2) * weight
            )
        else:
            return 2.966 + (0.69 * pm25) + (8.84 * pow(10, -4)) * pow(pm25, 2)

    # uncorrected
    return pm25


# https://www.airnow.gov/sites/default/files/2020-05/aqi-technical-assistance-document-sept2018.pdf
BREAKPOINTS = [
    [  0.0,  12.0,   0,  50, 'Good',           '#00e400'],  # noqa: E201
    [ 12.1,  35.4,  51, 100, 'Moderate',       '#ffff00'],  # noqa: E201
    [ 35.5,  55.4, 101, 150, 'Sensitive',      '#ff7e00'],  # noqa: E201
    [ 55.5, 150.4, 151, 200, 'Unhealthy',      '#ff0000'],  # noqa: E201
    [150.5, 250.4, 201, 300, 'Very Unhealthy', '#993f97'],
    [250.5, 350.4, 301, 400, 'Hazardous',      '#7e0023'],
    [350.5, 500.4, 501, 500, 'Hazardous',      '#7e0023'],
]


def pm25_to_aqi(pm25):
    # returns a tuple of (AQI, category, RBG color)
    assert pm25 >= 0.0
    bp = [bp for bp in BREAKPOINTS if pm25 >= bp[0]][-1]
    aqi = bp[2] + (pm25 - bp[0]) * float(bp[3] - bp[2]) / float(bp[1] - bp[0])
    return (int(aqi), bp[4], bp[5])


def add_derived_aqi(sensor_data):
    """
    Augment sensor data with derived AQI

    Does nothing if the data indicates an error.
    Mutates the data in place
    """
    if 'error' not in sensor_data:
        sensor = sensor_data["sensor"]
        corrected_pm25 = correct(sensor["pm2.5"], sensor["humidity"])
        aqi, category, color = pm25_to_aqi(corrected_pm25)
        sensor["aqi"] = aqi
        sensor["category"] = category
        # TODO: downgrade color if data is stale
        sensor["category_color"] = color


if __name__ == '__main__':
    """
    humidity = 40
    for pm25 in range(255):
        print(f'{pm25}: {pm25_to_aqi(correct(float(pm25), 40))}')
    """

    try:
        sensor_id = int(sys.argv[1])
    except Exception:
        print(f"Usage: {sys.argv[0]} ID")
        sys.exit(1)

    data = sensor_data(sensor_id)
    add_derived_aqi(data)

    print(json.dumps(data, indent=2))
