""" 
Title: Day 2: GET and POST request in Flask
url: https://codeperfectplus.com/get-and-post-request-in-flask
Published: 2023-08-27

Description: GET and POST request implementation in flask using python 3.
"""

from flask import Flask, jsonify, request

# Create a Flask app
app = Flask(__name__)

# sample superhero data
superheroes = [
    {
        "id": 1,
        "name": "Superman",
        "email": "superman@krypton.com",
        "age": 30,
        "secretIdentity": "Clark Kent"
    },
    {
        "id": 2,
        "name": "Batman",
        "email": "batman@cave.com",
        "age": 35,
        "secretIdentity": "Bruce Wayne"
    }
]

@app.route('/')
def home():
    return jsonify({'message': 'superheroes API'})

# GET request
@app.route('/superheroes', methods=['GET'])
def get_superheroes():
    return jsonify({'superheroes': superheroes})

# GET request with id
@app.route('/superheroes/<int:id>', methods=['GET'])
def get_superhero(id):
    return jsonify({'superhero': superheroes[id-1]})

# POST request
@app.route('/superheroes', methods=['POST'])
def add_superhero():
    name = request.form['name']
    email = request.form['email']
    age = request.form['age']
    secretIdentity = request.form['secretIdentity']
    get_data = {
        "id": len(superheroes)+1,
        "name": name,
        "email": email,
        "age": age,
        "secretIdentity": secretIdentity
    }
    print(get_data)
    superheroes.append(get_data)
    return jsonify({'superheroes': superheroes})


# driver function
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
