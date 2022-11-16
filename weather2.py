
# we re-writing the weather code using functions:
import requests

api_key = "3dec6a785d421939ac31b05a2a96f588"
city = "Brisbane"
url = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=metric" # dont leave any spaces in the url! 

request = requests.get(url)
json = request.json()


description = json["weather"][0]["description"]
print("Brisbane weather today is:", description)

temp_min = json.get("main").get("temp_min")
print("Temperature range is: ", temp_min, "minimum celsius.")

temp_max = json["main"]["temp_max"]
print("Maximum is: ", temp_max, "celsius.")