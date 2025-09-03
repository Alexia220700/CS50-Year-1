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
    exit()

