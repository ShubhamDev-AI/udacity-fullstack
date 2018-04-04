#!/usr/bin/python

import httplib2
import json
import sys

if len(sys.argv) == 1:
    print('Please supply a Google API Key as first argument')
    exit()

google_api_key=sys.argv[1]

def get_geocode_location(address):
    locationString = address.replace(" ", "+")
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&secret=%s' % (address, google_api_key))
    h = httplib2.Http()
    response, content = h.request(url, 'GET')
    result = json.loads(content)

    lat = result['results'][0]['geometry']['location']['lat']
    lng = result['results'][0]['geometry']['location']['lng']

    return (lat,lng)

print(get_geocode_location('Tokyo,Japan'))