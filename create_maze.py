from MazeSquare import MazeSquare

def createMaze():
  file1 = open('maze_1', 'r')
  Lines = file1.readlines()

  mazeSize = Lines[-1].split()[0].split(",")
  mazeSize = [int(mazeSize[0]), int(mazeSize[1])]

  mazeArray = []
  startPoint = None
  goals = []

  for x in range(mazeSize[0]):
    mazeRow = []
    for y in range(mazeSize[1]):
      currentSquare = Lines[x*mazeSize[1] + y]
      squareInfo = currentSquare.split()
      coordinates = squareInfo[0].split(",")
      squareObj = MazeSquare(coordinates[0], coordinates[1], squareInfo[1], squareInfo[2])
      mazeRow.append(squareObj)
      if(squareInfo[2] == "START"):
        startPoint = squareObj
      if(squareInfo[2] == "GOAL"):
        goals.append(squareObj)

    mazeArray.append(mazeRow)

  return [mazeArray, startPoint, goals]

def calculateCityBlockDistances(mazeArray, goals):
  for row in mazeArray:
    for node in row:
      closestGoalDistance = float("inf")
      for goal in goals:
        distance = abs(node.x - goal.x) + abs(node.y - goal.y)
        if(distance < closestGoalDistance):
          closestGoalDistance = distance
      node.cityBlockDistance = closestGoalDistance
