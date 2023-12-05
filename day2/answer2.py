import pandas as pd

df = pd.read_csv("day2\day2_data.csv")

def check_colour(colour, n):
    n = int(n)
    if n > 14:
        return False
    elif colour == "r" and n > 12:
        return False
    elif colour == "g" and n > 13:
        return False
    elif colour == "b" and n > 14:
        return False
    else:
        return True
    
iteration = 0
tot = 0

for sentence in df["Picks"]: 
    # dummy numbers starts as a blank string
    dum_num = ""
    current_game = df["Game"][iteration]
    iteration = iteration + 1
    #iterate over each letter
    for index, char in enumerate(sentence):
        if char in [",",";"]:
            dum_num = ""
        elif char.isdigit():
            # Storing number
            dum_num = dum_num + char
        elif char in ["r","g","b"] and check_colour(char, dum_num):
            current_game = current_game
        else:
            current_game = 0
    tot = tot + current_game
print(tot)
#2317
            
