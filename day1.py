#first half

increase = lambda x,y: 1 if x > y else 0
total = int()
previous = int()
with open("data/dataday1.txt") as f: 
    for line in f:
        total += increase(int(line), previous)
        previous = int(line)

## minus 1, cause in the first step dont exist a previous measurement.
print(total-1)

#second half

with open("data/dataday1.txt") as f: lst=[int(line.strip()) for line in f]

delta = int()
total = int()
previous = sum(lst[delta:delta+3])

for delta in range(1, len(lst)-2, 1):
    target = sum(lst[delta:delta+3])
    total += increase(target, previous)
    previous = target

print(total)




