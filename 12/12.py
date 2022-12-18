import os
import sys

def partOne(x, y, g):

    visited = {}
    queue = [[x, y, 0]]

    while True:
        coords = queue.pop(0)
        try :
            _ = visited[coords[0]+coords[1]*len(g[0])]
            continue
        except :
            visited[coords[0]+coords[1]*len(g[0])] = True
        
        counter = coords[2]
        x = coords[0]
        y = coords[1]

        if (x+1 < len(g[y])):
            close = ord(g[y][x+1])-ord(g[y][x]) <= 1
            finish = ord(g[y][x+1]) == 69 and g[y][x] == "z"
            if finish:
                counter += 1
                break
            if close:
                queue.append([x+1, y, counter+1])

        if (x-1 >= 0):
            close = ord(g[y][x-1])-ord(g[y][x]) <= 1
            finish = ord(g[y][x-1]) == 69 and g[y][x] == "z"
            if finish:
                counter += 1
                break
            if close:
                queue.append([x-1, y, counter+1])

        if (y+1 < len(g)):
            close = ord(g[y+1][x])-ord(g[y][x]) <= 1
            finish = ord(g[y+1][x]) == 69 and g[y][x] == "z"
            if finish:
                counter += 1
                break
            if close:
                queue.append([x, y+1, counter+1])

        if (y-1 >= 0):
            close = ord(g[y-1][x])-ord(g[y][x]) <= 1
            finish = ord(g[y-1][x]) == 69 and g[y][x] == "z"
            if finish:
                counter += 1
                break
            if close:
                queue.append([x, y-1, counter+1])

    return counter

def main():
    file = open(os.path.join(sys.path[0], "input.txt"), "r")
    data = file.read().split("\n")
    file.close()

    x, y = 0, 0
    points = []
    g = data[:]
    for line in range(len(g)):
        g[line] = list(g[line])
        for h in range(len(g[line])):
            if (g[line][h] == "a"):
                points.append([h, line])
        try:
            x = g[line].index("S")
            y = line
            g[line][g[line].index("S")] = "a"
        except:
            pass
        
    print("Partn one:")
    print(partOne(x, y, g))

    best = 100000000000000
    length = best
    for coords in points:
        try:
            length = partOne(coords[0], coords[1], g)
        except :
            pass
        if (best > length):
            best = length

    print("Part two:")
    print(best)

if __name__ == "__main__":
    main()