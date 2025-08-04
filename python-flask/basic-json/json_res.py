"""
Script Name : json_res.py
Description : Build a basic route that returns JSON response
Author      : @tonybnya
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def json_response():
    json = {
      "name": "Tony",
      "age": 39,
      "role": "Software Engineer",
      "skills": ["dsa", "web dev", "system design"],
      "address": {
        "street": "Ndogbong, carrefour Bifaga",
        "city": "Douala",
        "country": "Cameroon",
        "zipCode": "00000"
      }
    }
    # return json
    return f"<pre>{json}</pre>"
