import os
import sys

def main():
    file = open(os.path.join(sys.path[0], "input.txt"), "r")
    data = file.read()
    file.close()

    data = list(data)
    seq = data[:4]

    c = 4
    for ch in data[4:]:
        c += 1
        seq.append(ch)
        seq = seq[1:5]
        
        a = sum([ seq.count(seq[i]) for i in range(0, len(seq)) ])
        if (a == 4):
            print("Part one:")
            print (c)
            break

    data = list(data)   
    seq = data[:14]

    c = 14
    for ch in data[14:]:
        c += 1
        seq.append(ch)
        seq = seq[1:15]

        a = sum([ seq.count(seq[i]) for i in range(0, len(seq)) ])

        if (a == 14):
            print("Part two:")
            print (c)
            break

if __name__ == "__main__":
    main()