
"""
   Welcome to Elite 101 — this program is a starter for your chatbot project.
   The starter prompts the user to enter their name and then greets them with a personalized message.

   Functions:
       get_user_name(): Prompts the user to enter their name and returns it.
       greet_user(name): Prints a time-based greeting message using the provided name.
       main(): Main function that orchestrates the user input and greeting process.

   Execution:
       When the script is run directly (not imported as a module), it will execute the main() function.
"""

from datetime import datetime


def get_user_name():
    #Asks the user to enter their name and returns it.
    name = input("Welcome to Baffour Banking, please enter your first and last name: ")
    return name.strip()


def greet_user(name):
    #Greeting based on the time of the day.
    hour = datetime.now().hour

    if hour < 12:
        greeting = "Good morning"
    elif hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"                                              #fix time of day greeting

    print(f"{greeting}, {name}! Welcome to Baffour Banking.\n")


def create_account(name, account_type, min_age=13):
    #The process of actually creating the account.

    print(f"Let's get started with your {account_type}.\n")
    age = int(input(f"Hello, {name}! How old are you? "))

    if age < 13:
        print(f"Sorry {name}, you must be at least {min_age} years old to open a {account_type}")
        return #if user is too young

    phone = input("Enter your phone number: ")
    email = input("Enter your email address: ")
    password = input("Create a password for your account: ")
    ssn = input("Enter your Social Security Number (SSN): ")

    print(f"{name}, your {account_type} has been created.")

def main():
    #Main function
    name = get_user_name()
    greet_user(name)

    options = input(
        "How can I assist you today?\n"
        "--------------------------------------------------------\n"
        "Please choose from the following options:\n"
        "1. I would like to open a Checking Account.\n"
        "2. I would like to open a Savings Account.\n"
        "3. I would like to open a Credit Card.\n"
        "4. I would like to speak to a customer representative.\n"
        "Enter your choice (1-4): "
    )

    if options == "1":
        create_account(name, "Checking Account", min_age=13)


    elif options == "2":
        create_account(name, "Savings Account", min_age=13)

    elif options == "3":
        create_account(name, "Credit Card", min_age=18)

    elif options == "4":
        print(f"Connecting you to a customer representative, {name}... Please wait.")

    else:
        print("Invalid option. Please restart and choose a valid option (1-4).")

if __name__ == "__main__":
    main()
