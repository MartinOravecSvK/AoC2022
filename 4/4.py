import os
import sys

def main():
    file = open(os.path.join(sys.path[0], "input"), "r")
    data = file.read().split("\n")
    file.close()

    total = 0
    for pair in data:
        pair = pair.split(",")
        mem1 = pair[0].split("-")
        mem2 = pair[1].split("-")

        if (int(mem1[0]) <= int(mem2[0]) and int(mem1[1]) >= int(mem2[1])):
            total += 1
            continue
        if (int(mem1[0]) >= int(mem2[0]) and int(mem1[1]) <= int(mem2[1])):
            total += 1
            continue
                
    print("Part one")
    print(total)

    total = 0

    for pair in data:
        pair = pair.split(",")
        mem1 = pair[0].split("-")
        mem2 = pair[1].split("-")

        if (int(mem1[0]) <= int(mem2[0]) and int(mem1[1]) >= int(mem2[0])):
            total += 1
            continue
        if (int(mem1[0]) >= int(mem2[0]) and int(mem1[0]) <= int(mem2[1])):
            total += 1
            continue

    print("Part two")
    print(total)

if __name__ == "__main__":
    main()