def main():
    # Prompt the user for a greeting
    greeting = input("Greeting: ").strip().lower()
    # Call the value function and print the result
    print(f"${value(greeting)}")


def value(greeting):
    # Check the conditions and return the appropriate amount
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()


