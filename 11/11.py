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

    for _ in range(20):
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
                
                w = int(w/3)

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
    monkeys2 = monkeys.copy()

    for monkey in monkeys.keys():
        newA = []
        a = len(monkeys[monkey][0])
        for i in range(a):
            item = monkeys[monkey][0][i]
            itemlist = [ item%div for div in divs ]
            fullItem = {}
            c = 0
            for monkey2 in monkeys.keys():
                fullItem[monkey2] = itemlist[c]
                c += 1
            newA.append(fullItem)
        monkeys2[monkey][0] = newA

    monkeys = monkeys2.copy()

    for _ in range(10000):
        for monkey in monkeys.keys():
            for item in range(len(monkeys[monkey][0])):
                monkeys[monkey][5] += 1
                item = monkeys[monkey][0].pop()
                fopp = monkeys[monkey][1]
                fullItem = {}
                for i in item.keys():
                    w = 0
                    opp = list(map(lambda x : x.replace("old", str(item[i])), fopp))
                    if (opp[1] == '+'):
                        w = int(opp[0]) + int(opp[2])
                    elif (opp[1] == '-'):
                        w = int(opp[0]) - int(opp[2])
                    elif (opp[1] == '*'):
                        w = int(opp[0]) * int(opp[2])
                    else:
                        w = int(int(opp[0]) / int(opp[2]))
                    fullItem[i] = w%int(monkeys[i][2])
                if(fullItem[monkey] == 0):
                    monkeys[monkeys[monkey][3]][0].append(fullItem)
                else:
                    monkeys[monkeys[monkey][4]][0].append(fullItem)
    
    result = [ monkeys[x][5] for x in monkeys.keys()]
    result.sort()
    result.reverse()
    print("Part two:")
    print(result[0] * result[1])
    
    # 2713310158
    # 2876069637
    # 833266668

if __name__ == "__main__":
    main()