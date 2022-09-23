from numpy import random
class Maze():
    def __init__(self, rows, cols):
        self.rows = 2*rows - 1
        self.cols= 2*cols - 1
        self.maze = [["w" for col in range(self.cols)] for row in range(self.rows)]
        self.primsMaze()
    def calculeNeighborhood(self, cell):
        neighbours = []
        row, col = cell[0], cell[1]
        if row - 2 >= 0:
            neighbours.append((row - 2,col))
        if row + 2 < self.rows:
            neighbours.append((row + 2,col))
        if col - 2 >= 0:
            neighbours.append((row, col - 2))
        if col + 2 < self.cols:
            neighbours.append((row, col + 2))
        pathNeighbours = []
        for neighbour in neighbours:
            if self.maze[neighbour[0]][neighbour[1]] == "c":
                pathNeighbours.append(neighbour)
        return pathNeighbours  
    def makePassage(self, currCell, newCell):
        diffRow, diffCol = newCell[0] - currCell[0], newCell[1] - currCell[1]
        if diffRow == 0 and diffCol > 0:
            self.maze[currCell[0]][currCell[1] + 1] = "c"
        if diffRow == 0 and diffCol < 0:
            self.maze[currCell[0]][currCell[1] - 1] = "c"
        if diffRow > 0 and diffCol == 0:
            self.maze[currCell[0] + 1][currCell[1]] = "c"
        if diffRow < 0 and diffCol == 0:
            self.maze[currCell[0] - 1][currCell[1]] = "c"       
    def recalculeFrontier(self, cell, frontier):
        neighbours = []
        row, col = cell[0], cell[1]
        if row - 2 >= 0:
            neighbours.append((row - 2,col))
        if row + 2 < self.rows:
            neighbours.append((row + 2,col))
        if col - 2 >= 0:
            neighbours.append((row, col - 2))
        if col + 2 < self.cols:
            neighbours.append((row, col + 2))
        for cell in neighbours:
            if len(self.calculeNeighborhood(cell)) == 0:
                frontier.append(cell)
        return frontier
    def printMaze(self):
        for i in range(self.rows):
            for j in range(self.cols):
                print(self.maze[i][j], end = "  ")
            print("\n")
    def getMaze(self):
        return self.maze
    def primsMaze(self):
        currCell = (0,0)
        self.maze[0][0] = "c"
        frontier=[(0,2), (2,0)]
        while len(frontier) > 0:
            currCellInx = random.randint(len(frontier))
            currCell = frontier[currCellInx]
            neighbours =  self.calculeNeighborhood(currCell)
            neighbour = neighbours[random.randint(len(neighbours))]
            frontier = self.recalculeFrontier(currCell, frontier)
            self.maze[currCell[0]][currCell[1]] = "c"
            self.makePassage(currCell, neighbour)
            frontier.pop(currCellInx)
#p=Maze(5,5)
#p.printMaze()
#print(p.getMaze())