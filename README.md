# Measure Air Quality in Spain
This project extracts air quality measurements, specifically *NO2*, *PM10* and *PM2.5*, from *september 2021* and 
*september 2022* thanks to OpenAQ API (*https://docs.openaq.org/reference/measurements_get_v2_measurements_get*).

## System Architecture
![Architecture of the project](architecture.png)


## Install prerequisites:

```shell 
pip install -r requirements.txt
```

## Load data into MongoDB
Make sure your mongo instance is up and running and that you have a local database with two collections created inside:
`openaq2021` and `openaq2022` where measurements from *2021* and *2022* will be loaded respectively.

Once that is done, follow the next steps:

### Worker
```shell
celery -A air_quality_spain worker -l info -P solo
```

### Celery
```shell
celery -A air_quality_spain call tasks.get_measures_september_2021
```

```shell
celery -A air_quality_spain call tasks.get_measures_september_2022
```

### Beat
```shell
celery -A air_quality_spain beat --pidfile= -l info -S django
```


## Visualise results on map

```shell
streamlit run main.py 
```

**Note** : To visualize specific results from specific parameters (*NO2*, *PM10*, *PM2.5*) and years (*2021*, *2022*) 
the `main.py` file needs to be modified and comment/uncomment only the necessary lines to draw the desired map.
