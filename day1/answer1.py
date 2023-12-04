import pandas as pd

df = pd.read_csv("day1\day1_data.csv")

# initialise running total
tot = 0

# dictionary of lookup values to replace
lookup_dict = {"sixteen":16,
               "seventeen":17,
               "eighteen":18,
               "nineteen":19,
               "zero":0,
               "one":1,
               "two": 2,
               "three":3,
               "four":4,
               "five":5,
               "six":6,
               "seven":7,
               "eight":8,
               "nine":9,
               "ten":10,
               "eleven":11,
               "twelve":12,
               "thirteen":13,
               "fourteen":14,
               "fifteen":15,
               "twenty":20,
               "thirty":30,
               "forty":40,
               "fifty":50,
               "sixty":60,
               "seventy":70,
               "eighty":80,
               "ninety":90,
               }


for cal_val in df["calibration_value"]:    
    # blank dummy string
    dummy = ""
    #iterate over each letter
    for index, char in enumerate(cal_val):
        if index == 0:
            dummy = ""
        # build new string one letter at a time
        dummy = dummy + char
        # check if worded number is in dummy
        for word in lookup_dict.keys():
            if word in dummy:
                # replace 1st 2 letters of subs string
                # avoids issues with combined words in cal_val e.g. eightwo
                dummy = dummy.replace(word[:2],str(lookup_dict[word]))
    
    for index, char in enumerate(dummy):   
    # Checking if char is numeric
        if char.isdigit():
            # Storing number
            first_digit = char
            break
    # same as above, but reversing the string
    for index, char in reversed(list(enumerate(dummy))):
        if char.isdigit():
            second_digit = char
            break
    n = int(first_digit + second_digit)
    tot = tot + n

# print answer
print(tot)
# 55291
