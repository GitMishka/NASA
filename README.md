NASA Space Exploration Dashboard Documentation Overview

This web application, titled "NASA Space Exploration Dashboard," provides a daily display of NASA's Astronomy Picture of the Day (APOD). 
It uses a Python Flask backend to fetch data from the NASA API and an Nginx server for frontend hosting.
Technology Stack

    Backend: Python, Flask
    Frontend: HTML, CSS, JavaScript
    Server: Nginx
    Containerization: Docker

Installation

    Clone the repository.
    Build the Docker container using the provided Dockerfile.

Usage

    The Flask backend serves at http://127.0.0.1:5000/.
    Access the Astronomy Picture of the Day at http://127.0.0.1:5000/apod.
    The frontend displays the APOD image, title, and description.
