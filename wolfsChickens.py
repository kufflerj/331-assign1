# Assignment 1: Wolves and Chickens game
# Implemented using Breadth First Search, Depth First Search, Iterative Deepening Search, A* Search
# Authors: Jane Kuffler (kufflerj@oregonstate.edu), Rose Rodarte (rodartes@oregonstate.edu)
# Date: 4/14/22

import sys

# Breadth First Search
# Takes initial and goal states as input and returns the solution path
def bfs(leftS, rightS, leftE, rightE):
    return leftS

# Depth First Search
# Takes initial and goal states as input and returns the solution path
def dfs(leftS, rightS, leftE, rightE):
    return leftS

# Iterative Deepening
# Takes initial and goal states as input and returns the solution path
def iddfs(leftS, rightS, leftE, rightE):
    return leftS

# A-Star Search Depth First Search
# Takes initial and goal states as input and returns the solution path
def aStar(leftS, rightS, leftE, rightE):
    return leftS

if len(sys.argv) != 5:
    print("Error! Please try running in the following format: wolfsChickens.py initial-file goal-file mode output-file")

# store arguments in variables
inFile = open(sys.argv[1], "r")
gFile = open(sys.argv[2], "r")
mode = sys.argv[3]
outFile = open(sys.argv[4], "w")

x = inFile.readline()
leftStart = [int(i) for i in x.split(",")]
x = inFile.readline()
rightStart = [int(i) for i in x.split(",")]
    
inFile.close()

x = gFile.readline()
leftEnd = [int(i) for i in x.split(",")]
x = gFile.readline()
rightEnd = [int(i) for i in x.split(",")]

gFile.close()

print(leftStart)
print(rightStart)
print(leftEnd)
print(rightEnd)

# check if mode is breadth first search
if mode == "bfs":
    print("breadth first search")
# check if mode is breadth first search
elif mode== "dfs":
    print("depth first search")
# if mode is breadth first search
elif mode == "iddfs":  
    print("iterative deepening depth first search")
# if mode is breadth first search
elif mode == "astar":  
    print("a star search")
# if mode is breadth first search
else:
    print("invalid mode")
