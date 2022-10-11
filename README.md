# Measure Air Quality in Spain Sept. 2021 and Sept. 22
This project extracts air quality measurements, specifically *NO2*, *PM10* and *PM2.5*, from *september 2021* and 
*september 2022* thanks to OpenAQ API (*https://docs.openaq.org/reference/measurements_get_v2_measurements_get*).

## System Architecture
![Architecture of the project](architecture.png)


## Install prerequisites:

```shell 
pip install -r requirements.txt
```

## MongoDB
Make sure your mongo instance is up and running and that you have a local database with two collections created inside:
`openaq2021` and `openaq2022` where measurements from *2021* and *2022* will be loaded respectively.

If you don't have it yet, open a new terminal and run the following:

```shell
mongosh
```

```shell
use local
```

```shell
db.createCollection("openaq2021")
```

```shell
db.createCollection("openaq2022")
```

### Load data
In `main.py` file, comment everything under  `if __name__ == '__main__':` except lines **10** and **29** that are the
ones that will load the data extracted from OpenAQ API into our MongoDB collections.

Execute the `main.py` file:
```shell
python main.py
```

To check that the data has been loaded correctly go back to the mongo terminal and type:

```shell
db.openaq2021.find().count()
```

```shell
db.openaq2022.find().count()
```

Both commands must return a number greater than 0, which means the mongo collections have measurements data inside.

### Filter data from MongoDB and save average values in CSV file
Comment lines **10** and **29** again and uncomment lines **13, 14, 15, 18, 19, 20** to query data from mongodb by 
parameter from collection `opeanaq2021`. Automatically, this data will grouped by location and average value, and 
finally  saved in a CSV file under the `files` folder to use it later to draw the heated map. Run the `main.py` file
to execute the code.

Once done, comment those lines again and uncomment the ones related to 2022 and execute the code again to save the 
results related to september 2022 in this case.

Now, all CSV files are ready to be used to draw the heated maps using `Streamlit`.

## Streamlit for heat map drawing
Comment everything under `if __name__ == '__main__':` if not done. Uncomment only one line at a time that executes the 
`draw_map()` function to visualise the results on each parameter (NO2, PM10, PM2.5) and year (2021, 2022). In this case,
to visualise the map run the following:

```shell
streamlit run main.py
```

The web browser will open a new tab where the map will be drawn and a table under the map showing the CSV file will also
be shown.

**Note**: The MongoDB data loading and filtering it's only necessary to be done the first time as the collections are 
empty at the beginning, for the following times only the execution of the map visualisation using `streamlit` is 
necessary and not the whole process.


## Project Structure
### crawler folder
This folder contains two subfolders, `helpers` and `wrappers`. The `helpers` folder contains functions to help through 
the process of map drawing, mongodb connection and save to csv. The `wrappers` folder manages the API calls to extract
data from OpenAQ and personalised exceptions. Under `openaq.py` the endpoints are specified. In this case, there are two
endpoints, one for each year (2021, 2022). 

### files folder
This folder is mainly used to save the csv files from the data queried against mongodb that will be used to draw the map.

### tasks folder
In this folder pagination is managed to extract all existing records from the API and logs are also placed in order to 
monitor the data extraction to avoid errors. The file `openaq.py` executes the endpoints from the `crawler` folder and 
saves the data in `MongoDB` using the defined `writers`.

### tests folder
Here are the tests to test the connection with the OpenAQ API. Status 200 means the connection was successful.

### writers folder
This folder manages the data writing into `MongoDB` database using the `mongodb.py` helper file from `crawler/helpers` folder.


## Conclusion
Once you have all the map images from 2021 and 2022 and all parameters (NO2, PM10, PM2.5) you can compare and analyse 
the differences between each year and what has changed or improved/not improved. Also, you can have a look at the worst 
locations with air quality and think about a reason (big city, pollution, big industries around, ...)
