import csv

# specify the file path and column to search
file_path = 'data.csv'
column_to_search = 'column_name'
date_to_search = '2022-08-25T00:00:00.000Z'

original_line_count = 0 # variable to store the original line count
filtered_line_count = 0 # variable to store the filtered line count

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
            original_line_count += 1 # increment the original line count for each row
            # check if the specified column contains the specified date
            if row[column_to_search] != date_to_search:
                writer.writerow(row)
                filtered_line_count += 1 # increment the filtered line count for each row that is written

print(f'Number of lines in original file: {original_line_count}')
print(f'Number of lines in filtered file: {filtered_line_count}')
