from create_maze import calculateCityBlockDistances, createMaze
from create_tree import createTree

# Global variables for the search algorithm
frontier, frontierSize, maxFrontierSize = ([], 0, 0)
explored = []
expanded = []
numberOfExpanded = 0
depth = 0

# pushToFrontier function simply pushes a node to the frontier.
def pushToFrontier(node):
    global maxFrontierSize, frontierSize
    # Increase the size of the frontier by 1
    frontierSize = frontierSize + 1
    # Push the node to the frontier
    frontier.append(node)
    # Update the maximum size of the frontier if necessary
    if(frontierSize > maxFrontierSize): maxFrontierSize = frontierSize

# popFromFrontier function pops a node from the frontier. It also updates the size of the frontier.
def popFromFrontier(location = -1):
    global frontierSize
    # Decrease the size of the frontier by 1
    frontierSize = frontierSize - 1
    # pop the node from the frontier based on the location
    return frontier.pop(location)

## GENERAL SEARCH ##
def generalSearch(root, strategy, limit = None):
    global frontier, explored, numberOfExpanded
    frontier = []
    explored = []
    pushToFrontier(root)
    
    # While the frontier is not empty
    while True:
        if (len(frontier) == 0):
            return None
        # Get the next node to expand from the frontier based on the strategy
        node = strategy()
        if(node == None):
            return None

        if(node.square not in explored):
            explored.append(node.square)
        else: continue
        expanded.append(node)
        numberOfExpanded = numberOfExpanded + 1
        
        # If a node is a goal node, return the node.
        if node.isGoal:
            return node
        
        if(limit != None and node.depth + 1 > limit): continue
        
        # Traverse the children of the node and push them to the frontier
        for child in node.children:
            pushToFrontier(child)

## BFS STRATEGY ##
# It simply pops the first node from the frontier.
def bfsStrategy():
    return popFromFrontier(0)

## DFS STRATEGY ##
# It finds first node of last pushed nodes in frontier and pops it
# For example, if 3 nodes pushed at last time, it pops first of those
# because we push children according to their priorities
def dfsStrategy():
    index = -1
    while (frontierSize > abs(index) and frontier[-1].depth == frontier[index-1].depth):
        index = index - 1
    return popFromFrontier(index)

## UCS STRATEGY ##
# It pops the node with the lowest costSoFar variable from the frontier.
def ucsStrategy():
    frontier.sort(key = lambda x: x.costSoFar) 
    return popFromFrontier(0)

## GREEDY BEST FIRST STRATEGY ##
# It pops the node with the lowest cityBlockDistance variable from the frontier.
def greedyStrategy():
    frontier.sort(key = lambda x: x.square.cityBlockDistance)
    return popFromFrontier(0)

## A* STRATEGY ##
# It calculates the sum of the city block distances of the node and costSoFar 
# variable and pop the node with lowest calculated value from the frontier.
def aStarStrategy():
    frontier.sort(key = lambda x: x.square.cityBlockDistance + x.costSoFar)
    return popFromFrontier(0)

## To find solution we trace expanded list in reverse order
## First we start from last index which has goal state
## And trace backward to find the node has goal state as child
## Then for each node we are looking for its parent
## Finally we have the solution path
def findSolution():
    index = -1 ## Start index as -1 which is goal state's index
    lastIndex = -len(expanded) ## Get first element's index of array from backward 
    solutionPath = [expanded[index]]
    cost = expanded[index].cost ## We also find cost of the solution path
    while(index >= lastIndex):
        if(solutionPath[0] in expanded[index].children):
            solutionPath.insert(0, expanded[index])
            cost = cost + expanded[index].cost
        index = index - 1
    
    ## After getting solution path, we create a solution path string in format
    solutionPathString = ""
    for node in solutionPath:
        solutionPathString = solutionPathString + "(" + str(node.square.x) + "," + str(node.square.y) + ") - "
    solutionPathString = solutionPathString[:-2] ## Remove last two character which is "- "
    return [cost, solutionPathString]

# Main function
def main():
    print("Welcome to Maze Solver")
    # Ask the user for the size of the maze
    mazeName = input("Please enter the maze file [maze_1]: ") or "maze_1"
    
    # Craete mazeArray, startNode, and goals array based on the mazeName.
    mazeArray, startNode, goals = createMaze(mazeName)
    # Create the tree with its root and maxDepth variables based on the mazeArray and startNode
    root, maxDepth = createTree(mazeArray, startNode) 
    
    # Ask the user for the search strategy
    selection = askStrategy()
    
    # Based on the selection, call the general search function with the appropriate strategy
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
    
    # Print the results
    printResults()

# Display the menu and ask the user for the search strategy
def askStrategy():
    print("Please select a search strategie")
    print("1 - Depth First Search")
    print("2 - Breadth First Search")
    print("3 - Iterative Deepening")
    print("4 - Uniform Cost Search")
    print("5 - Greedy Best First Search")
    print("6 - A* Heuristic Search")
    
    selection = int(input("Type your selection number: "))
    # If the user enters a number outside of the range, ask again
    while(not(selection == 1 or selection == 2 or selection == 3 or selection == 4 or selection == 5 or selection == 6)):
        print("Please type a valid number\n")
        selection = askStrategy()
    return selection

## PRINT RESULTS ##
# Print the results of the search strategy
def printResults():
    cost, solutionPath = findSolution()
    print("\nThe cost of the solution found: " + str(cost))
    print("Number of expanded nodes: " +  str(numberOfExpanded))
    print("The maximum size of the frontier: " + str(maxFrontierSize))
    print("The maximum size of the explored set during the search: " + str(len(explored)))
    print("Solution Path: " + str(solutionPath))
    
main()