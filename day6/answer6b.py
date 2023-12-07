t = 51699878
d = 377117112241505

tot = 0

for i in range(1,t+1):
    if i*(t-1) > d:
        tot = tot + 1
    t = t - 1
print(tot)