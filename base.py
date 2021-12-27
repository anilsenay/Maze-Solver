from create_maze import calculateCityBlockDistances, createMaze
from create_tree import createTree

mazeArray, startNode, goals = createMaze()
root = createTree(mazeArray, startNode) 

frontier, frontierSize, maxFrontierSize = ([], 0, 0)
explored = []
numberOfExpanded = 0 # TODO
depth = 0

def pushToFrontier(node):
    global maxFrontierSize, frontierSize
    frontierSize = frontierSize + 1
    frontier.append(node)
    if(frontierSize > maxFrontierSize): maxFrontierSize = frontierSize

def popFromFrontier(location = -1):
    global frontierSize
    frontierSize = frontierSize - 1
    return frontier.pop(location)

## GENERAL SEARCH ##

def generalSearch(root, strategie, limit = None):
    global frontier, explored, numberOfExpanded
    frontier = []
    explored = []
    pushToFrontier(root)

    while True:
        if (len(frontier) == 0):
            return None
        node = strategie()
        if(node == None):
            return None
        print("\n", node)
        
        explored.append(node)

        if node.isGoal:
            return node

        if(limit != None and node.depth + 1 > limit): continue

        if(len(node.children) != 0):
            numberOfExpanded = numberOfExpanded + 1

        for child in node.children:
            pushToFrontier(child)

def findSolution():
    index = -1
    lastIndex = -len(explored)
    solutionPath = [explored[index]]
    cost = explored[index].cost
    while(index >= lastIndex):
        if(solutionPath[0] in explored[index].children):
            solutionPath.insert(0, explored[index])
            cost = cost + explored[index].cost
        index = index - 1
    for i in solutionPath:
        print(i)
    print("cost: ", cost)


## BFS STRATEGIE ##
def bfsStrategie():
    return popFromFrontier(0)

## DFS STRATEGIE ##
def dfsStrategie():
    index = -1
    while (frontierSize > abs(index) and frontier[-1].depth == frontier[index-1].depth):
        index = index - 1
    return popFromFrontier(index)

## ITERATIVE DEEPENING STRATEGIE ##
def idsStrategie():
    return popFromFrontier()

## UCS STRATEGIE ##
def ucsStrategie():
    frontier.sort(key = lambda x: x.costSoFar) 
    return popFromFrontier(0)

## GREEDY BEST FIRST STRATEGIE ##
def greedyStrategie():
    frontier.sort(key = lambda x: x.square.cityBlockDistance)
    return popFromFrontier(0)

## GREEDY BEST FIRST STRATEGIE ##
def aStarStrategie():
    frontier.sort(key = lambda x: x.square.cityBlockDistance + x.costSoFar)
    return popFromFrontier(0)

calculateCityBlockDistances(mazeArray, goals)
# generalSearch(root, dfsStrategie, 5)
generalSearch(root, dfsStrategie)
print("----------------------------")
findSolution()

## TODO: reset iterative deepening
# for i in range(20):
#     generalSearch(root, dfsStrategie, i)

## PRINT RESULTS ##
print("The maximum size of the explored set during the search.: " + str(len(explored)))
print("Number of expanded nodes: " + str(numberOfExpanded))
print("The maximum size of the frontier: " + str(maxFrontierSize))