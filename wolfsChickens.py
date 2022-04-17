# Assignment 1: Wolves and Chickens game
# Implemented using Breadth First Search, Depth First Search, Iterative Deepening Search, A* Search
# Authors: Jane Kuffler (kufflerj@oregonstate.edu), Rose Rodarte (rodartes@oregonstate.edu)
# Date: 4/14/22

import sys

#Put one chicken in the boat
#Put two chickens in the boat
#Put one wolf in the boat
#Put one wolf and one chicken in the boat
#Put two wolves in the boat

def expand(node):
    #print("Passed node: ", node)
    if node[0] < 0:
            return 
    if node[1] < 0:
        return
    temp = [[node[0]-1, node[1], node[2]], 
            [node[0]-2, node[1], node[2]], 
            [node[0], node[1]-1, node[2]], 
            [node[0]-1, node[1]-1, node[2]], 
            [node[0], node[1]-2, node[2]]]
    for node in temp:
        if node[0] < 0:
            temp.remove(node)
        if node[1] < 0:
            temp.remove(node)
    #print("Expanded temp: ", temp)
    return temp


# Breadth First Search (JK)
# Takes initial and goal states as input and returns the solution path & number of nodes expanded
def bfs(leftS, rightS, leftE, rightE, output):
    counter  = 0
    explored = []
    expanded = []
    temp = [[rightS[0]-1, rightS[1], rightS[2]], 
            [rightS[0]-2, rightS[1], rightS[2]], 
            [rightS[0], rightS[1]-1, rightS[2]], 
            [rightS[0]-1, rightS[1]-1, rightS[2]], 
            [rightS[0], rightS[1]-2, rightS[2]]]
    #print("Original temp: ", temp)
    for node in temp:
        if node[0] < node[1]:
            temp.remove(node)
            #print("skip")
        else:
            #print(node)
            counter = counter + 1
            expanded = expand(node)
            if(expanded):
                for x in expanded:
                    if x not in temp:
                        temp.append(x)
            explored.append(node)
            if(node[0] == 0 and node[1] == 0):
                #print("goal found")
                break
            #print("else frontier: ", temp)
            
    #print(counter)
    #print("Explored ", explored)

    f = open("output", "a")
    f.write("Breadth first search:\n" )
    f.write("Number of nodes expanded: %s\n" % counter)
    for x in explored:
        f.write("%s\n" % x)
    f.close()
        
    return leftS

# Depth First Search (RR)
# Takes initial and goal states as input and returns the solution path & number of nodes expanded
def dfs(leftS, rightS, leftE, rightE, output):
    # initialize counter, frontier and explored set
    counter = 0
    frontier = rightS
    explored = []

    # DFS algorithm


    # write counter and solution path to output

    output.close()

    # print counter and solution
    print(counter)



# Iterative Deepening (JK)
# Takes initial and goal states as input and returns the solution path & number of nodes expanded
def iddfs(leftS, rightS, leftE, rightE, output):
    return leftS

# A-Star Search Depth First Search (RR)
# Takes initial and goal states as input and returns the solution path & number of nodes expanded
def aStar(leftS, rightS, leftE, rightE, output):
    # initialize counter
    counter = 0
    # do alogirthm
    # write counter to output
    # write solution path to output
    # print counter
    # print solution

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

# check if mode is breadth first search
if mode == "bfs":
    print("breadth first search")
    bfs(leftStart, rightStart, leftEnd, rightEnd, outFile)
# check if mode is breadth first search
elif mode== "dfs":
    dfs(leftStart, rightStart, leftEnd, rightEnd, outFile)
# if mode is breadth first search
elif mode == "iddfs":  
    print("iterative deepening depth first search")
# if mode is breadth first search
elif mode == "astar":  
    print("a star search")
# if mode is breadth first search
else:
    print("invalid mode")
    outFile.close()
