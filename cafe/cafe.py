# define the main function of the code
def main():
    # first part
    # welcoming the customer and asking if they want to customize the text
    # or not
    print("Welcome to our Cafe!")
    string = ("Welcome to our Cafe!")
    answer1 = input("Would you like to customize this message? Answer with yes or no. ")

    # customizing the string if customer asks to do it
    if(answer1.lower() == "yes"):
        # checking if it's a character, not space etc
        for char in string:
            if char.isalpha():
                # end used to remove the newline at the end of each ...
                print(char, "...", end="");
            else:
                print(char, end="");


    # second part
    # asking customer for order
    order1 = input(" What would you like to order? ")

    # call writeOrder and get the price
    totalAmount = writeOrder(order1)

    # ask if the customer wants to order more items
    totalAmount += moreThanOneOrder()  # add more orders to the total

    # ask for tip percentage and calculate the total amount with tip
    totalPriceWithTip(totalAmount)

# making a function for taking the order more easily
# order1 is the argument of this function, bc it's defined in another function (the main function)
def writeOrder(order1):
    # make the letters lowercase to check the order
    # assigned the input string to a new variable, because I made it lowercase
    order = order1.lower();

    # matching the order to the appropriate emoji
    if(order =="coffee"):
        emoji = '☕';
    elif(order == "tea"):
        emoji ='🫖';
    elif(order == "cake"):
        emoji ='🍰';
    elif(order == "croissant"):
         emoji ='🥐';
    elif(order == "orange juice"):
         emoji ='🍊';
    else:
        print("Sorry, we don't have that item.");
        # exit the function with 0 if the item isn't recognized
        return 0

    # showing the order the customer made
    print("Okay, I will make " +order +emoji+ " for you. ")
    # I can rewrite it using (f"Okay, I will make {order} {emoji} for you.")

    # third part
    # calculating the energy level
    answer2 = input("Would you like to know the energy level of your order? ")

    if(answer2.lower() == "yes"):
        # convert string into an integer for the calculation to work
        weight = int(input("Input the weight, in grams, of the order you made. "))

        # in Python, ** used for exponentiation, instead of ^
        # Energy = mass * speed_of_light^2
        energyLevel = weight * (3 * 10**8)**2

        # rounding the number to three digits
        print(f"The energy level of your order is {round(energyLevel, 3)} Joules.")

    # fourth part
    # order total with tip

    # setting different prices for each drink or pastry
    if(order=="coffee"):
        # no need to put $ in Python
        price = 3;
    elif(order== "tea"):
        price = 2;
    elif(order== "cake"):
        price = 5;
    elif(order== "croissant"):
         price = 6;
    elif(order== "orange juice"):
         price = 8;

    # show the price of the specified item
    print("This item costs ", end="")
    print(price, end="")
    print("$.")
    # or change it with print(f"This item costs {price}$.")

    # return the price of the current order
    return price


def moreThanOneOrder():
    # check if customer wants to order something else or not
    totalAmount = 0

    # while customer responds with yes, the loop repeats
    while True:
        order2 = input("Would you like something else? ")
        if order2.lower() == "yes":
            # ask for new input
            order1 = input("What would you like to order? ")

            # calculate total cost
            # add the price of the new order
            totalAmount += writeOrder(order1)
        else:
            # exit the loop if the customer doesn't want anything else
            break

    # return the total of all additional orders
    return totalAmount



# fifth part
# ask for tip percentage and output the total amount for the customer

def totalPriceWithTip(totalAmount):

    # tip percentage
    tipPercentage = int(input("Choose a tip percentage: 10, 15 or 20. "))

    tip = (tipPercentage / 100) * totalAmount

    # add tip to the total amount
    finalPrice = totalAmount + tip

    print("Your total is: ")
    print(finalPrice, end="")
    print("$")
    print("Thank you for visiting our Cafe!")

main()

