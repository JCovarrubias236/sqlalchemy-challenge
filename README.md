# SQL Alchemy Challenge
This repository will be used for the module 10 SQL Alchemy challenge.

## Description

I completed this climate analysis about Honolulu, Hawaii because I will be vacationing there soon. I have used Python and SQL Alchemy for the climate analysis and data exploration. To start the analysis, I analyzed the precipitation of Honolulu. To do this, I queried for the previous 12 months of precipitation and loaded the data into a pandas data frame. Once in the data frame, I sorted the values by date and created a data frame plot to see if there were any seasonal trends with how much and frequently it rains in Honolulu. Next in the analysis, I examined the stations that gathered the data for this database. First, I determined the total number of stations in the dataset. Then from there, I found the most active station in the dataset (the station with the most rows of data). I then filtered the dataset for the most active station and calculated the lowest, highest, and average temperatures. Again using the most active station, I grabbed its previous 12 months of precipitation data and created a histogram with 12 bars to fit the data into.

For the second part of this project, I used Flask within Python to create my very first API that housed static and dynamic routes. I created a homepage that displayed all the possible routes for this API and some instructions for the dynamic routes. My first route was using the previous query I created to retrieve the last 12 months of precipitation data. The results were printed as a dictionary with the date as the key and the precipitation value as the key value. The route is seen below:

```python
'/api/v1.0/precipitation'
```

My second route displayed a JSON list of all the stations in the database. The route is seen below:

```python
'/api/v1.0/stations'
```

My third and final static route displayed the query results of the last year of data for the most active station. 

```python
'/api/v1.0/tobs'
```

My first dynamic route returns a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start.

```python
'/api/v1.0/start_date/<start_date>'
```

My second dynamic route is fairly similar as it returns a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a start-end range.

```python
'/api/v1.0/start_date/<start_date>/end_date/<end_date>'
```

## Installation

Feel free to download the Python Jupyter Notebook file and the Python file I provided to run the project on your own.

For the Jupyter Notebook file you will need the following dependencies:

```python
%matplotlib inline
from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime as dt
```

For the Python file you will need the following dependencies:

```python
from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from scipy import stats
import numpy as np
import pandas as pd
import datetime as dt
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change/recommend.

## Authors and Acknowledgement

I solely worked on this project, however, I did utilize the AI tool provided by the Northwestern Bootcamp I am taking. I used this tool to help me with the first dynamic route using the start date and on. I then utilized the code from the first route and updated it to include an end date. I also used many Stack Overflow forums, SQL Alchemy documentation, and Flask documentation to resolve bugs in the code that I came across. (and there were plenty of errors I came across -_- haha)
