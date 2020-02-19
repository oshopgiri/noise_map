import json
import requests
import time


def get_current_noise_levels():
    current_noise_levels = {}
    current_timestamp = time.time()

    for i in range(1, 13):
        response = requests.get(f"http://dublincitynoise.sonitussystems.com/applications/api/dublinnoisedata.php"
                                f"?location={i}&start={current_timestamp}&end={current_timestamp}")

        if response.status_code == 200:
            try:
                body = json.loads(response.text)
                current_noise_levels[i] = float(body["aleq"][-1])
            except:
                pass

    return current_noise_levels


def format_for_interface(noise_levels, location_information):
    display_data = {
        "type": "FeatureCollection",
        "crs": {
            "type": "name",
            "properties": {
                "name": "urn:ogc:def:crs:OGC:1.3:CRS84"
            }
        },
        "features": []
    }

    for location_number in noise_levels.keys():
        display_data["features"].append({
                "type": "Feature",
                "properties": {
                    "id": location_number,
                    "name": location_information[location_number]['name'],
                    "noise": noise_levels[location_number]
                },
                "geometry": {
                    "type": "Point",
                    "coordinates": [
                        location_information[location_number]['longitude'],
                        location_information[location_number]['latitude']
                    ]
                }
            })

    return display_data
