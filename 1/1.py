import sys
import os

def main():
    file = open(os.path.join(sys.path[0], "input"), "r")
    data = file.readlines()
    file.close()

    maxN = 0
    maxE = 0
    e = 0
    tmp = 0
    for c in range(0, len(data)):
        if (data[c] == "\n" or c == len(data)-1):
            if (maxN <= tmp):
                maxN = tmp
                maxE = e
            tmp = 0
            e += 1
            continue
        tmp += int(data[c])

    print("Part one")
    print("Maximum calories :",maxN)
    print("Elf carrying the largest amount :",maxE)

    maxN = {"1": (0, 0), "2": (0, 0), "3": (0, 0)}
    e = 0
    tmp = 0

    newData = []
    for c in range(0, len(data)):
        if (data[c] == "\n" or c == len(data)-1):
            newData.append(tmp)
            tmp = 0
            continue
        tmp += int(data[c])
    newData.sort(reverse=True)
    
    print("Part two")
    print("Sum of top 3 elfs is ", sum(newData[0:3]))

if __name__ == "__main__":
    main()