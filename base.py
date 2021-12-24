from create_maze import createMaze
from create_tree import createTree


mazeArray, startNode = createMaze()
root = createTree(mazeArray, startNode) 

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
        
        # print(node)
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
            

result = bfs(root)
print(result)
for i in range(len(explored)):
    print(explored[i])

# print(frontier)