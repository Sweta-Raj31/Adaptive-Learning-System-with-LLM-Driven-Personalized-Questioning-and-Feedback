from flask import Flask
from dash import Dash
import dash_bootstrap_components as dbc
import pyrebase



# # Connect to Firebase:
config = { 
  "apiKey": "AIzaSyBQE9w5zbwZXF53-rG2FbLjew7X8boXGX4",
 "authDomain": "psychopathology-8db58.firebaseapp.com",
  "projectId": "psychopathology-8db58",
  "storageBucket": "psychopathology-8db58.appspot.com",
 "messagingSenderId": "1066656200790",
  "appId": "1:1066656200790:web:a7d2434f6a75badaf8a3f7",
 "measurementId": "G-Z72SKZEDR0",
 "databaseURL": ""
 
}
# Initialize Firebase
firebase = pyrebase.initialize_app(config)
db = firebase.database()

# Create a Flask server:
server = Flask(__name__)
server.config.from_pyfile('config.py')

# Create a Dash app:
app = Dash(__name__,
            server=server,
            routes_pathname_prefix='/dashboard/',
            external_stylesheets=[dbc.themes.LUX])


if __name__ == '__main__':
    from views import *
    app.run_server(debug=True)
