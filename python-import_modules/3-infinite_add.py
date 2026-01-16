#!/usr/bin/python3
import sys

if __name__ == "__main__":
    total = 0

    for i in range(1, len(sys.argv)):
        total = total + int(sys.argv[i])

    print(total)
