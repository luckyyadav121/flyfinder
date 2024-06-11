import requests
from datetime import datetime, timedelta
from flight_data import FlightData

class FlightSearch:
    def __init__(self, api_key, currency="INR"):
        self.api_key = api_key
        self.currency = currency
        self.tequila_endpoint = "https://serpapi.com/search"
        self.flights_endpoint = f"{self.tequila_endpoint}/v2/search"
        self.location_endpoint = f"{self.tequila_endpoint}/locations/query"

    def get_location_iata_code(self, city_name):
        params = {
            "term": city_name,
            "location_types": "city"
        }

        response = requests.get(url=self.location_endpoint, headers={"apikey": self.api_key}, params=params)
        response.raise_for_status()
        data = response.json()["locations"]
        
        if data:
            return data[0]["code"]
        else:
            print(f"No IATA code found for city: {city_name}")
            return None

    def search_flights(self, departure_city, destination_city, from_date, to_date, max_stopovers=1):
        departure_iata = self.get_location_iata_code(departure_city)
        destination_iata = self.get_location_iata_code(destination_city)

        if not departure_iata or not destination_iata:
            return None

        params = {
            "fly_from": departure_iata,
            "fly_to": destination_iata,
            "date_from": from_date.strftime("%d/%m/%Y"),
            "date_to": to_date.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": max_stopovers,
            "curr": self.currency
        }

        response = requests.get(url=self.flights_endpoint, headers={"apikey": self.api_key}, params=params)
        data = response.json()

        if "data" not in data or not data["data"]:
            print(f"No flights found from {departure_city} to {destination_city}.")
            return None

        flight_data = data["data"][0]
        return self.process_flight_data(flight_data)

    def process_flight_data(self, flight_data):
        price = flight_data["price"]
        departure_city = flight_data["route"][0]["cityFrom"]
        departure_airport = flight_data["route"][0]["flyFrom"]
        destination_city = flight_data["route"][0]["cityTo"]
        destination_airport = flight_data["route"][0]["flyTo"]
        out_date = flight_data["route"][0]["local_departure"].split("T")[0]
        return_date = flight_data["route"][1]["local_departure"].split("T")[0]

        return FlightData(
            price=price,
            departure_city=departure_city,
            departure_airport=departure_airport,
            destination_city=destination_city,
            destination_airport=destination_airport,
            out_date=out_date,
            return_date=return_date
        )

if __name__ == "__main__":
    api_key = "2aa35e9c55c3893c79f250c689560068fd349648039b03761051c4b989df60f1"
    flight_search = FlightSearch(api_key)
  
    departure_city = "New York"
    destination_city = "Los Angeles"
    from_date = datetime.now() + timedelta(days=7)
    to_date = from_date + timedelta(days=10)

    flight_result = flight_search.search_flights(departure_city, destination_city, from_date, to_date, max_stopovers=1)

    if flight_result:
        print(f"Flight from {flight_result.departure_city} to {flight_result.destination_city}: ${flight_result.price}")
