import re

# Initialize empty list to store individuals' information
people = []

# Prompt the user for the number of people to add
num_people = int(input("How many people would you like to add? "))

for i in range(num_people):
    # Prompt for and validate first name
    while True:
        first_name = input("What is the person's first name? ")
        if not re.match("^[A-Za-z]*$", first_name):
            print("Invalid input. Please enter a valid first name.")
        else:
            break

    # Prompt for and validate last name
    while True:
        last_name = input("What is the person's last name? ")
        if not re.match("^[A-Za-z]*$", last_name):
            print("Invalid input. Please enter a valid last name.")
        else:
            break

    # Prompt for and validate age
    while True:
        age = input("What is the person's age? ")
        if not re.match("^[0-9]*$", age):
            print("Invalid input. Please enter a valid age.")
        else:
            age = int(age)
            if age < 0 or age > 150:
                print("Age must be between 0 and 150.")
            else:
                break

    # Prompt for and validate occupation
    while True:
        occupation = input("What is the person's occupation? ")
        if not re.match("^[A-Za-z]*$", occupation):
            print("Invalid input. Please enter a valid occupation.")
        else:
            break

    # Prompt for and validate street number
    while True:
        street_number = input("What is the person's street number? ")
        if not re.match("^[0-9]*$", street_number):
            print("Invalid input. Please enter a valid street number.")
        else:
            break

    # Prompt for and validate address
    while True:
        address = input("What is the person's address? ")
        if not re.match("^[A-Za-z]*$", address):
            print("Invalid input. Please enter a valid address.")
        else:
            break

    # Add the individual's information to the list
    person = {
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
        "occupation": occupation,
        "street_number": street_number,
        "address": address
    }
    people.append(person)

# Print the list of people
print(people)
