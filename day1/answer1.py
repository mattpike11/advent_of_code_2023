import pandas as pd

df = pd.read_csv("day1\day1_data.csv")

tot = 0

for cal_val in df["calibration_value"]:
    # Iterating over each character in the string
    for index, char in enumerate(cal_val):
    # Checking if char is numeric
        if char.isdigit():
            # Storing number
            first_digit = char
            break
    # same as above, but reversing the string
    for index, char in reversed(list(enumerate(cal_val))):
        if char.isdigit():
            second_digit = char
            break
    n = int(first_digit + second_digit)
    tot = tot + n

# print answer
print(tot)
# 55607
