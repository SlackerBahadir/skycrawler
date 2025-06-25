import requests

from skyfield.api import load, N, W, wgs84

def find_loc():
    url = "https://ipinfo.io/json"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        lon, lat = data["loc"].split(',')

        return lon, lat
    return ()

def get_planets_for_loc():
    ts = load.timescale()
    t = ts.now()

    planets = load('de421.bsp')

    print(planets)