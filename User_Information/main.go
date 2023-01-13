package main

import (
    "fmt"
    "regexp"
    "strconv"
)

// Define a struct to store information for each individual
type person struct {
    firstName string
    lastName  string
    age       int
    occupation string
    streetNumber string
    address   string
}

func main() {
    // Initialize empty slice to store individuals' information
    var people []person

    // Prompt the user for the number of people to add
    var numPeople int
    fmt.Print("How many people would you like to add? ")
    fmt.Scan(&numPeople)

    for i := 0; i < numPeople; i++ {
        // Prompt for and validate first name
        var firstName string
        for {
            fmt.Print("What is the person's first name? ")
            fmt.Scan(&firstName)
            match, _ := regexp.MatchString("^[A-Za-z]*$", firstName)
            if !match {
                fmt.Println("Invalid input. Please enter a valid first name.")
            } else {
                break
            }
        }

        // Prompt for and validate last name
        var lastName string
        for {
            fmt.Print("What is the person's last name? ")
            fmt.Scan(&lastName)
            match, _ := regexp.MatchString("^[A-Za-z]*$", lastName)
            if !match {
                fmt.Println("Invalid input. Please enter a valid last name.")
            } else {
                break
            }
        }

        // Prompt for and validate age
        var ageStr string
        var age int
        for {
            fmt.Print("What is the person's age? ")
            fmt.Scan(&ageStr)
            match, _ := regexp.MatchString("^[0-9]*$", ageStr)
            if !match {
                fmt.Println("Invalid input. Please enter a valid age.")
            } else {
                age, _ = strconv.Atoi(ageStr)
                if age < 0 || age > 150 {
                    fmt.Println("Age must be between 0 and 150.")
                } else {
                    break
                }
            }
        }

        // Prompt for and validate occupation
        var occupation string
        for {
            fmt.Print("What is the person's occupation? ")
            fmt.Scan(&occupation)
            match, _ := regexp.MatchString("^[A-Za-z]*$", occupation)
            if !match {
                fmt.Println("Invalid input. Please enter a valid occupation.")
            } else {
                break
            }
        }

        // Prompt for and validate street number
        var streetNumber string
        for {
            fmt.Print("What is the person's street number? ")
            fmt.Scan(&streetNumber)
            match, _ := regexp.MatchString("^[0-9]*$", streetNumber)
            if !match {
                fmt.Println("Invalid input. Please enter a valid street number.")
            } else {
                break
            }
        }

        //
// Prompt for and validate address
        var address string
        for {
            fmt.Print("What is the person's address? ")
            fmt.Scan(&address)
            match, _ := regexp.MatchString("^[A-Za-z]*$", address)
            if !match {
                fmt.Println("Invalid input. Please enter a valid address.")
            } else {
                break
            }
        }

        // Create a new person struct and add it to the slice of people
        newPerson := person{firstName, lastName, age, occupation, streetNumber, address}
        people = append(people, newPerson)
    }

    // Print the slice of people
    fmt.Println(people)
}
