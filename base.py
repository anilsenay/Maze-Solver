from create_maze import calculateCityBlockDistances, createMaze
from create_tree import createTree


mazeArray, startNode, goals = createMaze()
root = createTree(mazeArray, startNode) 

frontier, frontierSize, maxFrontierSize = ([], 0, 0)
explored = []
expanded = [] # TODO
cost = 0
depth = 0

def pushToFrontier(node):
    global maxFrontierSize
    global frontierSize
    frontierSize = frontierSize + 1
    frontier.append(node)
    if(frontierSize > maxFrontierSize): maxFrontierSize = frontierSize

def popFromFrontier():
    global frontierSize
    frontierSize = frontierSize - 1
    return frontier.pop(0)

## BREADTH FIRST SEARCH ##

def bfs(root):
    global frontier 
    frontier = []
    global explored
    explored = []
    cost = 0
    pushToFrontier(root)
    while True:
        if (len(frontier) == 0):
            return "Error! Frontier is empty."
        node = popFromFrontier()
        
        # print(node.square)
        explored.append(node.square)
        cost = cost + node.cost
        for child in node.children:
            if (child.isGoal):
                cost = cost + child.cost
                # explored.append(child.square) should not be added
                return cost
            if (child.square in explored):
                continue
            pushToFrontier(child)
            

# result = bfs(root)
# print(result)


## DEPTH FIRST SEARCH ##

def dfs():
    global depth
    depth = 0
    pushToFrontier(root)
    goal = recursiveDfs(root)
    print(goal)
    print(len(explored))
    print(cost)

def recursiveDfs(node):
    global depth   
    popFromFrontier()
    explored.append(node.square)

    global cost
    cost = cost + node.cost

    if(node.isGoal):
        return node
    for child in node.children:
        pushToFrontier(child)

    depth = depth + 1

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
    pushToFrontier(root)
    goal = recursiveDls(root, limit)
    print(goal)
    print(len(explored))
    print(cost)
    return goal

def recursiveDls(node, limit):
    global depth   
    if(depth > limit):
        return

    popFromFrontier()
    explored.append(node.square)

    global cost
    cost = cost + node.cost

    if(node.isGoal):
        return node
    for child in node.children:
        pushToFrontier(child)
        print("child:", child)

    depth = depth + 1

    for child in node.children:
        result = recursiveDls(child, limit)
        if(result != None): 
            return result
    depth = depth - 1

# dls(root, 5)

## ITERATIVE DEEPENING SEARCH ##

def iterativeDeepening(root, limit):
    result = None
    for i in range(limit):
        dlsResult = dls(root, i)
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
    frontier.append(root)

    while True:
        frontier.sort(key = lambda x: x.costSoFar, reverse=True) 
        node = frontier.pop()
        print(node, node.costSoFar)

        if node.isGoal:
            return node
         
        for child in node.children:
            child.costSoFar = node.costSoFar + child.cost
            frontier.append(child)

goal = ucs(root)
print(goal)




### TODO ###
## GREEDY BEST FIRST SEARCH ##

def greedyBestFirstSearch(root, mazeArray, goals):
    calculateCityBlockDistances(mazeArray, goals)
    for row in mazeArray:
        for node in row:
            print(node, node.cityBlockDistance)

## A* HEURISTIC SEARCH ##

def aHeuristicSearch(root, mazeArray, goals):
    calculateCityBlockDistances(mazeArray, goals)
    for row in mazeArray:
        for node in row:
            print(node, node.cityBlockDistance)
