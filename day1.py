increase = lambda x,y: 1 if x > y else 0
total = int()
previous = int()
with open("data/datatest.txt") as f: 
    for line in f:
        total += increase(int(line), previous)
        previous = int(line)

## minus 1, cause the first step where dont exist a previous measurement count as increased.
print(total-1)





