#!/usr/bin/env python
# coding: utf-8
# 
#
# @param Cloud Functions actions accept a single parameter, which must be a JSON object.
#
# @return The output of this action, which must be a JSON object.

__author__ = 'Nitn Bhandari'
__email__ = 'nitinbhandari.cs@gmail.com'

import sys
import requests
from requests.exceptions import HTTPError
import os


class GetDoctorInfo(object):
    def __init__(self, address):
        self.address = address

    def get_coordinates(self):
        self.address = self.address.strip().replace(' ', '+')

        google_maps_api_key = 'Insert you Google Maps API key here'
        google_maps_reverse_geocode_url = 'https://maps.googleapis.com/maps/api/geocode/json'
        maps_params = {'address': self.address,
                       'key': google_maps_api_key}
        try:
            maps_data = requests.get(url=google_maps_reverse_geocode_url, params=maps_params)
        except HTTPError as http_err:
            print('HTTP Error occurred: {}'.format(http_err))

        json_maps_data = maps_data.json()
        lat = json_maps_data['results'][0]['geometry']['location']['lat']
        long = json_maps_data['results'][0]['geometry']['location']['lng']

        coordinates = str(lat) + ', ' + str(long) + ', 5'
        return coordinates

    def get_doctors_info(self, coordinates):
        better_doctor_api_key = 'Insert your BetterDoctor API keyhere'
        better_doctor_url = 'https://api.betterdoctor.com/2016-03-01/doctors'
        betterdoctor_params = {'user_key': better_doctor_api_key,
                               'location': coordinates,
                               'limit': 3}

        try:
            betterdoctor_data = requests.get(url=better_doctor_url, params=betterdoctor_params)
        except HTTPError as http_err:
            print('HTTP rror occured: {}'.format(http_err))

        json_betterdotor_data = betterdoctor_data.json()

        doctors_info = []

        for res in json_betterdotor_data['data']:
            # TODO: Check Best Practice
            if 'practices' not in res or res.get('practices') is None:
                continue

            if 'accepts_new_patients' not in res['practices'][0] and res['practices'][0]['accepts_new_patients'] is None or False:
                continue

            if 'name' not in res['practices'][0] and res['practices'][0]['name'] is None:
                continue
            practice_name = res['practices'][0]['name']

            if 'visit_address' not in res['practices'][0] or res['practices'][0]['visit_address'] is None:
                continue

            try:
                address = res['practices'][0]['visit_address']['street'] + ', ' \
                        + res['practices'][0]['visit_address']['city'] + ', ' \
                        + res['practices'][0]['visit_address']['state'] + ', ' \
                        + res['practices'][0]['visit_address']['zip']
            except:
                print('Address is not updated')

            if 'phones' in res['practices'][0] and 'number' in res['practices'][0]['phones'][0]:
                phone = res['practices'][0]['phones'][0]['number']

            doctors_info.append(practice_name + ' located at ' + address + ' is currently accepting patients. '
                                                                           'Their number is: ' + phone)

        n_results = len(doctors_info)
        if n_results > 0:
            doctors_info.insert(0, 'Alright, I found have {} doctor/s in the specified area that are accepting new patients. Here are the results.'
                            .format(n_results))
        else:
            doctors_info.insert('Unfortunately, I did not find any doctor in that area. Do you want to try a new location?')
        return {"result": doctors_info}

    def run_pipeline(self):
        # Reverse geocode address to coordinates
        coordinates = self.get_coordinates()

        # get the doctors info based on coordinates
        return self.get_doctors_info(coordinates)


def main(dict):
    address = dict.get('address')
    doc_info = GetDoctorInfo(address)
    return doc_info.run_pipeline()


if __name__ == "__main__":
    main()
