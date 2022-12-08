import os
import sys

def main():
    file = open(os.path.join(sys.path[0], "input.txt"), "r")
    data = file.read().split("\n")
    file.close()

    directories = {}
    currentD = []

    for line in data:
        if ("$" in line):
            if ("cd" in line):
                if (line[5:] == ".."):
                    currentD.pop()
                else:
                    currentD.append(line[5:])
                    if (line[5:] not in directories.keys()):
                        directories['/'.join(currentD)] = []
            continue
        elif ("dir" in line):
            directories['/'.join(currentD)].append('/'.join(currentD)+"/"+line[4:])
        else:
            line = line.split(" ")
            directories['/'.join(currentD)].append(int(line[0]))

    closed = {}
    for _ in range(len(directories.keys())):
        for key in directories:
            if (key in closed.keys()):
                continue
            try:
                directories[key] = [ sum(directories[key]) ]
                closed[key] = [ sum(directories[key]) ]
            except:
                for i in range(len(directories[key])):
                    k = directories[key][i]
                    if (type(k) == int):
                        continue
                    if (k in closed.keys()):
                        directories[key][i] = closed[k][0]

    for key in directories:
        directories[key] = sum(directories[key])

    result = 0
    for d in directories:
        if (directories[d] <= 100000):
            result += directories[d]

    print("Part one:")
    print(result)

    space = 30000000-(70000000 - directories["/"])
    result = []
    for key in directories:
        if (directories[key] >= space):
            result.append(directories[key])
    result.sort()

    print("Part two:")
    print(result[0])

if __name__ == "__main__":
    main()