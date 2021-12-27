from create_maze import calculateCityBlockDistances, createMaze
from create_tree import createTree


mazeArray, startNode, goals = createMaze()
root = createTree(mazeArray, startNode) 

frontier, frontierSize, maxFrontierSize = ([], 0, 0)
explored = []
numberOfExpanded = 0 # TODO
cost = 0
depth = 0
limit = 5

def pushToFrontier(node):
    global maxFrontierSize
    global frontierSize
    frontierSize = frontierSize + 1
    frontier.append(node)
    if(frontierSize > maxFrontierSize): maxFrontierSize = frontierSize

def popFromFrontier(location = -1):
    global frontierSize
    frontierSize = frontierSize - 1
    return frontier.pop(location)

## GENERAL SEARCH ##

def generalSearch(root, strategie, limit = None):
    global frontier 
    frontier = []
    global explored
    explored = []
    cost = 0
    pushToFrontier(root)

    while True:
        if (len(frontier) == 0):
            return None
        node = strategie()
        if(node == None):
            return None
        print("\n", node)
        if node.isGoal:
            return node

        explored.append(node)

        if(limit != None and node.depth + 1 > limit): continue

        if(len(node.children) != 0):
            global numberOfExpanded
            numberOfExpanded = numberOfExpanded + 1

        for child in node.children:
            pushToFrontier(child)

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
generalSearch(root, aStarStrategie)
# for i in range(20):
#     generalSearch(root, dfsStrategie, i)

## BREADTH FIRST SEARCH ##

def bfs(root):
    global frontier 
    frontier = []
    global explored
    explored = []
    cost = 0
    pushToFrontier(root)
    explored.append(root)

    while True:
        if (len(frontier) == 0):
            return "Error! Frontier is empty."
        node = popFromFrontier()
        print(node)
        if node.isGoal:
            return node

        if(len(node.children) != 0):
            global numberOfExpanded
            numberOfExpanded = numberOfExpanded + 1
        
        cost = cost + node.cost

        for child in node.children:
            pushToFrontier(child)
            explored.append(child)
            

# result = bfs(root)
# print(result)


## DEPTH FIRST SEARCH ##

def dfs():
    global depth
    depth = 0
    pushToFrontier(root)
    explored.append(root)
    goal = recursiveDfs(root)
    print(goal)
    print(cost)

def recursiveDfs(node):
    global depth   
    popFromFrontier()
    print(node)

    global cost
    cost = cost + node.cost

    if(node.isGoal):
        return node
    for child in node.children:
        pushToFrontier(child)

    depth = depth + 1

    if(len(node.children) != 0):
        global numberOfExpanded
        numberOfExpanded = numberOfExpanded + 1

    for child in node.children:
        explored.append(child)

    for child in node.children:
        result = recursiveDfs(child)
        if(result != None): 
            return result
    depth = depth - 1
    


# dfs()

## DEPTH LIMITED SEARCH ##

def dls(root, limit):
    global depth
    depth = 0

    ## TODO: should we restart these for each iterative deepening step??
    global numberOfExpanded, explored, frontier, frontierSize, maxFrontierSize
    numberOfExpanded = 0
    explored = []
    frontier = []
    maxFrontierSize = 0
    frontierSize = 0
    ##

    pushToFrontier(root)
    explored.append(root)
    goal = recursiveDls(root, limit)
    print(goal)
    print(cost)
    return goal

def recursiveDls(node, limit):
    global depth   
    if(depth > limit):
        return

    popFromFrontier()
    print(node)

    global cost
    cost = cost + node.cost

    if(node.isGoal):
        return node
    for child in node.children:
        pushToFrontier(child)

    depth = depth + 1

    if(len(node.children) != 0 and depth <= limit):
        global numberOfExpanded
        numberOfExpanded = numberOfExpanded + 1
        for child in node.children:
            explored.append(child)

    for child in node.children:
        result = recursiveDls(child, limit)
        if(result != None): 
            return result
    depth = depth - 1

# dls(root, 20)

## ITERATIVE DEEPENING SEARCH ##

def iterativeDeepening(root, limit):
    result = None
    for i in range(limit):
        dlsResult = dls(root, i)
        print("\n-----------------------------------\n")
        if(dlsResult != None):
            result = dlsResult
            break
    print(result)

# iterativeDeepening(root, 30)


## UNIFORM COST SEARCH ##

def ucs(root):
    global frontier 
    frontier = []
    global explored
    explored = []
    root.costSoFar = 0
    pushToFrontier(root)
    explored.append(root)

    while True:
        frontier.sort(key = lambda x: x.costSoFar) 
        node = popFromFrontier()
        print(node, node.costSoFar)

        if node.isGoal:
            return node
        
        if(len(node.children) != 0):
            global numberOfExpanded
            numberOfExpanded = numberOfExpanded + 1
         
        for child in node.children:
            child.costSoFar = node.costSoFar + child.cost
            pushToFrontier(child)
            explored.append(child)

# goal = ucs(root)
# print(goal)


### TODO ###
## GREEDY BEST FIRST SEARCH ##

def greedyBestFirstSearch(root, mazeArray, goals):
    calculateCityBlockDistances(mazeArray, goals)
    global explored
    explored = []
    global frontier 
    frontier = []
    
    pushToFrontier(root)
    explored.append(root)

    while True:
        if (len(frontier) == 0):
            return "Error! Frontier is empty."
        
        frontier.sort(key = lambda x: x.square.cityBlockDistance)
        node = popFromFrontier()
        print(node.square)
        if (node.isGoal):
            return node

        if(len(node.children) != 0):
            global numberOfExpanded
            numberOfExpanded = numberOfExpanded + 1
            
        for child in node.children:
            explored.append(child)
            pushToFrontier(child)

# greedyBestFirstSearch(root, mazeArray, goals)

## A* HEURISTIC SEARCH ##

def aHeuristicSearch(root, mazeArray, goals):
    calculateCityBlockDistances(mazeArray, goals)
    for row in mazeArray:
        for node in row:
            print(node, node.cityBlockDistance)


## PRINT RESULTS ##
print("The maximum size of the explored set during the search.: " + str(len(explored)))
print("Number of expanded nodes: " + str(numberOfExpanded))
print("The maximum size of the frontier: " + str(maxFrontierSize))