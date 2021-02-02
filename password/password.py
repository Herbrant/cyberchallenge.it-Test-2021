#!/bin/env python3

import sys

fin = sys.stdin
fout = sys.stdout

MAX = 256
def compare(arr1, arr2): 
	for i in range(MAX): 
		if arr1[i] != arr2[i]: 
			return 0
	return 1
	
def search(pat, txt):

	M = len(pat) 
	N = len(txt) 

	PCounter = [0]*MAX
	TWCounter = [0]*MAX

	for i in range(M): 
		PCounter[ord(pat[i]) ] += 1
		TWCounter[ord(txt[i]) ] += 1

	for i in range(M,N): 
		if compare(PCounter, TWCounter): 
			return 1
		TWCounter[ ord(txt[i]) ] += 1
		TWCounter[ ord(txt[i-M])] -= 1
	if compare(PCounter, TWCounter): 
		return 1  

def solve():
    correct = 0

    P = fin.readline().strip()
    H = fin.readline().strip()

    correct = search(P, H) 

    if correct:
        print("1")
    else:
        print("0")

def main():
    T = int(fin.readline().strip())
    for _ in range(T):
        solve()

if __name__ == "__main__":
    main()
