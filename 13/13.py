import os
import sys

def listAppend(l):
    c = 1
    newList = []
    while (l[c] != "]"):
        if (l[c] == "["):
            partList = listAppend(l[c:])
            newList.append(partList[1])
            c += partList[0]
        else:
            newList.append(int(l[c]))
        c += 1
    return [c, newList]

def cmp(cmp1, cmp2):
    if (type(cmp1) == int and type(cmp2) == int):
        if (cmp1 < cmp2):
            return True
        elif (cmp1 == cmp2):
            return None
        else :
            return False

    else :
        if (type(cmp2) == int):
            cmp2 = [cmp2]
        if (type(cmp1) == int):
            cmp1 = [cmp1]
        
        val = None
        c = 0
        while (val == None and c < len(cmp1)):
            if (c >= len(cmp2)):
                val = False
                break
            val = cmp(cmp1[c], cmp2[c])
            c += 1
        if (val == None and len(cmp1) < len(cmp2)):
            val = True
        return val

def main():
    file = open(os.path.join(sys.path[0], "input.txt"), "r")
    data = file.read().split("\n")
    file.close()

    wrongOrder = []
    rightOrder = []
    result = 0

    for packet in range(0, len(data), 3):
        li = False
        skip = False
        left = list(data[packet])
        right = list(data[packet+1])
        for i in range(len(left)):
            try:
                _ = int(left[i])
                if (li and not skip):
                    left[i-1] = left[i-1]+left[i]
                    skip = True
                li = True
            except:
                skip = False
                li = False
                pass
        for i in range(len(right)):
            try:
                _ = int(right[i])
                if (li and not skip):
                    right[i-1] = right[i-1]+right[i]
                    skip = False
                li = True
            except:
                skip = False
                li = False
                pass
        left = [ x for x in left if x != ',']
        right = [ x for x in right if x != ',']

        left = listAppend(left)[1]
        right = listAppend(right)[1]
        comparison = cmp(left, right)

        if (comparison == True):
            rightOrder.append(left[:])
            rightOrder.append(right[:])
            result += int(packet/3)+1
        else :
            wrongOrder.append(left[:])
            wrongOrder.append(right[:])

    print("Part one:")
    print(result)

    order = []
    allPackets = rightOrder+wrongOrder+[[[2]], [[6]]]
    for e in allPackets:
        order.append([e[:], 0])
        for e2 in allPackets:
            comparison = cmp(e, e2)
            if comparison:
                order[-1][1] += 1
    order.sort(key=lambda x: x[1], reverse=True)
    for e in order:
        if (e[0] == [[2]]):
            a = order.index(e)+1
        elif (e[0] == [[6]]):
            b = order.index(e)+1

    print("Part two:")
    print(a*b)

if __name__ == "__main__":
    main()