import os
import sys
import string

def main():
    file = open(os.path.join(sys.path[0], "input"), "r")
    data = file.read().split("\n")
    file.close()

    prior = string.ascii_letters
    total = 0

    for backpack in data:
        backpack = list(backpack)
        compartmentA = backpack[0: int(len(backpack)/2)]
        compartmentB = backpack[int(len(backpack)/2): len(backpack)]
        found = []
        for itemA in compartmentA:
            if ((itemA in compartmentB) and (itemA not in found)):
                total += (prior.index(itemA)+1)#*min(compartmentA.count(itemA),compartmentB.count(itemA))
                found.append(itemA)

    print("Part one:")
    print(total)

    total = 0
    
    for group in range(0, len(data), 3):
        found = False
        mem1 = data[group]
        mem2 = data[group+1]
        mem3 = data[group+2]
        for badge in mem1:
            if (badge in mem2 and badge in mem3):
                total += prior.index(badge)+1
                found = True
            if found:
                break

    print("Part one:")
    print(total)

if __name__ == "__main__":
    main()