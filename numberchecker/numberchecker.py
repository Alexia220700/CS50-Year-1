def main():
    while True:
        try:
            num = float(input("Enter a number: "))
            break  # Exit the loop if the input is a valid number
        except ValueError:
            print("Invalid input. Please enter an number.")

    print("The number is", check(num), sep=" ")

def check(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

if __name__ == "__main__":
    main()
