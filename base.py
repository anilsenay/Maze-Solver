from create_maze import createMaze
from create_tree import createTree


mazeArray, startNode = createMaze()
root = createTree(mazeArray, startNode) 

frontier = []
explored = []
cost = 0
depth = 0

## BREADTH FIRST SEARCH ##

def bfs(root):
    global frontier 
    frontier = []
    global explored
    explored = []
    cost = 0
    frontier.append(root)
    while True:
        if (len(frontier) == 0):
            return "Error! Frontier is empty."
        node = frontier.pop(0)
        
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
            frontier.append(child)
            

# result = bfs(root)
# print(result)


## DEPTH FIRST SEARCH ##

def dfs():
    global depth
    depth = 0
    frontier.append(root)
    goal = recursiveDfs(root)
    print(goal)
    print(len(explored))
    print(cost)

def recursiveDfs(node):
    global depth   

    print(node)
    print("Count: ",len(frontier))
    print("depth: ",depth, "\n")
    frontier.pop()
    explored.append(node.square)

    global cost
    cost = cost + node.cost

    if(node.isGoal):
        return node
    for child in node.children:
        frontier.append(child)

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
    frontier.append(root)
    goal = recursiveDls(root, limit)
    print(goal)
    print(len(explored))
    print(cost)
    return goal

def recursiveDls(node, limit):
    global depth   
    if(depth > limit):
        return

    print(node)
    print("Count: ",len(frontier))
    print("depth: ",depth, "\n")
    frontier.pop()
    explored.append(node.square)

    global cost
    cost = cost + node.cost

    if(node.isGoal):
        return node
    for child in node.children:
        frontier.append(child)
        print("child:", child)

    depth = depth + 1

    for child in node.children:
        result = recursiveDls(child, limit)
        if(result != None): 
            return result
    depth = depth - 1

# dls(root, 2)

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
