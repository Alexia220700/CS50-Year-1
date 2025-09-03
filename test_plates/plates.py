def main():
    # prompt user for input car plate
    plate = input("Plate: ")
    # check if the car plate is valid or not and return the correct output
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    # check if the car plate has the correct number of characters
    if len(s) < 2 or len(s) > 6:
        return False

    # check if the first two characters are letters
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    # check if all characters are letters or numbers
    for char in s:
        if not (char.isalpha() or char.isnumeric()):
            return False

    # check if numbers come at the end of the license plate
    # and the first number is not '0'
    number = False
    for i, char in enumerate(s):
        if char.isnumeric():
            if not number and char == '0':
                return False
            number = True
        elif number:  # if a letter appears after a number, it's invalid
            return False

    # if all checks are passed
    return True

if __name__ == "__main__":
    main()


