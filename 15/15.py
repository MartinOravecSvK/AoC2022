import os
import sys

def per2(x, y, dist, plot, line):
    dy = 0
    while dist >= dy:

        if (not plot.get(y+dy, False)):
            plot[y+dy] = list()
        if (not plot.get(y-dy, False)):
            plot[y-dy] = list()

        if (y+dy == line):
            plot[y+dy] = list(dict.fromkeys(plot[y+dy] + ([ x for x in range(x-(dist-dy), x+(dist-dy)+1) ])))
        if (y-dy == line):
            plot[y-dy] = list(dict.fromkeys(plot[y-dy] + ([ x for x in range(x-(dist-dy), x+(dist-dy)+1) ])))
        
        dy += 1
    return x - dist, x + dist

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

    line = 2000000
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
    # check specific
    c = 0
    c = len(plot[line])
    for b in beacons:
        if (b == line):
            c -= 1
    
    print("Part one:")
    print(c)

    # limits 0 - 4000000

if __name__ == "__main__":
    main()