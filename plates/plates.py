def main():
    # prompt user for input car plate
    plate = input("Plate: ")
    # check if the car plate is valid or not and return the correct output
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
# easier: pattern = r"^[A-Z]{2,6}\d*$"

    # check if the car plate has the correct number of characters
    if len(s) < 2 or len(s) > 6:
        return False

    # use a for loop to check the first 2 characters
    for char in s:
        # check if the first character is a letter and uppercase
        # s is str in Python
        if not(s[0].isalpha() and s[0].isupper()):
            return False
        # check if the second character is a letter and uppercase
        if not(s[1].isalpha() and s[1].isupper()):
            return False


    # check if all characters are letters
    nrLetters = 0
    nrCharacters = 0

    for i, char in enumerate(s):
        nrCharacters += 1
        if (char.isalpha()):
            nrLetters += 1
        # if there is stg different than letters, stop the program
        else:
            break
    # if the letters are equal to characters, valid license plate
    if(nrCharacters == nrLetters):
        return True

    # check if the numbers come at the end of the license plate
    # enumerate() function used for looping over a sequence
    for i, char in enumerate(s):
        # check if character is a number
        if(s[i].isnumeric()):
            # aux will remember the index of the first number in the license plate
            aux = i
            # check if the first number is 0
            if (s[aux] == '0'):
                return False

            # break so it doesn't continue to check the characters
            break


    # enumerate() function used for looping over a sequence
    # enumerate(s[aux + 1:]) used to start loop from aux + 1
    # can be written also like for i in range(aux + 1, len(s))
    for i, char in enumerate(s[aux + 1:]):
        # if the characters after the first number are letters, return false
        if not(char.isnumeric()):
            return False

    # if all checks are passed
    return True

main()


