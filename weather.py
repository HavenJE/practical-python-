
import requests

def get_weather_desc_and_temp():
    api_key = "3dec6a785d421939ac31b05a2a96f588"
    city = "Baghdad"
    url = "https://api.openweathermap.org/data/2.5/weather?q="+city + \
        "&appid="+api_key+"&units=metric"  # dont leave any spaces in the url!

    request = requests.get(url)
    json = request.json()


    description = json["weather"][0]["description"]
    temp_min = json.get("main").get("temp_min")
    temp_max = json["main"]["temp_max"]

    # The print section 
    print("Brisbane weather today is:", description)
    print("Temperature range is: ", temp_min, "minimum celsius.")
    print("Maximum is: ", temp_max, "celsius.")

get_weather_desc_and_temp()