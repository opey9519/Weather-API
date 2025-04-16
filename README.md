# 🌤️ Weather API with Redis Caching

This project is a simple Flask-based API that fetches weather data for a given city using the Visual Crossing Weather API. To improve performance and reduce redundant API calls, it uses Redis to cache frequently accessed cities.

---

## 📦 Features

- Fetch current temperature data for any city
- Caches city data in Redis for 30 minutes
- Automatically serves from cache if available
- Simple frontend to input and view weather

---

## 🧰 Tech Stack

- **Backend:** Python, Flask
- **Caching:** Redis
- **Frontend:** HTML, JavaScript (Vanilla)
- **API Source:** [Visual Crossing Weather](https://www.visualcrossing.com/)

---

## ⚙️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/weather-api.git
cd weather-api
```
### 2. Create and activate a virtual environment (optional but recommended)
```bash
python3 -m venv weatherapi
source weatherapi/bin/activate
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Set up environment variables
```bash
WEATHER_API=your_visual_crossing_api_key
```
### 5. Start Redis server
```bash
redis-server
```
### 6. Run the Flask app
```bash
python app.py
```
