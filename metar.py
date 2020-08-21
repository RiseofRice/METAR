from sys import argv
import requester
import json
import requests

headers = {"X-API-Key": "69d7644418204967b4ff79fab3"}


def requesting(ICAO):
    url = f"https://api.checkwx.com/metar/{ICAO}"
    x = requests.get(url, headers=headers)
    data = json.dumps(x.json())
    data = json.loads(data)
    return data


def get_metar_info(ICAO):

    data = requesting(ICAO.lower())
    if data['results'] == 0:
        print("wrong or no ICAO code")
        return
    else:
        print(data)
        print("\n\n")

    data = data['data'][0].split(" ")
    x = 0
    l = []
    for i in data:
        x = x + 1
        l.append(i)
        if x == 3:

            print(f"{l[0]}\t\t{l[1]}\t\t{l[2]}")

            l = []
            x = 0
    print("\n\n")


if __name__ == "__main__":
    if len(argv) > 1:
        get_metar_info(argv[1])
    else:
        print("you need to enter an ICAO code")
