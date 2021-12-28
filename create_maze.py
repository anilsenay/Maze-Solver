from MazeSquare import MazeSquare
import sys

def createMaze(fileName = "maze_1"):
  try:
    file1 = open(fileName, 'r')
  except OSError:
    print ("Could not open/read maze file:", fileName)
    sys.exit()
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
