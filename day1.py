test = open("input1.txt")
sum = 0
for line in test.readlines():
    mass = int(line)
    while mass//3-2 > 0:
        print(f"mass: {mass}")
        sum += mass//3-2
        print(f"sum in loop: {sum}")
        mass = mass//3-2
print(f"sum: {sum}")
