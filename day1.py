test = open("input1.txt")
sum = 0
for line in test.readlines():
    mass = int(line)
    while mass//3-2 > 0:
        sum += mass//3-2
        mass = mass//3-2
print(f"result: {sum}")
