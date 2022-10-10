from crawler.helpers.mongodb import get_data_from_mongodb
from crawler.helpers.save_to_csv import save_csv
from crawler.helpers.draw_map import draw_map


if __name__ == '__main__':
    # --- 2021 --- #
    # Retrieve filtered data from database
    no2 = get_data_from_mongodb(parameter="no2", collection='openaq2021')
    pm10 = get_data_from_mongodb(parameter="pm10", collection='openaq2021')
    pm25 = get_data_from_mongodb(parameter="pm25", collection='openaq2021')

    # Save data in CSV files
    save_csv(data=no2, filename='no2_2021.csv')
    save_csv(data=pm10, filename='pm10_2021.csv')
    save_csv(data=pm25, filename='pm25_2021.csv')

    # Draw maps from CSV files
    draw_map(filename='no2_2021.csv')
    draw_map(filename='pm10_2021.csv')
    draw_map(filename='pm25_2021.csv')

    # --- 2022 --- #
    # Retrieve filtered data from database
    no2 = get_data_from_mongodb(parameter="no2", collection='openaq2022')
    pm10 = get_data_from_mongodb(parameter="pm10", collection='openaq2022')
    pm25 = get_data_from_mongodb(parameter="pm25", collection='openaq2022')

    # Save data in CSV files
    save_csv(data=no2, filename='no2_2022.csv')
    save_csv(data=pm10, filename='pm10_2022.csv')
    save_csv(data=pm25, filename='pm25_2022.csv')

    # Draw maps from CSV files
    draw_map(filename='no2_2022.csv')
    draw_map(filename='pm10_2022.csv')
    draw_map(filename='pm25_2022.csv')
