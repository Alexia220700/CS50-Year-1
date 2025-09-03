def get_valid_date():
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]


    while True:
        # prompt the user until a valid date is entered
        # remove leading/trailing spaces by using .strip()
        date = input("Date (month-day-year order): ").strip()

        # check if the input contains slashes (MM/DD/YYYY format)
        if "/" in date:
            # split the input into month, day, and year using "/"
            parts = date.split("/")
            # check if month, day, and year are all digits
            if len(parts) == 3:
                month, day, year = parts
                if month.isdigit() and day.isdigit() and year.isdigit():
                    # if yes, turn them into integers
                    month = int(month)
                    day = int(day)
                    year = int(year)
                    # validate the month, day, and year ranges
                    if (1 <= month <= 12 and 1 <= day <= 31 and 1 <= year <= 9999):
                        # return the date in YYYY-MM-DD format
                        return f"{year:04}-{month:02}-{day:02}"

        # check if the input contains a space and a comma (Month Day, Year format)
        elif " " in date and "," in date:
            # split the input into month_day and year using the comma
            month_day, year = date.split(",")
            # remove any leading/trailing spaces from month_day and year
            month_day = month_day.strip()
            year = year.strip()
            # check if the first part of month_day is a valid month name
            if month_day.split()[0] in months:
                # split month_day into month and day using the space
                month, day = month_day.split()
                # check if day and year are digits
                if day.isdigit() and year.isdigit():
                    day = int(day)
                    year = int(year)
                    # get the index of the month in the months list and add 1 (since list indices start at 0)
                    month_index = months.index(month) + 1
                    if (1 <= day <= 31 and 1 <= year <= 9999):
                        # return the date in YYYY-MM-DD format
                        return f"{year:04}-{month_index:02}-{day:02}"

        # if the input doesn't match any valid format
        print("Invalid date format. Please use month-day-year or month/day/year.")

# get and print the valid date
print(get_valid_date())


