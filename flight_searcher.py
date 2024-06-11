import requests
import flight_data

api_key = "qB1Wbo547j5gsWLCt8qtjIk9pcEhSH-Y"
tequila_endpoint = "https://tequila-api.kiwi.com"#REQUEST LOCATION
flights_endpoint = "https://tequila-api.kiwi.com/v2/search"
location_endpoint = "https://tequila-api.kiwi.com/locations/query"
header = {"apikey": api_key}
CURR = "INR"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def get_destination_iata_code(self, city_name):
        param = {
            "term": city_name,
            "location_types": "city"
        }

        response = requests.get(url=location_endpoint, headers=header, params=param)
        response.raise_for_status()

        data = response.json()
        data = data["locations"]
        iata_code = data[0]["code"]

        return iata_code

    def flight_cost(self, departure, destination, from_day, to_day):
        param = {
            "fly_from": departure,
            "fly_to": destination['iataCode'],
            "date_from": from_day.strftime("%d/%m/%Y"),
            "date_to": to_day.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": CURR
        }

        response = requests.get(url=flights_endpoint, headers=header, params=param)
        data = response.json()

        try:
            data = data["data"][0]
        except IndexError:
            param["max_stopovers"] = 1
            response = requests.get(url=flights_endpoint, headers=header, params=param)
            data = response.json()

            try:
                data["data"][0]
            except IndexError:
                print(f"No flights found for {destination['iataCode']}.")
                return None

            flight_result = flight_data.FlightData(
                price=data["price"],
                departure_city=data["route"][0]["cityFrom"],
                departure_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )
            return flight_result
        except KeyError:
            print(f'''No such city with name "{destination['city']}" exist''')
            return None
        else:
            flight_result = flight_data.FlightData(
                price=data["price"],
                departure_city=data["route"][0]["cityFrom"],
                departure_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0],
                stop_overs=param["max_stopovers"],
                via_city=data["route"][0]["cityTo"]
            )
            print(f"{flight_result.destination_city}: £{flight_result.price}")
            return flight_result

    def get_flight_details(self, from_country, from_city, to_country, to_city, from_day, to_day):
        if not from_city.strip() == "" :
            from_country += ","+from_city
        if not to_city.strip() == "" :
            to_country += ","+to_city

        param = {
            "fly_from": from_country,
            "fly_to": to_country,
            "date_from": from_day,  # .strftime("%d/%m/%Y")
            "date_to": to_day,  # .strftime("%d/%m/%Y")
            "flight_type": "oneway",
            "one_for_city": 1,
            "max_stopovers": 1,
            "max_sector_stopovers": 1,
            "curr": CURR,
            "limit": 200,
            "sort": "date",
            "stopover_from": "00:00",
            "stopover_to": "48:00"
        }
        response = requests.get(url=flights_endpoint, headers=header, params=param)
        data = response.json()

        res = list()
        print(data)
        data = data["data"]
        for temp in data:
            formats = {
                "from": {
                    'city': temp['cityFrom'],
                    'country': temp['countryFrom']['name']
                },
                "to": {
                    'city': temp['cityTo'],
                    'country': temp['countryTo']['name']
                },
                "price": temp["price"],
                "availability": temp["availability"]['seats'],
                "fare": temp["fare"],
                "flight_no": temp["route"][0]['flight_no'],
                "local_arrival": temp['local_arrival'],
                "utc_arrival": temp['utc_arrival'],
                "local_departure": temp['local_departure'],
                "utc_departure": temp['utc_departure'],
                "duration": temp['duration']['total'],
                "distance": temp["distance"],
                "bag_limit": temp['baglimit']['hold_weight'],
                "bags_price": temp['bags_price']

            }
            res.append(formats)

        return res
