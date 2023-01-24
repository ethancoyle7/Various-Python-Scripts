import csv

def read_csv(file_name, column_name):
    data = []
    with open(file_name, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row[column_name])
    return data

def check_occurrence(data1, data2):
    results = {}
    for value in data1:
        if value in data2:
            if value in results:
                results[value] += 1
            else:
                results[value] = 1
    return results

file1 = input("Enter the name of the first CSV file: ")
column1 = input("Enter the name of the column in the first CSV file: ")
file2 = input("Enter the name of the second CSV file: ")
column2 = input("Enter the name of the column in the second CSV file: ")

data1 = read_csv(file1, column1)
data2 = read_csv(file2, column2)

results = check_occurrence(data1, data2)

for value, count in results.items():
    print(f"{column1}: {value} occured: {count} times")
# This script prompts the user to enter the name of the two CSV files, and the name of the columns to be read. Then it uses the read_csv function to read the specified column of the first CSV file, and store all the values of that column in a list (data1).
# It then reads the second CSV file in the same way and store all the values of the specified column in a list (data2).
# Then it uses the check_occurrence function to compare the data1 and data2 list, it iterates over data1 and checks if the value is in data2 and if it is, it increments the count in the results dictionary.
# At the end of the process, script prints out the column name, the value and the count of how many times it occured in the second CSV file.
