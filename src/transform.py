from extract import get_airnow_data, get_waqi_data
from pprint import pprint

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

if __name__ == "__main__":
    raw = get_airnow_data("06033")
    transformed = transform_airnow(raw, "Hartford")
    pprint(transformed)