import os
import sys

def main():
    file = open(os.path.join(sys.path[0], "input.txt"), "r")
    data = file.read().split("\n")
    file.close()

    stacks = [[], [], [], [], [], [], [], [], []]
    iI = data.index("")

    for line in data[:iI-1]:
        line = line.replace("[", "").replace("]", "").replace("    " , "%").replace("   " , "%").replace(" ", "")
        counter = 0
        for crate in line:
            if (crate == "%"):
                counter += 1
                continue
            stacks[counter].append(crate)
            counter += 1

    for stack in stacks:
        stack.reverse()

    for instruction in data[iI+1:]:
        instruction = instruction.split(" ")
        q = int(instruction[1])
        f = int(instruction[3])
        t = int(instruction[5])
        for i in range(q):
            stacks[t-1].append(stacks[f-1].pop())

    print("Part One:")
    for stack in stacks:
        print(stack.pop(), end="")
    print()

    stacks = [[], [], [], [], [], [], [], [], []]
    iI = data.index("")

    for line in data[:iI-1]:
        line = line.replace("[", "").replace("]", "").replace("    " , "%").replace("   " , "%").replace(" ", "")
        counter = 0
        for crate in line:
            if (crate == "%"):
                counter += 1
                continue
            stacks[counter].append(crate)
            counter += 1

    for stack in stacks:
        stack.reverse()

    for instruction in data[iI+1:]:
        instruction = instruction.split(" ")
        q = int(instruction[1])
        f = int(instruction[3])
        t = int(instruction[5])
        tmp = []
        for i in range(q):
            tmp.append(stacks[f-1].pop())
        tmp.reverse()
        for crate in tmp:
            stacks[t-1].append(crate)

    print("Part Two:")
    for stack in stacks:
        print(stack.pop(), end="")
    print()
    
if __name__ == "__main__":
    main()