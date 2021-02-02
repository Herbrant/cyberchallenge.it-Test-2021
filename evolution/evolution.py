#!/bin/env python3

import sys

def getNonEmptyCell(G, i, j, N, M):
    counter = 0

    if i-1 >= 0 and j-1 >= 0 and G[i-1][j-1] != '.':
        counter += 1
    if i-1 >= 0 and G[i-1][j] != '.':
        counter += 1
    if i-1 >= 0 and j+1 < M and G[i-1][j+1] != '.':
        counter += 1
    if j-1 >= 0 and G[i][j-1] != '.':
        counter += 1
    if j+1 < M and G[i][j+1] != '.':
        counter += 1
    if i+1 < N and j-1 >= 0 and G[i+1][j-1] != '.':
        counter += 1
    if i+1 < N and G[i+1][j] != '.':
        counter += 1
    if i+1 < N and j+1 < M and G[i+1][j+1] != '.':
        counter += 1

    return counter

def copyMatrix(A, B, N, M):
    for i in range(0, N):
        for j in range(0, M):
            A[i][j] = B[i][j]


def solve(fin, fout):

    (N, M, K) = map(int, fin.readline().strip().split())

    G = []
    for _ in range(N):
        G.append(list(fin.readline().strip()))

    S = [[0 for i in range(0, N+1)] for i in range(0, M+1)]

    copyMatrix(S, G, N, M)
    
    for _ in range(0, K):
        for i in range(0, N):
            for j in range(0, M):
                if G[i][j] == '.' and getNonEmptyCell(G, i, j, N, M) > 4:
                    S[i][j] = '+'
                elif G[i][j] == '+':
                    if getNonEmptyCell(G, i, j, N, M) > 4:
                        S[i][j] = '*'
                    elif getNonEmptyCell(G, i, j, N, M) < 4:
                        S[i][j] = '.'
                elif G[i][j] == '*':
                    if getNonEmptyCell(G, i, j, N, M) > 4:
                        S[i][j] = '+'
                    elif getNonEmptyCell(G, i, j, N, M) < 4:
                        S[i][j] = '.'
        copyMatrix(G, S, N, M)
                
        

    

    for r in G:
        print("".join(r))

if __name__ == "__main__":
    solve(sys.stdin, sys.stdout)
