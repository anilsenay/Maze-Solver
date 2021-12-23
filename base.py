from create_maze import createMaze
from create_tree import createTree


mazeArray, startNode = createMaze()
root = createTree(mazeArray, startNode)
print(root)