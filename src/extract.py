import requests
from config import airnow_api, waqi_api, AIRNOW_BASE_URL, WAQI_BASE_URL


def get_airnow_data(zip_code):
    response = requests.get(AIRNOW_BASE_URL, params={
        "format" : "application/json",
        "zipCode" : zip_code,
        "distance" : 25,
        "API_KEY" : airnow_api
        })
    data = response.json()
    return data

def get_waqi_data(city):
    response = requests.get(WAQI_BASE_URL + city, params={"token": waqi_api})
    data = response.json()
    return data

if __name__ == "__main__":
    print(get_airnow_data("06033"))
    print(get_waqi_data("seoul"))