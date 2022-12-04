import os
import sys

def main():
    file = open(os.path.join(sys.path[0], "input"), "r")
    data = file.read().split("\n")
    file.close()

if __name__ == "__main__":
    main()