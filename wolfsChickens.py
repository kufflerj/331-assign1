# Assignment 1: Wolves and Chickens game
# Implemented using Breadth First Search, Depth First Search, Iterative Deepening Search, A* Search
# Authors: Jane Kuffler (kufflerj@oregonstate.edu), Rose Rodarte (rodartes@oregonstate.edu)
# Date: 4/14/22

import sys, math
from queue import PriorityQueue


# Order of moves (skip invalid moves):
#    1. Put one chicken in the boat
#    2. Put two chickens in the boat
#    3. Put one wolf in the boat
#    4. Put one wolf and one chicken in the boat
#    5. Put two wolves in the boat

def expand(node):
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
    return temp

# prints a solution to console and file
def prettyPrint(count, right, left, expr, expl, output):
    
    # output to file
    output.write("Number of nodes expanded: " + str(count) + "\n")
    output.write("%s" % right)
    output.write(" || ")
    output.write("%s" % left)
    output.write("\n")
    for ind in range(len(expr)):
        output.write("%s" % expr[ind])
        output.write(" || ")
        output.write("%s" % expl[ind])
        output.write("\n")

    # output to console
    print("Number of Nodes Expanded: " + str(count))
    print("Solution:")
    print(str(right) + " || " + str(left))
    for ind in range(len(expr)):
        print(str(expr[ind]) + " || " + str(expl[ind]))
    

# Breadth First Search (JK)
# Takes initial and goal states as input and returns the solution path & number of nodes expanded
def bfs(leftS, rightS, leftE, rightE, output):
    counter  = 1
    explored = []
    expanded = []
    explored_left = []
    temp = [[rightS[0]-1, rightS[1], rightS[2]], 
            [rightS[0]-2, rightS[1], rightS[2]], 
            [rightS[0], rightS[1]-1, rightS[2]], 
            [rightS[0]-1, rightS[1]-1, rightS[2]], 
            [rightS[0], rightS[1]-2, rightS[2]]]
    
    temp.reverse()
    while(temp):
        node = temp.pop()
        leftGroup = [0, 0, 0]
        for i in range(3):
            diff = rightS[i] - node[i]
            leftGroup[i] = diff
        if node[0] < node[1]:
            pass
        elif (node[0] < 0) or (node[1] < 0):
            pass
        elif(leftGroup[0] < leftGroup[1]):
            pass
        else:
            #print(node)
            counter = counter + 1
            expanded = expand(node)
            if(expanded):
                for x in expanded:
                    if x not in temp:
                        temp.append(x)
            explored.append(node)
            explored_left.append(leftGroup)
            if(node[0] == rightE[0] and node[1] == rightE[1]):
                #print("goal found")
                break


    output.write("Breadth first search\n" )
    prettyPrint(counter, rightS, leftS, explored, explored_left, output)
    output.close()
        

# Depth First Search using graph search (RR)
# Takes initial and goal states as input and returns the solution path & number of nodes expanded
def dfs( rightS, leftS, rightE, output):
    # initialize counter, frontier and explored set
    counter = 1
    explored = []
    explored_left = []
    # all possible moves in order using a LIFO queue
    frontier = [[rightS[0]-1, rightS[1], rightS[2]], 
            [rightS[0]-2, rightS[1], rightS[2]], 
            [rightS[0], rightS[1]-1, rightS[2]], 
            [rightS[0]-1, rightS[1]-1, rightS[2]], 
            [rightS[0], rightS[1]-2, rightS[2]]]

    # DFS algorithm
    while(frontier):
        node = frontier.pop()
        leftGroup = [0, 0, 0]
        for i in range(3):
            diff = rightS[i] - node[i]
            leftGroup[i] = diff
        # there cannot be less chickens than wolves
        if node[0] < node[1]:
            pass
        # there cannot be negative chickens or negative wolves
        elif (node[0] < 0) or (node[1] < 0):
            pass
        # make sure there are not more chickens than wolves on the opposite side of river
        elif(leftGroup[0] < leftGroup[1]):
                pass
        else:
            # counter is increased and each node in the queue is expanded fully before the next
            counter = counter + 1
            expanded = expand(node)
            if(expanded):
                for x in expanded:
                    if x not in frontier:
                        frontier.append(x)
            explored.append(node)
            explored_left.append(leftGroup)
            # if the goal state is reached
            if(node[0] == rightE[0] and node[1] == rightE[1]):
                break

    # output counter and solution path
    output.write("Depth first search\n" )
    prettyPrint(counter, rightS, leftS, explored, explored_left, output)
    # close the output file
    output.close()



# Iterative Deepening (JK)
# Takes initial and goal states as input and returns the solution path & number of nodes expanded
def iddfs(leftS, rightS, leftE, rightE, output):
    counter = 1
    explored = []
    explored_left = []
    # all possible moves in order using a LIFO queue
    frontier = [[rightS[0]-1, rightS[1], rightS[2]], 
            [rightS[0]-2, rightS[1], rightS[2]], 
            [rightS[0], rightS[1]-1, rightS[2]], 
            [rightS[0]-1, rightS[1]-1, rightS[2]], 
            [rightS[0], rightS[1]-2, rightS[2]]]
    #maxDepth is set to be 2* the original number of chickens
    maxDepth = (rightS[0])*2
    for i in range(maxDepth):
        #dfs algorithm here 
        node = frontier.pop()
        leftGroup = [0, 0, 0]
        for i in range(3):
            diff = rightS[i] - node[i]
            leftGroup[i] = diff
        # there cannot be less chickens than wolves
        if node[0] < node[1]:
                pass
        # there cannot be negative chickens or negative wolves
        elif (node[0] < 0) or (node[1] < 0):
            pass
        # make sure there are not more chickens than wolves on the opposite side of river
        elif(leftGroup[0] < leftGroup[1]):
            pass
        else:
        # counter is increased and each node in the queue is expanded fully before the next
            counter = counter + 1
            expanded = expand(node)
            if(expanded):
                for x in expanded:
                    if x not in frontier:
                        frontier.append(x)
            explored.append(node)
            explored_left.append(leftGroup)
        # if the goal state is reached
            if(node[0] == rightE[0] and node[1] == rightE[1]):
                print("GOAL FOUND")
                break

    output.write("Iterative Deepening Depth first search-\n")
    prettyPrint(counter, rightS, leftS, explored, explored_left, output)
    output.close()
    

# A-Star Search Depth First Search (RR)
# Takes initial and goal states as input and returns the solution path & number of nodes expanded
def aStar(leftS, rightS, rightE, output):
    # initialize counter, frontier and explored sets
    counter = 1
    explored = []
    explored_left = []
    # all possible moves from expanding a node
    frontier = [[rightS[0]-1, rightS[1], rightS[2]], 
            [rightS[0]-2, rightS[1], rightS[2]], 
            [rightS[0], rightS[1]-1, rightS[2]], 
            [rightS[0]-1, rightS[1]-1, rightS[2]], 
            [rightS[0], rightS[1]-2, rightS[2]]] 
    # calculate heuristics of each move
    heurs = []
    f = PriorityQueue()
    for node in frontier:
        h = math.sqrt((node[0]-rightE[0])^2 + (node[1]-rightE[1])^2)
        heurs.append(h)
    for i in range(len(frontier)):
        f.put((heurs[i], frontier[i]))

    # A* algorithm
    while(frontier):
        node = f.get()
        # find a heuristic
        leftGroup = [0, 0, 0]
        for i in range(3):
            diff = rightS[i] - node[1][i]
            leftGroup[i] = diff
        # there cannot be less chickens than wolves
        if node[1][0] < node[1][1]:
            pass
        # there cannot be negative chickens or negative wolves
        elif (node[1][0] < 0) or (node[1][1] < 0):
            pass
        # make sure there are not more chickens than wolves on the opposite side of river
        elif(leftGroup[0] < leftGroup[1]):
            pass
        else:
            # else increase counter and expand the node
            counter = counter + 1
            expanded = expand(node[1])
            if(expanded):
                for x in expanded:
                    h = math.sqrt((node[1][0]-rightE[0])^2 + (node[1][1]-rightE[1])^2)
                    f.put((h, x))
            explored.append(node[1])
            explored_left.append(leftGroup)
            # if the goal is found
            if(node[1][0] == rightE[0] and node[1][1] == rightE[1]):
                print("GOAL FOUND")
                break

    # write counter and solution path to output
    output.write("A* search-\n")
    prettyPrint(counter, rightS, leftS, explored, explored_left, output)
    # close the output file
    output.close()

# driver code below

# make sure the user has 5 arguments
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
# close the initial state file    
inFile.close()

x = gFile.readline()
leftEnd = [int(i) for i in x.split(",")]
x = gFile.readline()
rightEnd = [int(i) for i in x.split(",")]
# close the goal state file
gFile.close()

# check if mode is breadth first search
if mode == "bfs":
    print("Breadth first search:")
    bfs(leftStart, rightStart, leftEnd, rightEnd, outFile)
# check if mode is depth first search
elif mode== "dfs":
    print("Depth first search:")
    dfs(rightStart, leftStart, rightEnd, outFile)
# check if mode is iterative deepening dfs
elif mode == "iddfs":  
    print("iterative deepening depth first search")
    iddfs(leftStart, rightStart, leftEnd, rightEnd, outFile)
# check if mode is A* search
elif mode == "astar":  
    print("A* search:")
    aStar(leftStart, rightStart, rightEnd, outFile)
# all other modes are not valid, so close the file and quit
else:
    print("invalid mode")
    outFile.close()
