import requests
import datetime

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

# weather = dictionary of relevant values
def get_score(weather):
    # return dictionary of values
    pass


def make_weather(json):
    weather = {
        'icon'       : parse_icon(json['weather'][0]['icon']),
        'pressure'   : json['main']['pressure'],
        'humidity'   : json['main']['humidity'],
        'visibility' : json['visibility'],
        'wind'       : json['wind']['speed'],
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