# BEGINNING #

# initialize points with 0
points = 0
def main():
    global points
    points += 1

# output a message for the user before starting the tasks
print("Welcome to the Supermarket Survivor!")
# use this to print an empty line
print()

# make the list with the tasks that need to be done in order to escape the simulator
list = ["1. File Extensions",
        "2. Math Interpreter",
        "3. Meal Time",
        "4. Nutrition Facts",
        "5. Coke Machine",
        "6. CamelCase",
        "7. Outdated",
        "8. Guessing Game",
        "9. Bitcoin Index",
        "10. Emojize",
        "11. Exit"
        ]

print("You have to complete all of these tasks in order to escape the supermarket simulator:")
# use a for loop to print the list in order
for i in range (11):
    print(list[i])

# use this to print an empty line
print()


#
# 1ST TASK: FILE EXTENSIONS #
#

print("TASK NUMBER 1: FILE EXTENSIONS")
# ask for input to check the file
file = input("Input file name: ")
# make it lower and without spaces
file = file.lower().strip()

# check the end of the string and output the type of the file it is
if (file.endswith(".gif")):
    print("image/gif")
elif(file.endswith(".jpg") or file.endswith(".jpeg")):
    print("image/jpeg")
elif(file.endswith(".png")):
    print("image/png")
elif(file.endswith(".pdf")):
    print("application/pdf")
elif(file.endswith(".txt")):
    print("text/plain")
elif(file.endswith(".zip")):
    print("application/zip")
# if the file type doesn't match, show this
else:
    print("application/octet-stream")
    # if the type of file is not on the list, points = -1

# if the type of file was not on the list, the points become 0 again
# if it was on the list, the points become 1
# it's an easier approach
points += 1

print(f"Points: {points}")
print()


#
# 2ND TASK: MATH INTERPRETER #
#


import random

print("You encounter a vault with a mathematical puzzle. Solve it to unlock the vault.")

levels = [
    ("2 + 3 * 4", 14),
    ("(5 + 3) / 2", 4),
    ("10 - 2 * 3 + 1", 5),
    ("2 ** 3 + 4", 12),
]

for expression, answer in levels:
    print(f"Solve: {expression}")

    # loop used to constantly check if the answer is a number or not
    while True:
        user_answer = input("Your answer: ")

        # check if the input is a valid number
        if user_answer.replace(".", "").isdigit():  # allows floats
            user_answer = float(user_answer)
            break  # exit the loop if the input is valid

        else:
            print("Invalid input. Please enter a number.")

    # Check if the user's answer is correct
    if user_answer == answer:
        points += 1


print(f"Points: {points}")
print()



#
# 3RD TASK: MEAL TIME #
#


print("TASK NUMBER 3: MEAL TIME")

# implement a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time

def main():

    #loop to constantly check if the time is entered correctly
    while True:
        # ask for input hour
        time = input("What time is it? (HH:MM) ")

        # validate the input format
        if ":" in time and len(time.split(":")) == 2:
            hours, minutes = time.split(":")
            if hours.isdigit() and minutes.isdigit():
                hours = int(hours)
                minutes = int(minutes)
                if 0 <= hours < 24 and 0 <= minutes < 60:
                    # convert the input time to a float representing hours
                    final_time = convert(time)

                    # check for the correct hours and print the corresponding meal time
                    if 7.0 <= final_time <= 8.0:
                        print("breakfast time")
                        points+=1
                    elif 12.0 <= final_time <= 13.0:
                        print("lunch time")
                        points+=1
                    elif 18.0 <= final_time <= 19.0:
                        print("dinner time")
                        points+=1
                    else:
                        print("It's not meal time.")
                    break  # exit the loop after processing the valid input

                # if the input is invalid, reprompt the user
                print("Invalid time format. Please enter a valid time in HH:MM format.")



def convert(time):
    # split the time into hours and minutes
    hours, minutes = time.split(":")

    # convert hours and minutes to integers
    hours = int(hours)
    minutes = int(minutes)

    # used to convert the time into a single float value
    # dividing the minutes by 60 converts them into a fractional part of an hour
    # 2 hours and 30 minutes becomes 2 + (30 / 60) = 2 + 0.5 = 2.5 hours
    final_time = hours + (minutes / 60)

    # returning the float number so I can use it in def main()
    return final_time

if __name__ == "__main__":
    main()

print(f"Points: {points}")
print()



#
# 4TH TASK:  NUTRITION FACTS #
#


print("TASK NUMBER 4: NUTRITION FACTS")

# prompt user for input fruit
# make it lowercase
fruit = input("Enter a fruit: ").lower()

# dictionary of fruits and their calorie counts (per FDA poster)
fruit_calories = {
    'apple': 130,
    'avocado': 50,
    'banana': 110,
    'cantaloupe': 50,
    'grapefruit': 60,
    'grapes': 90,
    'honeydew melon': 50,
    'kiwifruit': 90,
    'lemon': 15,
    'lime': 20,
    'nectarine': 60,
    'orange': 80,
    'peach': 60,
    'pear': 100,
    'pineapple': 50,
    'plums': 70,
    'strawberries': 50,
    'sweet cherries': 100,
    'tangerine': 50,
    'watermelon': 80
}


# check if the fruit is in the dictionary
if fruit in fruit_calories:
    # output its calories
    print(f"Calories: {fruit_calories[fruit]}")
    # another way is to concatenate strings and variables using the + operator
    # print("Calories: " + str(fruit_calories[fruit]))
else:
    # make a loop that continously prompts user for input until it s a correct one
    while fruit not in fruit_calories:
        fruit = input("Enter a fruit: ").lower()

points += 1

# another method of solving it is by making 20 different booleans
print(f"Points: {points}")
print()



#
# 5TH TASK: COKE MACHINE #
#


print("TASK NUMBER 5: COKE MACHINE")

# inform customer about the amount due
print("Amount Due: 50 Cents.")

# accepted coin denominations
accepted_coins = [25, 10, 5]

# initialize the total amount paid
total_paid = 0

# keep asking for coins until the amount due is met or exceeded
while total_paid < 50:
    # calculate the remaining amount due
    amount_due = 50 - total_paid

    # inform the user of the amount due
    print(f"Amount Due: {amount_due}")
    # another way of writing this is w two print()
    # first one w the message
    # 2nd one with the amount due as an int

    # prompt user to insert a coin
    new_coin = int(input("Insert Coin: "))

    # check if the coin is valid, from the list
    if new_coin in accepted_coins:
        # add the coin to the total amount paid
        total_paid += new_coin
        # every time user enters a correct coin, he earns a points
        points += 1
    else:
        # if the coin is invalid, ignore it and inform the user
        print("Invalid coin. Please insert a valid coin (25, 10, or 5 cents).")


# if the total paid is 50 cents or more, calculate change owed
if total_paid >= 50:
    change_owed = total_paid - 50
    print(f"Change Owed: {change_owed}")

print(f"Points: {points}")
print()



#
# 6TH TASK: CAMELCASE"
#


print("TASK NUMBER 6: CAMELCASE")

# prompt user for input
camelCase = input("camelCase: ")

# strings in Python are immutable
# build a new string
# making function for snake_case
def snake_case(camelCase):
    # create an empty string to build the result
    snake_case = ""

    # iterate over each character in the string
    for i in camelCase:
        if (i.isupper()):
            # if it finds a character that is uppercase, add the underline, then the word lowercase
            snake_case += "_" + i.lower()
        else:
            # if character is lowercase, keep it like that
            snake_case += i
    return snake_case

# output the result
# pass in the camelCase string as an argument
print("snake_case:", snake_case(camelCase))
points += 1


print(f"Points: {points}")
print()


#
# 7TH TASK: OUTDATED #
#

from datetime import datetime

def get_valid_date():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]


    while True:
        # prompt the user until a valid date is entered
        # remove leading/trailing spaces by using .strip()
        date = input("Date (month-day-year order): ").strip()

        # check if the input contains slashes (MM/DD/YYYY format)
        if "/" in date:
            # split the input into month, day, and year using "/"
            parts = date.split("/")
            # check if month, day, and year are all digits
            if len(parts) == 3:
                month, day, year = parts
                if month.isdigit() and day.isdigit() and year.isdigit():
                    # if yes, turn them into integers
                    month = int(month)
                    day = int(day)
                    year = int(year)
                    # validate the month, day, and year ranges
                    if (1 <= month <= 12 and 1 <= day <= 31 and 1 <= year <= 9999):
                        # return the date in YYYY-MM-DD format
                        return f"{year:04}-{month:02}-{day:02}"

        # check if the input contains a space and a comma (Month Day, Year format)
        elif " " in date and "," in date:
            # split the input into month_day and year using the comma
            month_day, year = date.split(",")
            # remove any leading/trailing spaces from month_day and year
            month_day = month_day.strip()
            year = year.strip()
            # check if the first part of month_day is a valid month name
            if month_day.split()[0] in months:
                # split month_day into month and day using the space
                month, day = month_day.split()
                # check if day and year are digits
                if day.isdigit() and year.isdigit():
                    day = int(day)
                    year = int(year)
                    # get the index of the month in the months list and add 1 (since list indices start at 0)
                    month_index = months.index(month) + 1
                    if (1 <= day <= 31 and 1 <= year <= 9999):
                        # return the date in YYYY-MM-DD format
                        return f"{year:04}-{month_index:02}-{day:02}"

        # if the input doesn't match any valid format
        print("Invalid date format. Please use month-day-year or month/day/year.")


# make a function for certain expired items
def filter_expired_groceries():
    # make a list for the groceries
    groceries = [
        ("milk", "2023-10-01"),
        ("bread", "2023-09-15"),
        ("eggs", "2023-10-10"),
        ("cheese", "2023-09-20"),
    ]

    today = datetime.today().date()

    for item, expiry in groceries:
        expiry_date = datetime.strptime(expiry, "%Y-%m-%d").date()
        if expiry_date < today:
            print(f"{item} is expired.")
        else:
            print(f"{item} is still good.")

    print("You filtered out the expired items and found a clue to the next area.")


def main():
    print("TASK NUMBER 7: OUTDATED")
    print("You need to validate a date and filter expired groceries to proceed.")

    # Validate the date
    valid_date = get_valid_date()
    print(f"Validated Date: {valid_date}")

    # Filter expired groceries
    filter_expired_groceries()


if __name__ == "__main__":
    main()

points += 1

print(f"Points: {points}")
print()



#
# 8TH TASK: GUESSING GAME" #
#

print("TASK NUMBER 8: GUESSING GAME")
print("Choose a positive number.")

import random

# prompt user for input level, n
level = input("Level: ")

# check if level is not a digit and reprompt
while not (level.isdigit()):
    level = input("Level: ")

# convert level input into integer after checking
level = int(level)

# check if level is negative and reprompt user
while(level < 0):
    level = int(input("Enter a level: "))


# randomly generate an integer between 1 and n (inclusive n), using the random module
# integer from 0 to level (n) inclusive
# when using functions from a module, prefix the function with the module name
random_integer = random.randrange(level+1)

# check if the random integer is between 1 and n
while(random_integer < 1 or random_integer > level):
    random_integer = random.randrange(level+1)

# prompt user to guess the random integer
guess = input("Guess: ")
# check if guess is not a digit or is less than 1, and reprompt
while not guess.isdigit() or int(guess) < 1:
    guess = input("Guess: ")
guess = int(guess)


# if the guess is not correct
while not(guess == random_integer):
    if(guess < random_integer):
        print("Too small!")
        guess = int(input("Guess: "))
    elif(guess > random_integer):
        print("Too large!")
        guess = int(input("Guess: "))


# if the guess is correct
if(guess == random_integer):
    print("Just right!")
    points += 10


print(f"Points: {points}")
print()



#
# 9TH TASK: BITCOIN INDEX #
#



import requests  # import the library to make HTTP requests to the API

print("TASK NUMBER 9: BITCOIN INDEX")
print("You find a sign that says 'Buy Bitcoin!'")

# prompt the user to input the number of Bitcoins they want to buy and convert it to a float
bitcoins = float(input("How many Bitcoins would you like to buy? "))

try:
    # send a GET request to the CoinCap API to fetch Bitcoin data
    response = requests.get("https://api.coincap.io/v2/assets/bitcoin")

    # parse the JSON response into a Python dictionary
    data = response.json()

    # extract the Bitcoin price in USD from the JSON response and convert it to a float
    price_usd = float(data["data"]["priceUsd"])

    # calculate the total cost of the Bitcoins by multiplying the number of Bitcoins by the price
    total_cost = bitcoins * price_usd

    # display the total cost in USD with proper formatting (2 decimal places and commas)
    print(f"The cost of {bitcoins} Bitcoins is ${total_cost:,.2f}.")

    # ask the user if they want to proceed with the purchase and convert their input to lowercase
    decision = input("Would you like to proceed with the purchase? (yes/no): ").lower()

    # check the user's decision
    if decision == "yes":
        # if the user says "yes", confirm the purchase and allow them to proceed
        print("You bought Bitcoin and gained access to the next area.")
        points += 1
    else:
        # if the user says "no", inform them that the door remains locked
        print("You decided not to buy Bitcoin.")
except:
    # handle any errors that occur during the API request or data processing
    print("Failed to retrieve Bitcoin price.")



print(f"Points: {points}")
# print an empty row
print()



#
# 10TH TASK: EMOJIZE #
#

print("TASK NUMBER 10: EMOJIZE")

# List of emoji clues and their decoded meanings
clues = {
    "🍪": "cookies",  # Find fruit and cookies
    "🔑🚪": "find the key to the door",  # Find the key to the door
    "💡🔍": "see the light",  # Look for a light and search
}

print("You will find a series of emojis now. Decode the message to proceed and exit the supermarket.")

# loop through each emoji clue
for emoji_clue, decoded_meaning in clues.items():
    print(f"\nClue: {emoji_clue}")

    # prompt the user to guess the meaning of the emoji clue
    user_guess = input("What do you think this clue means? ").strip().lower()

    # check if the user's guess matches the correct meaning
    if user_guess == decoded_meaning:
        print("You decoded the clue.")
        points += 10
    else:
        print(f"The correct answer was: {decoded_meaning}")

print(f"Points: {points}")

#
# ENDING #
#
print("Congratulations! You managed to become a supermarket survivor.")
str = input("Generate a funny farewell speech: ")






