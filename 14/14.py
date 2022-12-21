import os
import sys

def main():
    file = open(os.path.join(sys.path[0], "input.txt"), "r")
    data = file.read().split("\n")
    file.close()

    # if not in area -> air
    area = {}
    maxX = 0
    maxY = 0
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
                area[str(a[0]+dx*i)+":"+str(a[1]+dy*i)] = True

    x, y = 500, 0
    s = 0
    while (y <= maxY+10):
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

if __name__ == "__main__":
    main()