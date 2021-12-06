with open("data/dataday2.txt") as f: lst=[line.strip() for line in f]

#Part 1
horizontalPos = int()
depth = int()
aim = int()
commands = [{key:int(value)} for key,value in [a.split(" ") for a in lst]]
for command in commands:
    if command.get('forward'):
        horizontalPos += command.get('forward')
    elif command.get('up'):
        depth -= command.get('up')
    else:
        depth += command.get('down')

print(f"the Horizontal Position is: {horizontalPos} \n the depth is: {depth} .\n")
print(f"Multiplying them return the value {horizontalPos*depth}. \n")

#part 2

horizontalPos = int()
depth = int()
aim = int()
commands = [{key:int(value)} for key,value in [a.split(" ") for a in lst]]
for command in commands:
    if command.get('forward'):
        horizontalPos += command.get('forward')
        depth += command.get('forward') * aim
    elif command.get('up'):
        aim -= command.get('up')
    else:
        aim += command.get('down')

print(f"the Horizontal Position is: {horizontalPos} \n the depth is: {depth} .\n")
print(f"Multiplying them return the value {horizontalPos*depth}. \n")
