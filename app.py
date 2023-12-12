from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "NASA Data Dashboard Backend Running"

if __name__ == '__main__':
    app.run(debug=True)
