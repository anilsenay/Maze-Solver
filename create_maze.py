from MazeSquare import MazeSquare
from create_tree import createTree

def createMaze():
  file1 = open('maze_1', 'r')
  Lines = file1.readlines()

  mazeSize = Lines[-1].split()[0].split(",")
  mazeSize = [int(mazeSize[0]), int(mazeSize[1])]

  mazeArray = []
  startPoint = None

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

    mazeArray.append(mazeRow)

  return [mazeArray, startPoint]