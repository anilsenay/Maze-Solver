from MazeSquare import MazeSquare

class Node:
  def __init__(self, cost, isGoal, children):
    self.cost = cost
    self.isGoal = isGoal
    self.children = children
  
  def __str__(self) -> str:
    return 'cost:{}, isGoal:{}, children:{}\n'.format(self.cost, self.isGoal, self.children)

COST = {
  "START": 0,
  "GOAL": 1,
  "EMPTY": 1,
  "TRAP": 10
}

mazeArray = []
stack = []

def createTree(nodeList, startNode: MazeSquare):
  global mazeArray
  mazeArray = nodeList
  root = createNodeWithChilds(startNode)
  print(root)
  return root

def createNodeWithChilds(node: MazeSquare):
  print(node)
  stack.append(node)
  nodeChildren = []

  if(node.squareType == "GOAL"):
    stack.pop()
    return Node(COST[node.squareType], False, nodeChildren)

  if(not(node.hasEastWall)):
    if(not(mazeArray[(node.x - 1)][(node.y - 1) + 1] in stack)):
      eastSquare = createNodeWithChilds(mazeArray[(node.x - 1)][(node.y - 1) + 1])
      nodeChildren.append(eastSquare)
  if(not(node.hasSouthWall)):
    if(not(mazeArray[(node.x - 1) + 1][(node.y - 1)] in stack)):
      southSquare = createNodeWithChilds(mazeArray[(node.x - 1) + 1][(node.y - 1)])
      nodeChildren.append(southSquare)
  if(not(node.hasWestWall)):
    if(not(mazeArray[(node.x - 1)][(node.y - 1) - 1] in stack)):
      westSquare = createNodeWithChilds(mazeArray[(node.x - 1)][(node.y - 1) - 1])
      nodeChildren.append(westSquare)    
  if(not(node.hasNorthWall)):
    if(not(mazeArray[(node.x - 1) - 1][(node.y - 1)] in stack)):
      northSquare = createNodeWithChilds(mazeArray[(node.x - 1) - 1][(node.y - 1)])
      nodeChildren.append(northSquare)
  stack.pop()
  return Node(COST[node.squareType], False, nodeChildren)