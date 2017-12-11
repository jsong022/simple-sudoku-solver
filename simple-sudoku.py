#!/usr/bin/env python3
import sys
import time
#returns True iff i and j indexes are in the same column 
def sameCol(i, j):
	return (abs(i-j)%9 == 0)
#returns True iff i and j indexes are in the same row
def sameRow(i, j):
	return (int(i/9) == int(j/9))
#returns True iff i and j indexes are in the same 3x3 block
def sameBlock(i, j):
	c1 = (int(i/27) == int(j/27))
	c2 = (int((i%9)/3) == int((j%9)/3))
	return (c1 and c2)
#prints a nice looking Sudoku puzzle from a string
#empty spots ('0') are represented by '.'
def printPuzzle(p):
	row = "|"
	for i in range(81):
		if (i%27 is 0): print("-------------")
		row += "." if (p[i] is "0") else p[i]
		row += "|" if (i%3 is 2) else ""
		if (i%9 is 8):
			print(row)
			row = "|"
	print("-------------")
#returns an array of integers
#integers returned are the empty indexes in the puzzle
def findEmpties(puzzle):
	empties = []
	for i in range(len(puzzle)):
		if (puzzle[i] in {' ', '-', '_', '.', '0'}):empties.append(i)
	return empties
#returns true iff 'num' character at position 'index'
#    in the 'puzzle' string is valid
def valid(n, i, p):
	#for each integer from 0 to 80
	for j in range(81):
		if (i is not j):#if in same row/col/block && not 'i' itself
			if (sameRow(i, j) or sameCol(i, j) or sameBlock(i, j)):
				#return false if invalid
				if (int(p[j]) is int(n)): return False				
	return True; #return true if nothing else invalidates it
#returns a new string with 'num' char
#at 'pos' index of 's' string
def replaceChar(num, pos, s):
	return s[:pos] + num + s[pos+1:]
#brute force DFS algorithm
def bruteForce(puzzle):
	emt = findEmpties(puzzle) #array of empty indexes
	ei = 0 #empty Index
	num = 1 #integer [1,9] to brute force through for each index 
	p = puzzle #copy of the problem to edit
	while True: #INFINITE LOOP (will end when solution is returned)
		current = emt[ei] #current empty index
		if valid(str(num), current, p):#if num is valid at current index
			p = replaceChar(str(num), current, p) #write num down for that index
			ei += 1 #and move onto the next empty index
			#if current position is the last one, then puzzle is solved
			if (ei is len(emt)): return p
			else: num = 1 #otherwise move on to next empty square
		else: #num is invalid at current position
			if (num is 9): #if no num was valid
				while (num is 9): #back up to last empty that wasn't 9
					#impossible if must back up past the first empty index
					if (ei is 0): return "Impossible Problem: "+puzzle
					else:
						#make current index empty again
						p = replaceChar('0', current, p)
						#move current index & num back to last-filled empty index
						ei -= 1
						current = emt[ei]
						num = int(p[current])
			num += 1 #increment num
#solve puzzle
def solve(puzzle):
	print("solving....")
	printPuzzle(puzzle)
	startTime = time.time()
	solution = bruteForce(puzzle)
	endTime = time.time()
	if solution[0] is 'I': print(solution)
	else:
		print("Solution found:")
		printPuzzle(solution)
	print("--- %s seconds ---" % (endTime - startTime))
#get custom puzzle as user input
def getPuzzle():
	prompt= "Enter Row  of the problem\n"
	p = ""
	for i in range(9):
		p += input(prompt[:10]+str(i+1)+prompt[10:])
	return p
#main program method. mainly handles inputs
def main():
	p = ""
	if (len(sys.argv) is 1):
		p = getPuzzle()
		if len(p) is not 81: print("Invalid input! "+p)
		else: solve(p)
	else:
		for i in range(len(sys.argv)-1):
			p = sys.argv[i+1]
			if len(p) is not 81: print("Invalid input! "+p)
			else: solve(p)
#run it
main();