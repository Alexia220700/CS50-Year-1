import math
import random
from datetime import datetime
import panda as pd

def circle_area(radius):
    return math.pi  * radius ** 2
#print(circle_area(float(input("enter radius "))))

def pick_random_name(names):
    return random.choice(names)

names_list = ["Adriana", "Mark", "Nicolo", "Jan", "Kamyab", "Stefan", "Oleksander"]
print(pick_random_name(names_list))

# Calculate the difference between two dates
def date_diff(date1, date2):
    format_str = "%Y-%m-%d"
    d1 = datetime.strptime(date1, format_str)
    d2 = datetime.strptime(date2, format_str)

    return abs(d1-d2)

#print(date_diff("2025-02-24", "1975-12-08"))

df = pd.read_csv("vgsales.csv")
#print(df.head())
#print(df.info())


