def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # getting rid of the dollar sign
    d  = d.replace("$", "")
    # returning a float value
    return float(d)

def percent_to_float(p):
    #getting rid of the percentage sign
    p = p.replace("%", "")
    # returning a float value without the last two 
    p = float(p) / 100
    return float(p)

main()
