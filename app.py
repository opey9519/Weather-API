from flask import Flask
import requests

app = Flask(__name__)

# Hardcoded data to test API endpoints
local_weather = {
    'florida' : {
        'tampa' : {
            'temperature' : 70,
            'humidity' : '40%',
            'cloud' : None
        }
    }
}

@app.route('/')
def home():
    return '<h1>Let\'s find the weather! </h1>'

@app.route('/weather')
def get_weather():
    tampa = local_weather.get('florida').get('tampa')
    
    tampa_weather = f'In tampa it is {tampa.get('temperature')} degrees fahrenheit, with {tampa.get('humidity')} humidity and {'some clouds' if tampa.get('cloud') else 'no clouds'}'

    return tampa_weather

if __name__ == '__main__':
    app.run()