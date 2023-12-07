import pandas as pd

df = pd.read_csv("day4/day4_data.csv")

total_cards = {0: 0}

for index, row in df[["Card", "Winners"]].iterrows():
    original = row["Card"]
    winners = row["Winners"]

    if winners > 0:
        total_cards.update({original: list(range(original + 1, original + 1 + winners))})
    elif winners == 0:
        total_cards.update({original: winners})
