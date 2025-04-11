from flask import Flask, request, jsonify
import requests
from dotenv import load_dotenv
import os

load_dotenv()  # Brings all environment variables from .env into os.environ
app = Flask(__name__)

API_KEY = os.getenv('WEATHER_API')


@app.route('/')
def home():
    return '<h1>Let\'s find the weather! </h1>'

# Get weather data for specified location using query parameters
@app.route('/weather/<location>', methods=['GET'])
def get_weather(location):

    URL = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}?key={API_KEY}'

    try:
        response = requests.get(URL)
        if response.status_code == 200:
            data = response.json()
            return jsonify({'temp': data.get('days')[0].get('temp')}), 200
        else:
            return jsonify({'error' : 'could not fetch data'}), response.status_code

    except requests.exceptions.RequestException as e:
        return jsonify({'error' : f"Error: {e}"}), 500


if __name__ == '__main__':
    app.run()
