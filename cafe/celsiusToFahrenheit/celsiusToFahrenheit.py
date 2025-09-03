def main():
    celsius = input("Input temperature (Celsius): ")

    # convert Celsius to Fahrenheit
    fahrenheit = celsius_to_fahrenheit(celsius)

    print(f"{fahrenheit}°F")

def celsius_to_fahrenheit(celsius):
    # replace comma with period for decimal separator
    celsius = celsius.replace(",", ".")

    # check if the input is a valid number (integer or float)
    try:
        celsius = float(celsius)  # convert input to float
    except ValueError:
        celsius = input("Input temperature (Celsius): ")

    celsius = float(celsius)

    # calculate celsius in fahrenheit
    fahrenheit = (9/5) * celsius + 32
    return fahrenheit

main()
