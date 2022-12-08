import os
import sys

def main():
    file = open(os.path.join(sys.path[0], "input.txt"), "r")
    data = file.read().split("\n")
    file.close()

    result = 2*len(data) + 2*len(list(data[0])) - 4

    for y in range(1, len(data)-1):
        row = list(data[y])
        for x in range(1, len(row)-1):
            t = row[x]
            up = [ l[x] for l in data[0 : y] ]
            down = [ l[x] for l in data[y+1 : len(data)] ]
            left = row[0 : x]
            right = row[x+1 : len(row)]

            for direction in [up, down, left, right]:
                v = True
                for tree in direction:
                    if (tree >= t):
                        v = False
                        break
                if v:
                    result += 1
                    break

    print(result)

    highest = 0
    for y in range(1, len(data)-1):
        row = list(data[y])
        for x in range(1, len(row)-1):
            t = row[x]
            up = [ l[x] for l in data[0 : y] ]
            down = [ l[x] for l in data[y+1 : len(data)] ]
            left = row[0 : x]
            right = row[x+1 : len(row)]

            up.reverse()
            left.reverse()

            localFull = 1
            for direction in [up, down, left, right]:
                local = 0
                for tree in direction:
                    if (tree >= t):
                        local += 1
                        break
                    else:
                        local += 1
                localFull *= local

            if (localFull > highest):
                highest = localFull

    print(highest)

if __name__ == "__main__":
    main()