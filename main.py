import psycopg2
from flask import Flask, jsonify
import json

app = Flask(__name__) # setup initial flask app; gets called throughout in routes


@app.route('/') #python decorator 
def hello_world(): #function that app.route decorator references
  response = hello()
  return response

def hello():
  return "GIS 5572 Lab 1 pleaseeeeeee"

# Route to retrieve polygon as GeoJSON

if __name__ == "__main__":
    app.run(
      #debug=True, #shows errors 
      host='0.0.0.0', #tells app to run exposed to outside world
      port=8080)
