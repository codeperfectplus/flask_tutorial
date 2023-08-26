""" 
Title: Day 1: How to create a basic Flask application?
url: https://codeperfectplus.com/how-to-create-a-basic-flask-application
Published: 2023-08-26

Description: Simple Flask application to understand the basic concepts of Flask.
"""

from flask import Flask, jsonify

# Create a Flask app
app = Flask(__name__)


# Create a route for home page 
@app.route('/')
def home():
    return jsonify({'message': 'codeperfectplus.com'})


# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)