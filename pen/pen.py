def print_pen(colour, shape, brand):
    result = " ====  PEN ==== \n"
    result += f"colour: {colour}\n"
    result += f"shape: {shape}\n"
    result += f"brand: {brand}\n"
    return result

    colour1 = "yellow"
    shape1 = "cylinder"
    brand1 = "123ink.nl"

    colour2 = "blue"
    shape2 = "cylinder"
    brand2 = "manter"

    colour3 = "white"
    shape3 = "cylinder"
    brand3 = "stabilo"

    pen1 = (colour1, shape1, brand1)
    pen2 = (colour2, shape2, brand2)
    pen3 = (colour3, shape3, brand3)

    pens = [pen1, pen2, pen3]

    print("the Procedural pen factory")
    print("Printing one by one")
    print(print_pen(*pen1))
    print(print_pen(*pen2))
    print(print_pen(*pen3))

# OR
# class Pen:

