import sys # to handle command-line arguments
import requests # to make requests

# check if the user provided the correct number of arguments
# the program expects exactly one argument
if len(sys.argv) != 2:
    print("Usage: python bitcoin.py <amount_of_bitcoins>")
    # exit the program if the argument is missing
    sys.exit(1)

# try to convert the argument to a float
try:
    # get the 2nd argument from the command line and check it
    bitcoins = float(sys.argv[1])
except ValueError:
    # if the argument cannot be converted to a float/it's not a number
    print("Command-line argument is not a number")
    # exit the program
    sys.exit(1)

# query the CoinCap API to get the current Bitcoin price
try:
    # send a GET request to CoinCap API to fetch Bitcoin data
    response = requests.get("https://api.coincap.io/v2/assets/bitcoin")
    # check if the request was successful
    response.raise_for_status()

    # parse the JSON response into a Python dictionary
    data = response.json()

    # extract the Bitcoin price in USD from the JSON response
    price_usd = float(data["data"]["priceUsd"])
except requests.RequestException as e:
    # handle any errors that occur during the API request
    print(f"Error: Failed to retrieve Bitcoin price. {e}")
    # exit the program
    sys.exit(1)
except (KeyError, ValueError) as e:
    # handle errors if the JSON structure is invalid or the price cannot be converted to a float
    print(f"Error: Invalid data received from the API. {e}")
    # exit the program w code 1, not 0 as the code asks
    sys.exit(1)

# calculate the total cost of the Bitcoins
total_cost = bitcoins * price_usd

# display the total cost in USD with proper formatting
print(f"The cost of {bitcoins} Bitcoins is ${total_cost:,.4f}")
