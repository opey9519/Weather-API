from flask import Flask, request, jsonify
from dotenv import load_dotenv
from flask_cors import CORS
import requests
import os
import redis

load_dotenv()  # Brings all environment variables from .env into os.environ
app = Flask(__name__)
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

CORS(app)

API_KEY = os.getenv('WEATHER_API')
if not API_KEY:
    raise EnvironmentError("WEATHER_API key not set in .env file!")

# Get weather data for specified location using query parameters


@app.route('/weather/<location>', methods=['GET'])
def get_weather(location):
    if r.exists(location):
        temp_data = r.get(location)  # Access cache
        print('cache accessed')
        return jsonify({'temp': temp_data}), 200

    URL = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}?key={API_KEY}'

    try:
        response = requests.get(URL)
        if response.status_code == 200:
            data = response.json()
            # Store temperature data from city
            temp_data = data.get('days')[0].get('temp')
            r.set(location, temp_data, ex=1800)  # Cache

            return jsonify({'temp': temp_data}), 200
        else:
            return jsonify({'error': 'could not fetch data'}), response.status_code

    except requests.exceptions.RequestException as e:
        return jsonify({'error': f"Error: {e}"}), 500


if __name__ == '__main__':
    app.run()
