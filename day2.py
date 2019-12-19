numbers = open("input2.txt").read().strip().split(",")
numbers = [int(n) for n in numbers]
#restore 
numbers[1] = 12
numbers[2] = 2
#initiate 
def compute(x):
    result = [i for i in x] 
    for i in range(0,len(result),4): 
            opcode = int(result[i])
            n1_pos = result[i+1]
            n2_pos = result[i+2]
            n3_pos = result[i+3]
            if opcode == 1: 
                result[n3_pos] = result[n1_pos]+result[n2_pos]
            elif opcode == 2:
                result[n3_pos] = result[n1_pos]*result[n2_pos]
            elif opcode == 99:
                break
            else:
                print("Something went wrong!")
                break
    return result        

res, noun, verb = 0, 0, 0
for i in range(100):
    print(i)
    if res == 19690720: 
        break
    for j in range(100):
        noun = i
        verb = j
        numbers[1] = noun
        numbers[2] = verb
        res = compute(numbers)[0]
        print(f"res: {res}")
        if res == 19690720:
            break
print(f"noun: {noun}, verb: {verb}, [0]: {res}, result: {100*noun + verb}")
