#!/usr/bin/env python3
#
# Client for the UINames.com service.

import requests


def SampleRecord():
    r = requests.get("http://uinames.com/api?ext&region=germany",
                     timeout=2.0)
    # 1. Add a line of code here to decode JSON from the response.
    response_data = r.json()

    return "My name is {name} {surname} and the PIN on my card is {pin}.".format(
        # 2. Add the correct fields from the JSON data structure.
        name=response_data['name'],
        surname=response_data['surname'],
        pin=response_data['credit_card']['pin']
    )

if __name__ == '__main__':
    print(SampleRecord())
