import click

from config import Config
from url_constructor import URLConstructor
from weather_app import WeatherApp


@click.command()
@click.argument('zipcode')
def main(zipcode):
	config = Config("../config.json")

	weather_app = WeatherApp(config)
	print(weather_app.get_weather(zipcode))

if __name__ == "__main__":
    main()
