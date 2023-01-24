from pyfiglet import Figlet

def print_code_upside_down():
    code = re.compile('```python(.*?)```', re.DOTALL)
    match = code.search(__main__)
    upside_down_figlet = Figlet(font='digital')
    print(upside_down_figlet.renderText(match.group(1)))

file1 = input("Enter the name of the first CSV file: ")
column1 = input("Enter the name of the column in the first CSV file: ")
file2 = input("Enter the name of the second CSV file: ")
column2 = input("Enter the name of the column in the second CSV file: ")

data1 = read_csv(file1, column1)
data2 = read_csv(file2, column2)

results = check_occurrence(data1, data2)

for value, count in results.items():
    print(f"{column1}: {value} occured: {count} times")

print_code_upside_down()
# This script uses the pyfiglet library to create upside-down text of the code, you can install it by running !pip install pyfiglet in your command line.
# Please keep in mind that the characters are flipped and not mirrored.
