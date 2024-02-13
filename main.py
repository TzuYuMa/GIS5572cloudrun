import psycopg2
from flask import Flask, jsonify
import json

app = Flask(__name__) # setup initial flask app; gets called throughout in routes

# Connect to the PostgreSQL database

pgSQL_connect = {
    'dbname':"gis5572",
    'user':"postgres",
    'password':"19950920840920Yu",
    'host':"34.133.74.255",
    'port':"5432"
}


@app.route('/') #python decorator 
def hello_world(): #function that app.route decorator references
  response = hello()
  return response

def hello():
  return "GIS 5572 Lab 1 pleaseeeeeee"

# Route to retrieve polygon as GeoJSON
@app.route('/getgeojson', methods=['GET'])
def get_geojson():
    # Connect to the database
    connection = psycopg2.connect(**pgSQL_connect)
    cursor = connection.cursor()

    # Query to retrieve polygon as GeoJSON
    query = "SELECT ST_AsGeoJSON(geometry) FROM polygon_lab1;"
    cursor.execute(query)
    rows = cursor.fetchall()

    # Close database connection
    cursor.close()
    connection.close()

    # Prepare GeoJSON response
    features = []
    for row in rows:
        feature = {
            "type": "Feature",
            "geometry": json.loads(row[0]),
            "properties": {}
        }
        features.append(feature)

    feature_collection = {
        "type": "FeatureCollection",
        "features": features
    }

    # Return GeoJSON response
    return jsonify(feature_collection)

if __name__ == "__main__":
    app.run(
      #debug=True, #shows errors 
      host='0.0.0.0', #tells app to run exposed to outside world
      port=8080)
