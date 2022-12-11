import os
import sys

def main():
    file = open(os.path.join(sys.path[0], "input.txt"), "r")
    data = file.read().split("\n")
    file.close()

    directions = {"U": [0, 1], "D": [0, -1], "R": [1, 0], "L": [-1, 0]}

    local = lambda a, b : (abs(a[0]-b[0]) <= 1) and (abs(a[1]-b[1]) <= 1)

    visited = []
    currentH = [0, 0]
    currentT = [0, 0]
    prev = None

    for ins in data:
        ins = ins.split(" ")
        direction = ins[0]
        dis = int(ins[1])

        for _ in range(dis):
            if (not local(currentT, currentH)):
                currentT = prev
            if (currentT not in visited):
                visited.append(currentT[:])
            prev = currentH[:]
            currentH[0] += directions[direction][0]
            currentH[1] += directions[direction][1]
    print("Part one:")
    print(len(visited))


    visited = [ [[0, 0]] for _ in range(10) ]
    rope = [ [0, 0] for _ in range(10) ]
    
    for ins in data:
        ins = ins.split(" ")
        direction = ins[0]
        dis = int(ins[1])

        for _ in range(dis):
            prev[0] = rope[0][:]
            rope[0][0] += directions[direction][0]
            rope[0][1] += directions[direction][1]

            for point in range(len(rope)-1):
                headPoint = rope[point]
                tailPoint = rope[point+1]

                if (not local(headPoint, tailPoint)):
                    if (headPoint[0] == tailPoint[0]):
                        if (tailPoint[1] < headPoint[1]):
                            tailPoint[1] += 1
                        else :
                            tailPoint[1] -= 1
                    elif (headPoint[1] == tailPoint[1]):                        
                        if (tailPoint[0] < headPoint[0]):
                            tailPoint[0] += 1
                        else :
                            tailPoint[0] -= 1
                    else:
                        if (tailPoint[0] < headPoint[0]):
                            tailPoint[0] += 1
                        else :
                            tailPoint[0] -= 1
                        if (tailPoint[1] < headPoint[1]):
                            tailPoint[1] += 1
                        else :
                            tailPoint[1] -= 1

                if (tailPoint not in visited[point+1]):
                    visited[point+1].append(tailPoint[:])
                rope[point+1] = tailPoint[:]

    print("Part two:")
    print(len(visited[-1]))

if __name__ == "__main__":
    main()

"""
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
"""