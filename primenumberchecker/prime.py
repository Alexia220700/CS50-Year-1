def main():
    while True:
        prime_number = input("Enter a prime number: ")

        # check if the input is a valid integer greater than 1
        if (prime_number.isnumeric()):
            prime_number = int(prime_number)
            if (prime_number > 1):
                break
            else:
                print("Enter a number greater than 1: ")
        else:
            print("Enter a prime number: ")

    # check if the number is prime
    if check_prime(prime_number):
        print(f"{prime_number} is a prime number.")
    else:
        print(f"{prime_number} is not a prime number.")

def check_prime(prime_number):
    nr_dividing_prime = 0

    # loop from 1 to n (inclusive)
    for i in range(1, prime_number + 1):
        if prime_number % i == 0:
            nr_dividing_prime += 1

    # a prime number has exactly 2 divisors: 1 and itself
    if nr_dividing_prime == 2:
        return True
    else:
        return False

# run the program
main()

