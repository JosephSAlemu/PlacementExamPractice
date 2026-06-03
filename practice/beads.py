from enum import Enum

class Direction(Enum):
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4
    UPLEFT = 5
    UPRIGHT = 6
    DOWNLEFT = 7
    DOWNRIGHT = 8

class Bead:
    def __init__(self, row, col, direction):
        self.row = row
        self.col = col
        self.direction = direction


def move(nrows, ncols, beads):
    height = nrows - 1
    width = ncols - 1
    for bead in beads:
        if bead.direction == Direction.UPLEFT:
            if bead.row == 0 and bead.col == 0:
                bead.direction = Direction.DOWNRIGHT
                bead.row +=1
                bead.col +=1
            elif bead.row == 0:
                bead.direction = Direction.DOWN
                bead.row +=1
            elif bead.col == 0:
                bead.direction = Direction.RIGHT
                bead.col +=1
            else:
                bead.row -=1
                bead.col -=1
                
        elif bead.direction == Direction.UP:
            if bead.row == 0:
                bead.direction = Direction.DOWN
                bead.row +=1
            else:
                bead.row -=1

        elif bead.direction == Direction.DOWN:
            if bead.row == height:
                bead.direction = Direction.UP
                bead.row -=1
            else:
                bead.row +=1

        elif bead.direction == Direction.LEFT:
            if bead.col == 0:
                bead.direction = Direction.RIGHT
                bead.col +=1
            else:
                bead.col -=1

        elif bead.direction == Direction.RIGHT:
            if bead.col == width:
                bead.direction = Direction.LEFT
                bead.col -=1
            else:
                bead.col +=1

        elif bead.direction == Direction.UPRIGHT:
            if bead.row == 0 and bead.col == width:
                bead.direction = Direction.DOWNLEFT
                bead.row +=1
                bead.col -=1
            elif bead.row == 0:
                bead.direction = Direction.DOWN
                bead.row +=1
            elif bead.col == width:
                bead.direction = Direction.LEFT
                bead.col -=1
            else:
                bead.row -=1
                bead.col +=1



        elif bead.direction == Direction.DOWNLEFT:
            if bead.row == height and bead.col == 0:
                bead.direction = Direction.UPRIGHT
                bead.row -=1
                bead.col +=1
            elif bead.row == height:
                bead.direction = Direction.UP
                bead.row -=1
            elif bead.col == 0:
                bead.direction = Direction.RIGHT
                bead.col +=1
            else:
                bead.row +=1
                bead.col -=1



        elif bead.direction == Direction.DOWNRIGHT:
            if bead.row == height and bead.col == width:
                bead.direction = Direction.UPLEFT
                bead.row -=1
                bead.col -=1
            elif bead.row == height:
                bead.direction = Direction.UP
                bead.row -=1
            elif bead.col == width:
                bead.direction = Direction.LEFT
                bead.col -=1
            else:
                bead.row +=1
                bead.col +=1

def collisions(beads) -> list:
    unique = [b for b in beads]
    for i in range(len(beads)):
        for j in range(i+1, len(beads)):
            if beads[i].row == beads[j].row and beads[i].col == beads[j].col:
                if beads[i] in unique:
                    unique.remove(beads[i])
                if beads[j] in unique:
                    unique.remove(beads[j])
    return unique


def beads(nrows: int, ncols: int, sr: int, sc: int, steps: int) -> int:
    """
    Simulate motion of beads within a grid, as specified in the problem statement.
    
    Bouncing off the UP wall will cause a bead to start moving downward.
    Bouncing off the bottom wall will cause a bead to start moving upward.
    Bouncing off the left wall will cause a bead to start moving right.
    Bouncing off the right wall will cause a bead to start moving left.

    Inputs:
        nrows: the number of rows in the grid
        ncols: the number of columns in the grid
        sr, sc: the starting row and column of the beads
        steps: how many time steps to simulate

    Returns (int): how many beads remain after the given number of time steps
    """

    beads = []
    beads.append(Bead(sr-1, sc-1, Direction.UPLEFT))
    beads.append(Bead(sr-1, sc, Direction.UP))
    beads.append(Bead(sr-1, sc+1, Direction.UPRIGHT))

    beads.append(Bead(sr, sc-1, Direction.LEFT))
    beads.append(Bead(sr, sc+1, Direction.RIGHT))

    beads.append(Bead(sr+1, sc-1, Direction.DOWNLEFT))
    beads.append(Bead(sr+1, sc, Direction.DOWN))
    beads.append(Bead(sr+1, sc+1, Direction.DOWNRIGHT))
    for i in range(steps):
        move(nrows, ncols, beads)
        beads = collisions(beads)

    # TODO: Implement this function.
    return len(beads)
