#!/usr/bin/env python
# coding: utf-8

__author__ = 'Nitn Bhandari'
__email__ = 'nitinbhandari.cs@gmail.com'

import requests
from requests.exceptions import HTTPError
import os
from dotenv import load_dotenv


class getDoctorInfo(object):
    def __init__(self, address):
        self.address = address

    def get_coordinates(self, address):
        address = address.strip().replace(' ', '+')

        google_maps_api_key = 'AIzaSyCnlLqSJhK7PPgPaa69gj7UaHdeKHN7es0'
        google_maps_reverse_geocode_url = 'https://maps.googleapis.com/maps/api/geocode/json'
        maps_PARAMS = {'address': self.address,
                       'key': google_maps_api_key}
        try:
            maps_data = requests.get(url=google_maps_reverse_geocode_url, params=maps_PARAMS)
        except HTTPError as http_err:
            print('HTTP rror occured: {}'.format(http_err))

        json_maps_data = maps_data.json()
        lat = json_maps_data['results'][0]['geometry']['location']['lat']
        long = json_maps_data['results'][0]['geometry']['location']['lng']

        coordinates = str(lat) + ', ' + str(long) + ', 5'
        rerturn coordinates

    def get_doctors_info(self, coordinates):
        better_doctor_api_key = '3d75d15626810e1edf67533f5b18611e'
        better_doctor_url = 'https://api.betterdoctor.com/2016-03-01/doctors'
        betterdoctor_PARAMS = {'user_key': better_doctor_api_key,
                               'location': coordinates,
                               'limit': 5}

        try:
            betterdoctor_data = requests.get(url=better_doctor_url, params=betterdoctor_PARAMS)
        except HTTPError as http_err:
            print('HTTP rror occured: {}'.format(http_err))

        json_betterdotor_data = betterdoctor_data.json()
        print(betterdoctor_data.json())
        return None

    def gen_resp(self, info):
        pass

    def run_pipeline(self):
        # Reverse geocode address to coordinates
        coordinates = self.get_coordinates()

        # get the doctors info based on coordinates
        info = self.get_doctors_info(coordinates)

        # generate responses that can be spoken in human language
        responses = self.get_resp(info)



def main():
    doc_info = getDoctorInfo(address)
    doc_info.run_pipeline()


if __name__ == "__main__":
    main()
