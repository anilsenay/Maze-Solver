class MazeSquare:
  def __init__(self, x, y, walls, squareType):
    self.x = int(x)
    self.y = int(y)
    self.squareType = squareType
    self.hasNorthWall = walls.find("N") != -1
    self.hasSouthWall = walls.find("S") != -1
    self.hasEastWall = walls.find("E") != -1
    self.hasWestWall = walls.find("W") != -1
  
  def __str__(self) -> str:
    return 'x:{}, y:{}, type:{}, NorthWall:{}, EastWall:{}, SouthWall:{}, WestWall:{}\n'.format(self.x, self.y, self.squareType, self.hasNorthWall,self.hasEastWall, self.hasSouthWall, self.hasWestWall)
