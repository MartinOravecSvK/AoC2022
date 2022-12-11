import os
import sys

def main():
    file = open(os.path.join(sys.path[0], "input.txt"), "r")
    data = file.read().split("\n")
    file.close()

    x = 1
    pc = 0
    ic = 0
    result = 0
    crt = []
    print("Part two:")
    while True:
        pc += 1
        pos0 = len(crt)-1
        pos1 = len(crt)+1
        if (pos0 <= x and x <= pos1):
            crt.append("X")
        else:
            crt.append(".")

        ins = data[ic].split(" ")
        ic += 1
        if(len(data) <= ic):
            break
        if (pc%20 == 0 and (pc/20)%2 == 1):
            result += pc*int(x)
        if (pc%40 == 0):
            for e in crt:
                print(e, end="")
            print()
            crt = []
        if (ins[0] == "addx"):
            pc += 1
            pos0 = len(crt)-1
            pos1 = len(crt)+1
            if (pos0 <= x and x <= pos1):
                crt.append("X")
            else:
                crt.append(".")

            if (pc%20 == 0 and (pc/20)%2 == 1):
                result += pc*int(x)
            if (pc%40 == 0):
                for e in crt:
                    print(e, end="")
                print()
                crt = []
            x += int(ins[1])
        else:
            pass
    if (pc%40 == 0):
        for e in crt:
            print(e, end="")
        print()
        crt = []
    print("Part one:")
    print(result)
if __name__ == "__main__":
    main()