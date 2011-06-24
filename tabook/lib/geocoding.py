import json
from urllib import urlencode
from urllib2 import urlopen


def get_geo_info(address):
    url = "http://maps.googleapis.com/maps/api/geocode/json"
    get_params = {"address": address, "sensor": "false"}

    data = urlopen("%s?%s" % (url, urlencode(get_params))).read()
    return json.loads(data)


def get_lat_lng(address):
    # 'lat': 37.4213068, 'lng': -122.08529
    data = get_geo_info(address)
    try:
        lat_lng = data["results"][0]["geometry"]["location"]
    except IndexError:
        return None, None
    return lat_lng["lat"], lat_lng["lng"]
