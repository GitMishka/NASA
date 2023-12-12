from flask import Flask, jsonify
import requests
import config

app = Flask(__name__)

@app.route('/')
def home():
    return "NASA Data Dashboard Backend Running"

@app.route('/apod')
def apod():
    response = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={config.NASA_API_KEY}')
    data = response.json()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
