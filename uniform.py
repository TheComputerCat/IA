from heapq import heappop, heappush
import sys
class Uniform:
    def __init__(self, origin, goal, maze):
        self.maze = maze
        self.height = len(self.maze)
        self.width = len(self.maze[0])
        if self.isInRange(goal):
            self.goal = goal
        else:
            self.goal = (self.height - 1, self.width - 1)
        if self.isInRange(origin):
            self.origin = origin
        else:
            self.origin = (0, 0)
    def isInRange(self,cell):
        return cell[0] <= self.height and cell[0] >= 0 and cell[1] <= self.width and cell[1] >= 0
    def d(self, start, final):
        return abs(start[0] - final[0]) + abs(start[1] - final[1])
    def calculeNeighborhood(self, cell):
        neighbours = []
        row, col = cell[0], cell[1]
        if row - 1 >= 0:
            neighbours.append((row - 1,col))
        if row + 1 < self.height:
            neighbours.append((row + 1,col))
        if col - 1 >= 0:
            neighbours.append((row, col - 1))
        if col + 1 < self.width:
            neighbours.append((row, col + 1))
        pathNeighbours = []
        for neighbour in neighbours:
            if self.maze[neighbour[0]][neighbour[1]] == "c":
                pathNeighbours.append(neighbour)
        return pathNeighbours  
    def getPath(self, cameFrom, current):
        path = [current]
        while current!= None:
            current = cameFrom[current[0]][current[1]]
            path.append(current)
        print(path)
    def printMaze(self):
        for i in range(self.height):
            for j in range(self.width):
                print(self.maze[i][j], end = "  ")
            print("\n")
    def findPath(self):
        cameFrom = [[ None for col in range(self.width)] for row in range(self.height)]
        g = [[ sys.maxsize for col in range(self.width)] for row in range(self.height)]
        g[self.origin[0]][self.origin[1]] = 0
        openSet = []
        #(f,x,y)
        heappush(openSet, (g[self.origin[0]][self.origin[1]],) + self.origin)
        while len(openSet) > 0:
            currCell = heappop(openSet)[1:3]
            if currCell == self.goal:
                self.getPath(cameFrom, currCell)
            neighbours = self.calculeNeighborhood(currCell)
            for neighbour in neighbours:
                preG = g[currCell[0]][currCell[1]] + self.d(currCell, neighbour)
                if preG < g[neighbour[0]][neighbour[1]]:
                    preNeighbour = (g[neighbour[0]][neighbour[1]],) + neighbour
                    cameFrom[neighbour[0]][neighbour[1]] = currCell
                    g[neighbour[0]][neighbour[1]] = preG
                    if preNeighbour not in openSet:
                        heappush(openSet, (g[neighbour[0]][neighbour[1]],) + neighbour)
