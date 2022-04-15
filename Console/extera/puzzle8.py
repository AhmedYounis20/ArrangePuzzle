"""
Puzzle8 Game
-------------
| 0 | 1 | 2 |
-------------
| 3 | 4 | 5 |
-------------
| 6 | 7 | 8 |
-------------
"""

from random import randrange
from functions import *
from SearchAgent import *

def print_puzzle(puzzle):
	p=''
	for i in puzzle:
		if i==0: p+=' '
		else: p+=str(i)
	print (
		'-'*13 + '\n' +
		'| ' + p[0] + ' | ' + p[1] + ' | ' + p[2] + ' |' + '\n' +
		'-'*13 + '\n' +
		'| ' + p[3] + ' | ' + p[4] + ' | ' + p[5] + ' |' + '\n' +
		'-'*13 + '\n' +
		'| ' + p[6] + ' | ' + p[7] + ' | ' + p[8] + ' |' + '\n' +
		'-'*13
		)

def shuffle_puzzle(n):
	puzzle=[0, 1, 2, 3, 4, 5, 6, 7, 8]
	for _ in range(n):
		actions=possibleMoves(puzzle)
		rand_index=randrange(0,len(actions))
		puzzle=Move(puzzle,actions[rand_index])
	return puzzle

if __name__ == '__main__':
	puzzle=shuffle_puzzle(50)

	Stratgy=input("enter stratgy: ")
	if Stratgy.upper()=="DFS":
		puzzle=puzzle=[1, 0, 2, 6, 3, 5, 4, 7, 8]
	print_puzzle(puzzle)
	print(solve(Stratgy.upper(),puzzle))

	#use the implelemented search strategies (DFS,BFS,UCS) to solve the puzzle
	#print the final solution and the number of expanded nodes for each strategy
	#for DFS use this puzzle [1, 0, 2, 6, 3, 5, 4, 7, 8]
