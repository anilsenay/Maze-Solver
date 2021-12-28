from create_maze import calculateCityBlockDistances, createMaze
from create_tree import createTree

frontier, frontierSize, maxFrontierSize = ([], 0, 0)
explored = []
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
    global frontier, explored
    frontier = []
    explored = []
    pushToFrontier(root)

    while True:
        if (len(frontier) == 0):
            return None
        node = strategie()
        if(node == None):
            return None
        
        explored.append(node)

        if node.isGoal:
            return node

        if(limit != None and node.depth + 1 > limit): continue

        for child in node.children:
            pushToFrontier(child)

## BFS STRATEGY ##
def bfsStrategy():
    return popFromFrontier(0)

## DFS STRATEGY ##
def dfsStrategy():
    index = -1
    while (frontierSize > abs(index) and frontier[-1].depth == frontier[index-1].depth):
        index = index - 1
    return popFromFrontier(index)

## UCS STRATEGY ##
def ucsStrategy():
    frontier.sort(key = lambda x: x.costSoFar) 
    return popFromFrontier(0)

## GREEDY BEST FIRST STRATEGY ##
def greedyStrategy():
    frontier.sort(key = lambda x: x.square.cityBlockDistance)
    return popFromFrontier(0)

## A* STRATEGY ##
def aStarStrategy():
    frontier.sort(key = lambda x: x.square.cityBlockDistance + x.costSoFar)
    return popFromFrontier(0)

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
    solutionPathString = ""
    for node in solutionPath:
        solutionPathString = solutionPathString + "(" + str(node.square.x) + "," + str(node.square.y) + ") - "
    solutionPathString = solutionPathString[:-2]
    return [cost, solutionPathString]

def main():
    print("Welcome to Maze Solver")
    mazeName = input("Please enter the maze file [maze_1]: ") or "maze_1"
    
    mazeArray, startNode, goals = createMaze(mazeName)
    root, maxDepth = createTree(mazeArray, startNode) 

    selection = askStrategy()

    if(selection == 1):
        generalSearch(root, dfsStrategy)
    elif(selection == 2):
        generalSearch(root, bfsStrategy)
    elif(selection == 3):
        for i in range(maxDepth):
            goal = generalSearch(root, dfsStrategy, i)
            if(goal != None): break
    elif(selection == 4):
        generalSearch(root, ucsStrategy)
    elif(selection == 5):
        calculateCityBlockDistances(mazeArray, goals)
        generalSearch(root, greedyStrategy)
    elif(selection == 6):
        calculateCityBlockDistances(mazeArray, goals)
        generalSearch(root, aStarStrategy)

    printResults()

def askStrategy():
    print("Please select a search strategie")
    print("1 - Depth First Search")
    print("2 - Breadth First Search")
    print("3 - Iterative Deepening")
    print("4 - Uniform Cost Search")
    print("5 - Greedy Best First Search")
    print("6 - A* Heuristic Search")

    selection = int(input("Type your selection number: "))
    while(not(selection == 1 or selection == 2 or selection == 3 or selection == 4 or selection == 5 or selection == 6)):
        print("Please type a valid number\n")
        selection = askStrategy()
    return selection

## PRINT RESULTS ##
def printResults():
    cost, solutionPath = findSolution()
    print("The cost of the solution found: " + str(cost))
    print("Number of expanded nodes: " +  str(len(explored)))
    print("The maximum size of the frontier: " + str(maxFrontierSize))
    print("The maximum size of the explored set during the search: " + str(len(explored)))
    print("Solution Path: " + str(solutionPath))
    
main()