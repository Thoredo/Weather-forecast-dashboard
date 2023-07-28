from dotenv import load_dotenv
import os
import requests

load_dotenv()

API_KEY = os.getenv("API_KEY")

def get_data(place, forecast_days, view_type):

    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    number_of_values = 8 * forecast_days
    filtered_data = filtered_data[:number_of_values]
    if view_type == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
    if view_type == "Sky":
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
    return filtered_data

if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3, view_type="Temperature"))
