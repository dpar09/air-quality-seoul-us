from extract import get_airnow_data, get_waqi_data
from pprint import pprint

valid_pollutant = ["co", "no2", "o3", "pm10", "pm25", "so2"]

def transform_airnow(data, city_name):
    results = []
    for item in data:
        new_record = {
            "source" : "airnow",
            "city" : city_name,
            "pollutant" : item["ParameterName"],
            "value" : item['AQI'],
            "timestamp" : item["DateObserved"] + " " + str(item["HourObserved"]) + ":00"
        }
        results.append(new_record)
    return results

def transform_waqi(data, city_name):
    results = []
    iaqi = data["data"]["iaqi"]
    for pollutant_name in iaqi:
        if pollutant_name in valid_pollutant:
            value = iaqi[pollutant_name]["v"]
            new_record = {
                "source" : "waqi",
                "city" : city_name,
                "pollutant" : pollutant_name,
                "value" : value,
                "timestamp" : data["data"]["time"]["s"]
            }
            results.append(new_record)
    return results


if __name__ == "__main__":
    raw = get_airnow_data("06033")
    transformed = transform_airnow(raw, "Hartford")
    pprint(transformed)

    raw_waqi = get_waqi_data("seoul")
    transformed_waqi = transform_waqi(raw_waqi, "Seoul")
    pprint(transformed_waqi)