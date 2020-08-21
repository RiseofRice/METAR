import requests
import headers
import json


def requesting(ICAO):
    url = f"https://api.checkwx.com/metar/{ICAO}"
    x = requests.get(url, headers=headers.headers)
    data = json.dumps(x.json())
    data = json.loads(data)
    return data
