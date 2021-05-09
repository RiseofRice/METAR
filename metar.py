from sys import argv
import requester
import json
import requests
import headers

headers = headers.headers


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

    data = data['data'][0].split()
    # print(data)

    for i in range(0, len(data), 3):
        print('\t\t'.join(data[i:i+3]))
    print("\n\n")
    

if __name__ == "__main__":
    if len(argv) > 1:
        get_metar_info(argv[1])
    else:
        print("you need to enter an ICAO code")


