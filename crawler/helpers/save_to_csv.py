import csv


def save_csv(data: list, filename: str):
    """
        This function calculates the current air quality by city, being the air quality defined as the average of the
        measurements. It creates a csv file with these results.
    :param data: Result list from the query against the MongoDB database
    :param filename: Name of the file where to write the final result
    """
    values = []
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["location", "city", "lat", "lng", "avg_val", "count_measurements"])
        current_loc = data[0]['location']
        lat = data[0]['coordinates']['latitude']
        lon = data[0]['coordinates']['longitude']
        city = data[0]['city']

        for message in data:
            message_loc = message['location']
            lat = message['coordinates']['latitude']
            lon = message['coordinates']['longitude']
            city = message['city']
            if current_loc == message_loc:
                values.append(float(message['value']))
            else:
                values.append(float(message['value']))
                avg = sum(values) / len(values)
                writer.writerow([current_loc, city, lat, lon, avg, len(values)])
                current_loc = message_loc
                lat = message['coordinates']['latitude']
                lon = message['coordinates']['longitude']
                city = message['city']
                values = []  # Empty array for new iteration
                values.append(float(message['value']))

        # Write last city
        avg = sum(values) / len(values)
        writer.writerow([current_loc, city, lat, lon, avg, len(values)])
