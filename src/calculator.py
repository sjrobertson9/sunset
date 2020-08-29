import requests

print(">>> Getting location data...")

ips_response = requests.get("http://api.ipstack.com/check?access_key=adab7fe0178697d5ffacb44af49876d4")

print(ips_response.json())

# GET INFO FOR WEATHER API

ips_data = ips_response.json()
city = ips_data["city"]
state = ips_data["region_name"]

print(">>> Getting weather data...")

key = "7aa9e7efe97e40ea07757dbf0c02b044"
url = "http://api.openweathermap.org/data/2.5/"
params = "?q=" + city + "," + state + "&units=imperial&appid="

complete_url = url + "weather" + params + key

opw_response = requests.get(complete_url)

print(opw_response.json())
