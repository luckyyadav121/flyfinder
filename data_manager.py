import requests

SHEETY_ENDPOINT = "https://api.sheety.co/c911a26e90e4a5b8bc09926a407ec5bb/flightSearcher/sheet1"


class DataManager:
    def __init__(self):
        self.main_data = {}

    def get_data(self):
        response = requests.get(url=SHEETY_ENDPOINT)
        data = response.json()
        # self.main_data = data["Sheet1"]
        return data['sheet1']

    def update_destination_codes(self):
        for city in self.main_data:
            new_data = {
                "sheet1": {
                    "iataCode": city["iataCode"]
                }
            }
            requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}", json=new_data)
