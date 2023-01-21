import csv

# specify the file path and column to search
file_path = 'file.csv'
column_to_search = 'column_name'
date_to_search = '2022-08-25T00:00:00.000z'

# read the CSV file
with open(file_path, 'r') as file:
    reader = csv.DictReader(file)

    # create a new CSV file to write the filtered rows
    with open('filtered_' + file_path, 'w', newline='') as filtered_file:
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(filtered_file, fieldnames=fieldnames)
        writer.writeheader()

        # iterate through the rows in the CSV file
        for row in reader:
            # check if the specified column contains the specified date
            if row[column_to_search] != date_to_search:
                writer.writerow(row)
