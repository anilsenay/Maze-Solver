from MazeSquare import MazeSquare
import sys

# This createMaze function is used to create a mazeArray of MazeSquares
def createMaze(fileName = "maze_1"):
  try: # Open the file and read the lines
    file1 = open(fileName, 'r')
  except OSError:
    print ("Could not open/read maze file:", fileName)
    sys.exit()
  # Read lines from the file
  Lines = file1.readlines()

  # Create mazeSize variable to store the size of the maze as a array of two integers  
  mazeSize = Lines[-1].split()[0].split(",")
  mazeSize = [int(mazeSize[0]), int(mazeSize[1])]

  mazeArray = []
  startPoint = None
  goals = []
  
  # Iterate within the mazeSize and create a list of MazeSquares
  for x in range(mazeSize[0]):
    mazeRow = []
    for y in range(mazeSize[1]):
      currentSquare = Lines[x*mazeSize[1] + y] # Get the current square
      squareInfo = currentSquare.split() # Get the square info
      coordinates = squareInfo[0].split(",") # Get the coordinates
      # Create a MazeSquare object and append it to the mazeRow array
      squareObj = MazeSquare(coordinates[0], coordinates[1], squareInfo[1], squareInfo[2]) 
      mazeRow.append(squareObj)
      # Check if the square is a start point and set the startPoint variable
      if(squareInfo[2] == "START"):
        startPoint = squareObj
      # Check if the square is a goal and append it to the goals array
      if(squareInfo[2] == "GOAL"):
        goals.append(squareObj)
    
    # Append the mazeRow to the mazeArray
    mazeArray.append(mazeRow)

  return [mazeArray, startPoint, goals]

# calculateCityBlockDistance function is used to calculate the city block distance between two MazeSquares
def calculateCityBlockDistances(mazeArray, goals):
  # Iterate through the mazeArray and calculate the city block distance between the node and each goal
  for row in mazeArray:
    for node in row:
      # Create closestGoalDistance variable to store the closest goal distance
      closestGoalDistance = float("inf")
      for goal in goals:
        # Calculate the city block distance
        distance = abs(node.x - goal.x) + abs(node.y - goal.y)
        # Check if the distance is less than the closestGoalDistance and set the closestGoalDistance to the cityBlockDistance
        if(distance < closestGoalDistance):
          closestGoalDistance = distance
      node.cityBlockDistance = closestGoalDistance
