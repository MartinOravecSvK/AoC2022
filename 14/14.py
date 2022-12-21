import os
import sys

def main():
    file = open(os.path.join(sys.path[0], "input.txt"), "r")
    data = file.read().split("\n")
    file.close()

    # if not in area -> air
    area = {}
    maxX = 0
    minX = 1000000
    maxY = 0
    minY = 0
    points = []
    c = 0
    for lines in data:
        points.append([])
        lines = lines.split(" -> ")
        for line in lines:
            line = line.split(",")
            points[c].append([int(line[0]), int(line[1])])
            # might be useful
            maxX = max(maxX, int(line[0]))
            maxY = max(maxY, int(line[1]))
            minX = min(minX, int(line[0]))
        c += 1

    for line in range(len(points)):
        for point in range(len(points[line])-1):
            a, b = points[line][point], points[line][point+1]
            dx, dy = 0, 0
            if (a[0]-b[0] > 0):
                dx = -1
            elif (a[0]-b[0] < 0):
                dx = 1

            if (a[1]-b[1] > 0):
                dy = -1
            elif (a[1]-b[1] < 0):
                dy = 1

            for i in range(0, max(abs(a[0]-b[0]), abs(a[1]-b[1]))+1):
                area[str(a[0]+dx*i)+":"+str(a[1]+dy*i)] = "#"

    originalArea = area.copy()
    x, y = 500, 0
    s = 0
    while (y <= maxY):
        if not area.get(str(x)+":"+str(y+1), False):
            y += 1
        elif not area.get(str(x-1)+":"+str(y+1), False):
            x -= 1
            y += 1
        elif not area.get(str(x+1)+":"+str(y+1), False):
            x += 1
            y += 1
        else :
            area[str(x)+":"+str(y)] = True
            s += 1
            x, y = 500, 0

    print("Part one:")
    print(s)

    floor = maxY + 2
    area = originalArea

    for i in range(0, 2*maxX):
        area[str(1*i)+":"+str(floor)] = "#"

    x, y = 500, 0
    s = 0
    while True:
        if not area.get(str(x)+":"+str(y+1), False) and y != floor:
            y += 1
        elif not area.get(str(x-1)+":"+str(y+1), False) and y != floor:
            x -= 1
            y += 1
        elif not area.get(str(x+1)+":"+str(y+1), False) and y != floor:
            x += 1
            y += 1
        elif (x == 500 and y == 0):
            area[str(x)+":"+str(y)] = "O"
            s += 1
            break
        else :
            maxX = max(maxX, x)
            minX = min(minX, x)
            area[str(x)+":"+str(y)] = "O"
            s += 1
            x, y = 500, 0

    # Visualizer :D (for part two, you can change it a bit to make it work for the first part)

    # for line in range(floor+1):
    #     print()
    #     for point in range(minX-1, maxX+2):
    #         if (area.get(str(point)+":"+str(line), False)):
    #             print(area.get(str(point)+":"+str(line)), end="")
    #         else :
    #             print(".", end="")
    # print()

    print("Part two:")
    print(s)

if __name__ == "__main__":
    main()