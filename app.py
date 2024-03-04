# Import the dependencies.
from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

import numpy as np
import pandas as pd
import datetime as dt

#################################################
# Database Setup
#################################################

# create engine to hawaii.sqlite
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################

# Home page
@app.route("/")
def home():
    print("Server received request for home page...")
    return (f"Welcome to my weather station page!<br/>"
            f"Available Routes:<br/>"
            f"/api/v1.0/precipitation<br/>"
            f"/api/v1.0/stations<br/>"
            f"/api/v1.0/tobs"
        )

# Precipitation
year_ago_date = dt.date(2017,8,23) - dt.timedelta(days=365)

year_ago_data = session.query(Measurement.date,Measurement.prcp).\
    filter(Measurement.date >= year_ago_date).\
    filter(Measurement.date <= dt.date(2017,8,23)).all()

precipitation = {}
for tuple in year_ago_data:
    precipitation[tuple[0]] = tuple[1]

@app.route("/api/v1.0/precipitation")
def precipitation_data():
    """Return the precipitation data as json"""
    return jsonify(precipitation)

# Stations
joined = session.query(Station.id,Measurement.station,Station.name,Station.latitude,Station.longitude,Station.elevation).join(Station, Measurement.station==Station.station).group_by(Measurement.station).order_by(Station.id).all()

stations_dict = {}
for tuple in joined:
     stations_dict[tuple[0]] = {
          'Station': tuple[1],
          'Name': tuple[2],
          'Latitude': tuple[3],
          'Longitude': tuple[4],
          'Elevation': tuple[5]
     }

@app.route("/api/v1.0/stations")
def stations_list():
    return jsonify(stations_dict)

# Tobs
year_ago_station_date = dt.date(2017,8,18) - dt.timedelta(days=365)

year_ago_station_data = session.query(Measurement.date,Measurement.tobs).\
    filter(Measurement.date >= year_ago_station_date).\
    filter(Measurement.date <= dt.date(2017,8,18)).\
    filter(Measurement.station == 'USC00519281').all()

temperature = {}
for tuple in year_ago_station_data:
    temperature[tuple[0]] = tuple[1]

@app.route("/api/v1.0/tobs")
def tobs():
    """Return the temperature data for the most active station as json"""
    return jsonify(temperature)

if __name__ == "__main__":
    app.run(debug=True)