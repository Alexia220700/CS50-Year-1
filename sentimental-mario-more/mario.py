from cs50 import get_int

# ask for correct input height
height = get_int("Choose a height between 1-8")

while (height < 1 or height > 8):
    height = get_int("Choose a height between 1-8")

i = 0
j = 0

# i goes through rows
for i in range(height):
    # j goes through collumns
    for j in range(height - i - 1):
        # prevents the newline and instead specify a different string to be appended at the end of the output
        # used to print multiple items on the same line
        print(" ", end="")

# print hashes for the pyramid
    for j in range(i + 1):
        print("#", end="")

# print the gap between the two parts of the pyramid
    print("  ", end="")

# print the right side hashes
    for j in range(i + 1):
        print("#", end="")

    # move to a new line after every row
    print()
