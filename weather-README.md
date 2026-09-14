# 🌤️ Weather API

A simple **Python weather application** that fetches real-time weather data for a city using the **Open-Meteo API**.

The user enters a city name, and the program retrieves its geographical coordinates and displays the current weather information.

## 🚀 Features

* 🌍 Search for a city by name
* 📍 Get the city's latitude and longitude using the Open-Meteo Geocoding API
* 🌡️ Display the current temperature
* 💨 Display wind speed
* 💧 Display humidity
* ☀️ Display the current weather condition
* 🔗 Fetch data from a REST API using Python

## 🛠️ Technologies Used

* **Python**
* **Requests**
* **REST API**
* **Open-Meteo API**
* **JSON**

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/weather-api.git
```

Go to the project folder:

```bash
cd weather-api
```

Install the required library:

```bash
pip install requests
```

## ▶️ How to Run

Run the Python file:

```bash
python app.py
```

Enter a city when prompted:

```text
Enter a city: Rabat
```

Example output:

```text
=== Weather in Rabat ===

Temperature: 24.5 °C
Wind speed: 12.3 km/h
Humidity: 58 %
Condition: Mainly clear 🌤️
```

## 🔌 API

This project uses **Open-Meteo**, a free weather API that provides weather and geocoding data.

* Geocoding API: Converts a city name into latitude and longitude.
* Weather API: Uses these coordinates to retrieve current weather data.

## 📚 What I Learned

Through this project, I practiced:

* Making HTTP requests with Python
* Working with REST APIs
* Processing JSON responses
* Extracting data from nested dictionaries
* Using user input
* Building URLs dynamically
* Handling data received from an external API

## 🔮 Future Improvements

Possible improvements for future versions:

* Add more weather conditions
* Handle invalid city names
* Add error handling for API requests
* Display the country of the searched city
* Add a graphical user interface
* Add a multi-day weather forecast

## 📄 License

This project is for learning and educational purposes.
