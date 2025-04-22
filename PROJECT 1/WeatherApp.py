import os
import requests

# Warna untuk terminal
RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

# Mapping ikon cuaca berdasarkan deskripsi
weather_icons = {
    "clear sky": "☀",
    "few clouds": "🌤",
    "scattered clouds": "⛅",
    "broken clouds": "☁",
    "shower rain": "🌧",
    "rain": "🌧",
    "thunderstorm": "⛈",
    "snow": "❄",
    "mist": "🌫"
}

def get_weather(city):
    api_key = "9e88bd7a61bd268781b90e0fa8548f3b"  # Ganti dengan API key OpenWeatherMap
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            weather_desc = data["weather"][0]["description"]
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]

            # Ambil ikon cuaca berdasarkan deskripsi
            icon = weather_icons.get(weather_desc.lower(), "🌍")

            # Format output lebih menarik
            result = f"""
{CYAN}========================={RESET}
{GREEN}🌎 Cuaca di {city.title()} {RESET}
{CYAN}========================={RESET}
{icon} {YELLOW}{weather_desc.capitalize()}{RESET}
🌡 Suhu: {temp}°C
💧 Kelembaban: {humidity}%
🌬 Kecepatan Angin: {wind_speed} m/s
"""
            return result
        else:
            return f"{RED}Kota tidak ditemukan atau terjadi kesalahan.{RESET}"
    
    except requests.exceptions.RequestException as e:
        return f"{RED}Terjadi kesalahan: {e}{RESET}"

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    city = input("Masukkan nama kota: ")
    print(get_weather(city))