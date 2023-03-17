import os
import sys

def dij(queue, valves, dist, dists, distLimit):

    valve = queue.pop()
    dists.append((valve, dist))
    tunnels = valves[valve][1]
    dist += 1

    for tunnel in [ x for x in tunnels if x not in [ x[0] for x in dists ] + queue ]:
        queue.append(tunnel)

    if (dist > distLimit or queue == []):
        return

    dij(queue, valves, dist, dists, distLimit)

def traverse(valve, valves, timeLimit, pressure):

    while (timeLimit >= 0):

        nextValve = valve
        dists = []
        dij([nextValve], valves, 0, dists, timeLimit)
        pressure += valves[max(dists)[0]][0] * (timeLimit - (max(dists)[1] + 1))
        timeLimit -= max(dists)[1]+1
        
        nextValve = max(dists)[0]

    return pressure

def main():
    file = open(os.path.join(sys.path[0], "input.txt"), "r")
    data = file.read().split("\n")
    file.close()

    time = 30 # minutes
    valves = {}
    maxOpenValves = []

    for valve in data:
        valve = valve.split(" ")
        flow = valve[4].replace("rate=", "").replace(";", "")
        tunnels = valve[9:]
        for i in range(len(tunnels)-1):
            tunnels[i] = tunnels[i][:len(tunnels[i])-1]
        if (int(flow) != 0):
            maxOpenValves.append(valve[1])
        valves[valve[1]] = (int(flow), tunnels)

    print(traverse("AA", valves, time, 0))

    maxPressure = 0
    print("Part one:")
    print(maxPressure)

if __name__ == "__main__":
    main()