def main():
    # ask user for input string
    string = input("Input: ")

    # call the shorten function to remove vowels
    # iterates through each character in the string
    # joins the characters back into a single string and returns it
    shortened_string = shorten(string)

    # output the result
    print("Output:", shortened_string)

def shorten(word):
    # define the vowels to be removed
    vowels = "AEIOUaeiou"

    # construct a new string without vowels
    # [char for char in word if char not in vowels] is a list comprehension in Python
    result = ''.join([char for char in word if char not in vowels])

    return result

# ensures that the main function is called only when the script is run directly, not when imported as a module
# needed for unittest
if __name__ == "__main__":
    main()
