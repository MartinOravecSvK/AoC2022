import os
import sys

def queueF(queue):
    newQueue = [queue.pop(0)]

    for item in queue[1:]:
        i = 0
        while (item[1]>newQueue[i][1]):
            i += 1
            if (len(newQueue) <= i):
                break
        newQueue = newQueue[:i] + [item] + newQueue[i+1:]

    return newQueue

def dij(queue, graph, maxDistance, reachedNodes):
    currentNode = queue.pop(0)
    currentDistance = currentNode[1]
    if (currentNode in reachedNodes):
        return
    reachedNodes.append(currentNode)

    adjacentNodes = graph[currentNode[0]][1]
    for node in adjacentNodes:
        if (node in [ x[0] for x in reachedNodes ]):
            continue
        queue.append((node, currentDistance+1))

    if (len(queue) == 0 or currentDistance >= maxDistance):
        return
    
    queue = queueF(queue)
    dij(queue, graph, maxDistance, reachedNodes)

def maximumPressure(valve, valves, timeLimit, pressure):
    nextValve = valve
    openValves = []

    while (timeLimit >= 0):
        best = ["", 0, 0]
        valvePriorityList = []
        dij([(nextValve, 0)], valves, timeLimit, valvePriorityList)

        for i in range(len(valvePriorityList)):
            v, timeUsed = valvePriorityList[i]
            if ((timeLimit-timeUsed)*valves[v][0] > best[1] and v not in openValves):
                best = [v, (timeLimit-timeUsed)*valves[v][0], timeUsed]
        
        nextValve = best[0]
        if (nextValve == ""):
            break
        pressure += best[1]
        timeLimit -= best[2]
        openValves.append(nextValve)

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

    maxPressure = maximumPressure("AA", valves, time, 0)

    print("Part one:")
    print(maxPressure)

if __name__ == "__main__":
    main()