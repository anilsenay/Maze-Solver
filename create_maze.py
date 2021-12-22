from MazeSquare import MazeSquare

file1 = open('maze_1', 'r')
Lines = file1.readlines()

mazeSize = Lines[-1].split()[0].split(",")
mazeSize = [int(mazeSize[0]), int(mazeSize[1])]

mazeArray = []

for x in range(mazeSize[0]):
  mazeRow = []
  for y in range(mazeSize[1]):
    currentSquare = Lines[x*mazeSize[1] + y]
    squareInfo = currentSquare.split()
    coordinates = squareInfo[0].split(",")
    mazeRow.append(MazeSquare(coordinates[0], coordinates[1], squareInfo[1], squareInfo[2]))
  mazeArray.append(mazeRow)

for x in range(mazeSize[0]):
  for y in range(mazeSize[1]):
    print(mazeArray[x][y])