import requests

import json
headers = {"X-API-Key": "69d7644418204967b4ff79fab3"}

def requesting(ICAO):
    url = f"https://api.checkwx.com/metar/{ICAO}"
    x = requests.get(url, headers=headers)
    data = json.dumps(x.json())
    data = json.loads(data)
    return data
