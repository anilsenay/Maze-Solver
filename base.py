from create_maze import createMaze
from create_tree import createTree


mazeArray, startNode = createMaze()
root = createTree(mazeArray, startNode) 

def bfs(root):
    frontier = []
    explored = []
    cost = 0
    frontier.append(root)
    i = 0
    while True:
        if (len(frontier) == 0):
            return "Error! Frontier is empty."
        node = frontier.pop(0)
        
        # print(node)
        explored.append(node.square)
        cost = cost + node.cost
        for child in node.children:
            if (child.isGoal):
                
                print(child)
                cost = cost + child.cost
                return cost
            if (child.square in explored):
                continue
            frontier.append(child)
            
        i = i + 1

result = bfs(root)
# print(result)