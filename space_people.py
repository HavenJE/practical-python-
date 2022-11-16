
# HTTP is how you communicate with web servers that host websites on the internet
# some websites return raw data, these raw data is returned under the API (application programming interface) for the website such as api.twitter.com

# JSON is a data format that is used to exchange data to/from a web server 

import requests

response = requests.get("http://api.open-notify.org/astros.json")
json = response.json()
print("The astronauts currently in space are:")

for person in json.get("people"):
    print(person.get("name"))