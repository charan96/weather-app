# Weather App

Simple command-line weather application to find the basic weather info such as temperature, humidity, wind, and cloudiness. We just enter the zipcode as an argument. I'm using the OpenWeatherMap API (free tier) to get the data, which limits to 60 API calls per hour. 

## How to Run

`python main.py <zipcode>`

I have a config.json file (not included) located in the repo that contains a `apikey` which is the key required to grab the data from the OWM API. If you'd like to run this application, sign up to get the API key from here: [https://openweathermap.org/appid]

The output looks like this:

| | |
| ----------- | --------
| Location    | New York
| Condition   | Clear
| Temperature | 38.2 F
| Wind        | 9.2 mph
| Humidity    | 72%
| Cloudiness  | 1%
