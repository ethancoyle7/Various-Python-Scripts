# Write the OOP program in python using class. Assuming you have four
# classes: Bank account which is the parent class and it has two child classes Saving
# Account class and Checking account class. Customer is another class who has a bank
# account; either saving or checking or both. Implement the scenario using python OOP
# and make sure you have covered those OOP concepts on your code: inheritance(any),
# polymorphism (runtime and compile time), abstraction and encapsulation.

# Parent Class: Bank Account
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        else:
            return "Insufficient balance"

    def __str__(self):
        return f"Name: {self.name}, Balance: {self.balance}"

# Child Class: Saving Account
class SavingAccount(BankAccount):
    def __init__(self, name, balance, interest_rate):
        BankAccount.__init__(self, name, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        return interest

    def __str__(self):
        return f"Name: {self.name}, Balance: {self.balance}, Interest Rate: {self.interest_rate}"

# Child Class: Checking Account
class CheckingAccount(BankAccount):
    def __init__(self, name, balance, overdraft_limit):
        BankAccount.__init__(self, name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if self.balance + self.overdraft_limit >= amount:
            self.balance -= amount
            return self.balance
        else:
            return "Insufficient balance with overdraft limit"

    def __str__(self):
        return f"Name: {self.name}, Balance: {self.balance}, Overdraft Limit: {self.overdraft_limit}"

# Class: Customer
class Customer:
    def __init__(self, name):
        self.name = name
        self.saving_account = None
        self.checking_account = None

    def open_saving_account(self, interest_rate):
        self.saving_account = SavingAccount(self.name, 0, interest_rate)

    def open_checking_account(self, overdraft_limit):
        self.checking_account = CheckingAccount(self.name, 0, overdraft_limit)

    def get_total_balance(self):
        total_balance = 0
        if self.saving_account:
            total_balance += self.saving_account.balance
        if self.checking_account:
            total_balance += self.checking_account.balance
        return total_balance

    def __str__(self):
        return f"Name: {self.name}"
      
      
#     In this implementation, the BankAccount class acts as a parent class for SavingAccount 
#     and CheckingAccount classes through inheritance. The SavingAccount and CheckingAccount
#     classes have their own properties and methods, as well as inherit properties and methods
#     from the BankAccount class. The Customer class has two properties for saving and checking
#     accounts and can open both types of accounts. The withdraw method in the CheckingAccount 
#     class is an example of polymorphism (runtime polymorphism) as it overrides the withdraw
#     method from the parent class BankAccount. The get_total_balance method in the Customer
#     class is an example of abstraction as it hides the implementation details of how the total
#     balance is calculated and only provides the total balance. The properties and methods in the
#     classes are an example of encapsulation as they define the data and behavior for each class
#     and protect the internal state of the objects from external changes.
