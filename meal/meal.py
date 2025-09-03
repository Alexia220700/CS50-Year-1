# implement a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time

def main():
    # ask for input hour
    time = input("What time is it? (HH:MM) ")

    # convert the input time to a float representing hours
    final_time = convert(time)

    # check for the correct hours
    if(final_time >= 7.0 and final_time <= 8.0):
        print("breakfast time")
    elif(final_time >= 12.0 and final_time <= 13.0):
        print("lunch time")
    elif(final_time >= 18.0 and final_time <= 19.0):
        print("dinner time")


def convert(time):
    # split the time into hours and minutes
    hours, minutes = time.split(":")

    # convert hours and minutes to integers
    hours = int(hours)
    minutes = int(minutes)

    # used to convert the time into a single float value
    # dividing the minutes by 60 converts them into a fractional part of an hour
    # 2 hours and 30 minutes becomes 2 + (30 / 60) = 2 + 0.5 = 2.5 hours
    final_time = hours + (minutes / 60)

    # returning the float number so I can use it in def main()
    return final_time


if __name__ == "__main__":
    main()
