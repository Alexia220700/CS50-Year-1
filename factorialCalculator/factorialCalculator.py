def main():
    factorial_number = input("Enter a number: ")

    factorial_number = int(factorial_number)

    if(factorial_number < 0):
        factorial_number = input("Enter a positive number: ")
        factorial_number = int(factorial_number)

    result = factorial_calculation(factorial_number)

    print(result)

def factorial_calculation(factorial_number):
    if(factorial_number == 0 or factorial_number == 1):
        return 1

    # initialize result integer with 1, because it s a multiplication
    result = 1
    for i in range(1, factorial_number + 1):
        # multiply result with each number that s less or equal to factorial_number input
        result = result * i

    return result

main()


