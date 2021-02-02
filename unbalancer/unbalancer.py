#!/bin/env python3

import sys

fin = sys.stdin
fout = sys.stdout


def main():

    (N, K) = map(int, fin.readline().strip().split())
    V = list(map(int, fin.readline().strip().split()))

    solution = 0

    for _ in range(0, K+1):
        solution += max(V)
        V.remove(max(V))
        

    
    print(solution)

if __name__ == "__main__":
    main()
