import requests
import datetime

### SOURCING API

def get_weather():
    # GET INFO FOR WEATHER API
    ips_response = requests.get("http://api.ipstack.com/check?access_key=adab7fe0178697d5ffacb44af49876d4")
    ips_data = ips_response.json()
    city = ips_data["city"]
    state = ips_data["region_name"]
    
    # GET WEATHER VALUES
    key = "7aa9e7efe97e40ea07757dbf0c02b044"
    url = "http://api.openweathermap.org/data/2.5/"
    params = "?q=" + city + "," + state + "&units=imperial&appid="
    complete_url = url + "weather" + params + key

    opw_response = requests.get(complete_url)

    # RETURN RELEVANT VALUES
    return make_weather(opw_response.json())

### SCORE CALCULATION

# weather : dictionary of relevant values
def calculate_score(weather):
    return calculate_icon(weather["icon"]) + calculate_pressure(weather["pressure"]) + calculate_humidity(weather["humidity"]) \
             + calculate_visibility(weather["visibility"]) + calculate_clouds(weather["clouds"])

# icon : visual symbol of weather
def calculate_icon(icon):
    return icon_scores[icon]

# pressure : air pressure in hPa
def calculate_pressure(pressure):
    if pressure > 1000:
        return 8
    elif pressure < 1000:
        return 3
    else: 
        return 5

# humidity : air humidity as a %
def calculate_humidity(humidity):
    if humidity > 50:
        return 3
    elif humidity < 50: 
        return 8
    else:
        return 5

# visibility : visible distance in feet
def calculate_visibility(visibility):
    if visibility > 10000:
        return 8
    elif visibility < 10000:
        return 3
    else:
        return 5

# clouds : cloud cover as a %
def calculate_clouds(clouds):
    if clouds < 25:
        return 8
    elif clouds < 50:
        return 5
    elif clouds < 75:
        return 3

# score : how good is da sunset
def interpret_score(score):
    if 30 < score <= 40:
        return "EXCELLENT"
    elif 20 < score <= 30:
        return "GOOD"
    elif 10 < score <= 30:
        return "MEDIOCRE"
    else:
        return "ayo that shit SUCKS"
    

### PARSING

def make_weather(json):
    weather = {
        'icon'       : parse_icon(json['weather'][0]['icon']),
        'pressure'   : json['main']['pressure'],
        'humidity'   : json['main']['humidity'],
        'visibility' : json['visibility'],
        'clouds'     : json['clouds']['all'],
        'sunset'     : parse_sunset(json['sys']['sunset'])
    }
    return weather

# icon ex: "10n.png"
def parse_icon(icon):
    return icon.strip('dn')

# turns it to normal time
def parse_sunset(sunset):
    time = datetime.datetime.fromtimestamp(sunset)
    return time.strftime('%H:%M:%S')


### DICTIONARIES

# NOTE: if i ever decided to expand, a more comprehensive list could be
#       created by using the weather condition code IDs
icons = {
    '01' : 'clear sky',
    '02' : 'few clouds',
    '03' : 'scattered clouds',
    '04' : 'broken clouds',
    '09' : 'shower rain',
    '10' : 'rain',
    '11' : 'thunderstorm',
    '13' : 'snow',
    '50' : 'mist'
}

icon_scores = {
    '01' : 5, # clear sky
    '02' : 6, # few clouds
    '03' : 7, # scattered clouds
    '04' : 8, # broken clouds
    '09' : 2, # shower rain
    '10' : 2, # rain
    '11' : 3, # thunderstorm
    '13' : 3, # snow
    '50' : 5  # mist
}

