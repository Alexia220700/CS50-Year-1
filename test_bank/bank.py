def main():
    # prompt the user for a greeting
    greeting = input("Greeting: ").strip().lower()
    # call the value function and print the result
    print(f"${value(greeting)}")


def value(greeting):
    # strip leading/trailing whitespace and convert to lowercase
    greeting = greeting.strip().lower()
    # check the conditions and return the appropriate amount
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()


