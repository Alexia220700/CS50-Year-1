def main():
    fraction = input("Enter a fraction (X/Y format): ")

    try:
        # Pass the user's input (fraction) to the convert function
        percentage = convert(fraction)

        # If no errors occurred, call the gauge function and print the result
        print(gauge(percentage))
    except (ValueError, ZeroDivisionError) as e:
        # Handle errors and print the error message
        print(e)
        fraction = input("Enter a fraction (X/Y format): ")


def convert(fraction):
    # Split the input string
    try:
        X, Y = fraction.split('/')
    except ValueError:
        raise ValueError("Input must be in X/Y format.")

    # Check if X and Y are integers
    try:
        X = int(X)
        Y = int(Y)
    except ValueError:
        raise ValueError("X and Y must be integers.")


    # Check if X is greater than Y
    if X > Y:
        raise ValueError("X cannot be greater than Y.")
        return False

    # Check if Y is zero
    if Y == 0:
        raise ZeroDivisionError("Y cannot be zero.")
        return False

    # Calculate the percentage
    percentage = round((X / Y) * 100)

    # Ensure the percentage is between 0 and 100
    if percentage < 0:
        percentage = 0
    elif percentage > 100:
        percentage = 100

    return percentage


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
