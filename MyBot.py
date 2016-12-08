from hlt import *
from networking import *

myID, gameMap = getInit()
sendInit("dpetkerPythonBot")

def create_move(location):
  site = gameMap.getSite(location)

  # See if there's an enemy adjacent to us with less strength. If so, capture it
  for d in CARDINALS:
    neighbour_site = gameMap.getSite(location, d)
    if neighbour_site.owner != myID and neighbour_site.strength < site.strength:
      return Move(location, d)

  # Don't move until we're sufficiently strong
  if site.strength < site.production * 5:
    return Move(location, STILL)

  return Move(location, NORTH if random.random() > 0.5 else WEST)

while True:
    moves = []
    gameMap = getFrame()
    for y in range(gameMap.height):
        for x in range(gameMap.width):
            location = Location(x, y)
            if gameMap.getSite(location).owner == myID:
                moves.append(create_move(location))
    sendFrame(moves)
