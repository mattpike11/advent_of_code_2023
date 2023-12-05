import pandas as pd

df = pd.read_csv("day2\day2_data.csv")
tot = 0

for sentence in df["Picks"]: 
    # dummy numbers starts as a blank string
    dum_num = ""
    
    r_num = 0
    g_num = 0
    b_num = 0

    for index, char in enumerate(sentence):
        # reset dummy if comma/semi colon  
        if char in [",",";"]:
            dum_num = ""
            
        # read the number
        if char.isdigit():
            # Storing number
            dum_num = dum_num + char
        
        if char in ["r","g","b"]:
            dum_num = int(dum_num)
            # judge number for its corresponding colour
            if char == "r":
                r_num = max(r_num,dum_num)
            elif char == "g":
                g_num = max(g_num, dum_num)
            else:
                b_num = max(b_num, dum_num)
        
        if index == len(sentence) - 1:
            power = r_num * g_num * b_num
            tot = tot + power
print(tot)
#74804
