import requests
import os
from dotenv import load_dotenv
load_dotenv()


def main():
    username = os.getenv('FLIGHTWARE_USERNAME')
    apikey = os.getenv('FLIGHTAWARE_API')
    fxml_url = "https://flightxml.flightaware.com/json/FlightXML2/"
    payload = {'airport': 'KSFO',
               'howMany': '10'}

    response = requests.get(fxml_url + "Enroute", params=payload, auth=(username, apikey))

    if response.status_code == 200:
        print(response.json())
    else:
        print("Error executing request")


if __name__ == '__main__':
    main()
