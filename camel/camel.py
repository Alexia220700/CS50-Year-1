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









