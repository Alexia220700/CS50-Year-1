from cs50 import get_int

card_number = get_int("Enter a card number: ")
aux = card_number
first2_nr = card_number

# counting the length of card number
length = 0
while (card_number != 0):
    card_number = card_number // 10
    length += 1

# sum of digits
sum = 0

# counts position of number
alternate = 1

while aux > 0:
    digit = aux % 10
    aux = aux // 10

    if alternate % 2 == 0:
        # multiplies every other digit by 2, starting with the number's
        # second-to-last digit
        digit = digit * 2

        if digit > 9:
            digit = digit - 9

    sum = sum + digit
    alternate += 1

# check if the length and first two digits are correct
# or only the first digit for VISA
if length == 15 and (first2_nr // 10000000000000 == 34 or first2_nr // 10000000000000 == 37) and sum % 10 == 0:
    print("AMEX")
elif length == 16 and (first2_nr // 100000000000000 >= 51 and first2_nr // 100000000000000 <= 55) and sum % 10 == 0:
    print("MASTERCARD")
elif (length == 13 or length == 16) and (first2_nr // 1000000000000 == 4 or first2_nr // 1000000000000000 == 4) and sum % 10 == 0:
    print("VISA")
else:
    print("INVALID")
