import os
import sys

def main():
    file = open(os.path.join(sys.path[0], "input.txt"), "r")
    data = file.read()
    file.close()

    monkeys = {}
    cM = ""
    # There is a better input handler...
    for line in data.split("\n"):
        line = line.split(" ")
        if ("Monkey" in line):
            cM = line[1].replace(":", "")
            monkeys[cM] = [0, 0, 0, 0, 0, 0]
        elif ("Starting" in line):
            monkeys[cM][0] = ([ int(item.replace(',', '')) for item in line[4:] ])
        elif ("Operation:" in line):
            monkeys[cM][1] = (line[len(line)-3:])
        elif ("Test:" in line):
            monkeys[cM][2] = int(line[5])
        elif ("true:" in line):
            monkeys[cM][3] = line[9]
        elif ("false:" in line):
            monkeys[cM][4] = line[9]

    for round in range(20):
        for monkey in monkeys.keys():
            for item in range(len(monkeys[monkey][0])):
                monkeys[monkey][5] += 1
                item = monkeys[monkey][0].pop()
                w = 0
                opp = monkeys[monkey][1]
                opp = list(map(lambda x : x.replace("old", str(item)), opp))
                if (opp[1] == '+'):
                    w = int(opp[0]) + int(opp[2])
                elif (opp[1] == '-'):
                    w = int(opp[0]) - int(opp[2])
                elif (opp[1] == '*'):
                    w = int(opp[0]) * int(opp[2])
                else:
                    w = int(int(opp[0]) / int(opp[2]))
                
                # w = int(w/3)

                if(w%int(monkeys[monkey][2]) == 0):
                    monkeys[monkeys[monkey][3]][0].append(w)
                else:
                    monkeys[monkeys[monkey][4]][0].append(w)
    
    result = [ monkeys[x][5] for x in monkeys.keys()]
    result.sort()
    result.reverse()
    print("Part one:")
    print(result[0] * result[1])

    monkeys = {}
    cM = ""
    # There is a better input handler...
    for line in data.split("\n"):
        line = line.split(" ")
        if ("Monkey" in line):
            cM = line[1].replace(":", "")
            monkeys[cM] = [0, 0, 0, 0, 0, 0]
        elif ("Starting" in line):
            monkeys[cM][0] = ([ int(item.replace(',', '')) for item in line[4:] ])
        elif ("Operation:" in line):
            monkeys[cM][1] = (line[len(line)-3:])
        elif ("Test:" in line):
            monkeys[cM][2] = int(line[5])
        elif ("true:" in line):
            monkeys[cM][3] = line[9]
        elif ("false:" in line):
            monkeys[cM][4] = line[9]

    divs = [ int(monkeys[x][2]) for x in monkeys.keys() ]
    check = lambda x, y: map(lambda div: x%div == y%div, divs)

    for round in range(10000):
        print(round)
        for monkey in monkeys.keys():
            for item in range(len(monkeys[monkey][0])):
                monkeys[monkey][5] += 1
                item = monkeys[monkey][0].pop()
                w = 0
                opp = monkeys[monkey][1]
                opp = list(map(lambda x : x.replace("old", str(item)), opp))
                if (opp[1] == '+'):
                    w = int(opp[0]) + int(opp[2])
                elif (opp[1] == '-'):
                    w = int(opp[0]) - int(opp[2])
                elif (opp[1] == '*'):
                    w = int(opp[0]) * int(opp[2])
                else:
                    w = int(int(opp[0]) / int(opp[2]))

                if(w%int(monkeys[monkey][2]) == 0):
                    i = 0
                    while (False in check(w, i)):
                        i+=1
                    monkeys[monkeys[monkey][3]][0].append(w)
                else:
                    i = 0
                    while (False in check(w, i)):
                        i+=1
                    monkeys[monkeys[monkey][4]][0].append(w)
    
    result = [ monkeys[x][5] for x in monkeys.keys()]
    result.sort()
    result.reverse()
    print("Part two:")
    print(result[0] * result[1])

if __name__ == "__main__":
    main()