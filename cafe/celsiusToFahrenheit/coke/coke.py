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
    else:
        # if the coin is invalid, ignore it and inform the user
        print("Invalid coin. Please insert a valid coin (25, 10, or 5 cents).")

# if the total paid is 50 cents or more, calculate change owed
if total_paid >= 50:
    change_owed = total_paid - 50
    print(f"Change Owed: {change_owed}")
