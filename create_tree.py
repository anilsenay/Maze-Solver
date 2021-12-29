from MazeSquare import MazeSquare

class Node:
  def __init__(self, square, cost, isGoal, children, nodeDepth, costSoFar):
    self.square = square
    self.cost = cost
    self.isGoal = isGoal
    self.children = children
    self.depth = nodeDepth
    self.costSoFar = cost + costSoFar
  
  def __str__(self) -> str:
    return 'square:{}, cost:{}, isGoal:{}, children:{}, depth:{}, costSoFar:{}\n'.format(self.square, self.cost, self.isGoal, self.children, self.depth, self.costSoFar)

COST = {
  "START": 0,
  "GOAL": 1,
  "EMPTY": 1,
  "TRAP": 10
}

mazeArray = []
stack = []
depth = -1
maxDepth = 0

def createTree(nodeList, startNode: MazeSquare):
  global mazeArray
  mazeArray = nodeList
  root = createNodeWithChilds(startNode, -1, 0)
  return [root, maxDepth]

def createNodeWithChilds(node: MazeSquare, rootDepth, costSoFar): 
  global maxDepth
  stack.append(node)
  nodeChildren = []
  nodeDepth = rootDepth + 1
  if(nodeDepth > maxDepth): maxDepth = nodeDepth
  nodeCostSoFar = costSoFar + COST[node.squareType]

  if(node.squareType == "GOAL"):
    stack.pop()
    return Node(node, COST[node.squareType], True, nodeChildren, nodeDepth, costSoFar)

  if(not(node.hasEastWall)):
    if(not(mazeArray[(node.x - 1) + 1][(node.y - 1)] in stack)):
      eastSquare = createNodeWithChilds(mazeArray[(node.x - 1) + 1][(node.y - 1)], nodeDepth, nodeCostSoFar)
      nodeChildren.append(eastSquare)
  if(not(node.hasSouthWall)):
    if(not(mazeArray[(node.x - 1)][(node.y - 1) + 1] in stack)):
      southSquare = createNodeWithChilds(mazeArray[(node.x - 1)][(node.y - 1) + 1], nodeDepth, nodeCostSoFar)
      nodeChildren.append(southSquare)
  if(not(node.hasWestWall)):
    if(not(mazeArray[(node.x - 1) - 1][(node.y - 1)] in stack)):
      westSquare = createNodeWithChilds(mazeArray[(node.x - 1) - 1][(node.y - 1)], nodeDepth, nodeCostSoFar)
      nodeChildren.append(westSquare)    
  if(not(node.hasNorthWall)):
    if(not(mazeArray[(node.x - 1)][(node.y - 1) - 1] in stack)):
      northSquare = createNodeWithChilds(mazeArray[(node.x - 1)][(node.y - 1) - 1], nodeDepth, nodeCostSoFar)
      nodeChildren.append(northSquare)
  stack.pop()
  return Node(node, COST[node.squareType], False, nodeChildren, nodeDepth, costSoFar)