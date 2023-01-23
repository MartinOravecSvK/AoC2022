import os
import sys

def per2(x, y, dist, plot, line):
    dy = 0
    while dist >= dy:

        if (not plot.get(y+dy, False)):
            plot[y+dy] = [[x-(dist-dy), x+(dist-dy)+1]]
        else :
            plot[y+dy].append([x-(dist-dy), x+(dist-dy)+1])

        if (not plot.get(y-dy, False)):
            plot[y-dy] = [[x-(dist-dy), x+(dist-dy)+1]]
        else :
            plot[y-dy].append([x-(dist-dy), x+(dist-dy)+1])
        
        dy += 1
    return x - dist, x + dist

def inter(ax1, ax2, bx1, bx2):
    if (ax2 < bx1 or bx2 < ax1):
        return False
    return True
    

def main():
    file = open(os.path.join(sys.path[0], "input.txt"), "r")
    data = file.read().split("\n")
    file.close()

    sensors = {}
    beacons = []
    plot = {}
    maxX = 0
    minX = 10000000
    for line in data:
        line = line.split(" ")
        x = line[2].replace("x=", "").replace(",", "")
        y = line[3].replace("y=", "").replace(":", "")
        bx = line[8].replace("x=", "").replace(",", "")
        by = line[9].replace("y=", "")
        sensors[x+":"+y] = bx+":"+by
        beacons.append(int(by))

    for sensor in sensors.keys():
        beacon = sensors[sensor]
        sensor = sensor.split(":")
        beacon = beacon.split(":")
        x = int(sensor[0])
        y = int(sensor[1])
        bx = int(beacon[0])
        by = int(beacon[1])
        dist = abs(x-bx)+abs(y-by)

        localMinX, localMaxX = per2(x, y, dist, plot, line)

        maxX = max(localMaxX, maxX)
        minX = min(localMinX, minX)

    beacons = list(dict.fromkeys(beacons))
    # check specific line
    line = 2000000
    line = 10
    c = []
    for boundry in plot[line]:
        c += [ x for x in range(boundry[0], boundry[1])]
        c = list(dict.fromkeys(c))
    c = len(c)
    for b in beacons:
        if (b == line):
            c -= 1
    
    print("Part one:")
    print(c)

    maximum = 4000000
    finished = False
    x, y = 0, 0

    for i in range(0, maximum):
        change = True
        while change:
            change = False
            newBouderies = []
            toRemove = []
            for boundary1 in plot[i]:
                for boundary2 in plot[i][plot[i].index(boundary1):]:
                    if (inter(boundary1[0], boundary1[1], boundary2[0], boundary2[1]) and boundary1 != boundary2):
                        newBouderies.append([min(boundary1[0], boundary2[0]), max(boundary1[1], boundary2[1])])
                        toRemove.append(boundary1)
                        toRemove.append(boundary2)
                        change = True

            for oldBoundary in toRemove:
                if (oldBoundary in plot[i]):
                    plot[i].remove(oldBoundary)

            for newBoundary in newBouderies:
                if (newBoundary not in plot[i]):
                    plot[i].append(newBoundary)

        for boundary in plot[i]:
            if (inter(boundary[0], boundary[1], 0, maximum)):
                if (min(boundary[0], 0) == 0 and boundary[0] != 0):
                    x = boundary[0]-1
                    y = i
                    finished = True
                    break
                if (max(boundary[1], maximum) == maximum):
                    x = boundary1
                    y = i
                    finished = True
                    break
        if finished:
            break

    print("Part two:")
    print(x*maximum+y)

if __name__ == "__main__":
    main()