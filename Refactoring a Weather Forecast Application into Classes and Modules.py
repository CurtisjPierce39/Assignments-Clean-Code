# Weather Forecast Application Script
class WeatherDataFetcher:

    def __init__(self):
        self.weather_data = {
            "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50, "city": "New York"},
            "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65, "city": "London"},
            "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70, "city": "Tokyo"}
        }

    def fetch_weather_data(self, city):
        # Simulated function to fetch weather data for a given city
        print(f"Fetching weather data for {city}...")
        # Simulated data based on city
        return self.weather_data.get(city, {})

class DataParser:

    def __init__(self):
        self.data_fetcher = WeatherDataFetcher()

    def parse_weather_data(self, weather_data):
        # Function to parse weather data
        if not weather_data:
            return "Weather data not available"
        city = weather_data["city"]
        temperature = weather_data["temperature"]
        condition = weather_data["condition"]
        humidity = weather_data["humidity"]
        return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"

    def get_detailed_forecast(self, city):

        # Function to provide a detailed weather forecast for a city
        data = self.data_fetcher.fetch_weather_data(city)
        return self.parse_weather_data(data)
    
    def display_weather(self, city):

            # Function to display the basic weather forecast for a city
        data = self.data_fetcher.fetch_weather_data(city)
        if not data:
            print(f"Weather data not available for {city}")
        else:
            return data

class UserInterface:
    def main(self, get_detailed_forecast, display_weather):
        while True:
            city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
            if city.lower() == 'exit':
                print("Thank you for using the Weather Forecast App!")
                break
            detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
            if detailed == 'yes':
                forecast = get_detailed_forecast(city)
            else:
                forecast = display_weather(city)
            print(forecast)

if __name__ == "__main__":
    forecast_weather_data = WeatherDataFetcher()
    user_interface = UserInterface()
    data_parser = DataParser()
    user_interface.main(data_parser.get_detailed_forecast, data_parser.display_weather)