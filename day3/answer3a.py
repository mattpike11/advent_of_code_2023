import pandas as pd

raw_data = pd.read_csv("day3\day3_data.csv")

# Split the characters into a list of single characters
df = pd.DataFrame(raw_data["engine"].apply(list).tolist())
df.columns = [f"c{i}" for i in range(1, 141)]

#print(df[["c138","c139","c140"]].head())

for y in range(0,140):
    dum_num = ""
    for x in range(1,141):
        char = df[f"c{x}"].iloc[y]
        if char.isdigit():
            # Storing number
            dum_num = str(dum_num) + char
        elif char in ["@","*","&","%","$","+","=","-","#","."]:    
            try:
                dum_num = int(dum_num)
            except ValueError:
                dum_num = ""
            if isinstance(dum_num, int):
                print(dum_num)
            dum_num = ""