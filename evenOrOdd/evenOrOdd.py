number = input("Input: ")

if (number.isnumeric()):
    number = int(number)
else:
    while not number.isnumeric():
        number = input("Input: ")

number = int(number)
if not(number % 2 == 0):
    print("Odd number")
    exit()
else:
    print("Even number")
