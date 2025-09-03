# ask for input
arithmetic_expression = input("Expression (x, y, z): ")

# separates a string into a sequence of values,
# all of which can be assigned to variables at once
x, y, z = arithmetic_expression.split(" ")

# convert x and z to integers
# necessary for performing arithmetic operations
x = int(x)
z = int(z)

# check wht type of operator variable y is
# and make it execute the correct operation
# printing the number as a float with only one digit after the decimal point
if y == "+":
    # can be rewritten like print("{:.1f}".format(x + z))
    print(f"{(x + z):.1f}")
elif y == "-":
    print(f"{(x - z):.1f}")
elif y == "*":
    print(f"{(x * z):.1f}")
elif y == "/":
    print(f"{(x / z):.1f}")
# if the operation is invalid:
else:
    print("Invalid operator.")


