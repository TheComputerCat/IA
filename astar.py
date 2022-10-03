from heapq import heappop, heappush
import random
import sys
from specialTuple import Tup
from RenderMaze import RenderMaze
import graphviz

class AStar:
    def __init__(self, origin, goal, maze, interval = 100):
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
        self.graph=True if self.height<=10 and self.width<=10 else False
        if self.graph:
            self.f = graphviz.Digraph('a', format='png')
            self.f.attr(bgcolor='#282C34')
            self.f.attr('node',fontcolor='#F9F9F9')
            self.f.attr('node',color='#F9F9F9')
            self.f.attr('edge',color='#F9F9F9')
            self.f.attr('edge',fontcolor='#F9F9F9')
        self.render = RenderMaze(maze, interval, ['black', 'white', 'blue', 'red', 'green','brown'])
    
    def isInRange(self,cell):
        return cell[0] <= self.height and cell[0] >= 0 and cell[1] <= self.width and cell[1] >= 0
    def d(self, start, final):
        return abs(start[0] - final[0]) + abs(start[1] - final[1])
    def h(self, cell):
        return abs(cell[0] - self.goal[0]) + abs(cell[1] - self.goal[1])
    def calculeNeighborhood(self, cell):
        neighbours = []
        row, col = cell[0], cell[1]
        if col - 1 >= 0:
            neighbours.append((row, col - 1))
        if col + 1 < self.width:
            neighbours.append((row, col + 1))
        if row - 1 >= 0:
            neighbours.append((row - 1,col))
        if row + 1 < self.height:
            neighbours.append((row + 1,col))
        pathNeighbours = []
        for neighbour in neighbours:
            if self.maze[neighbour[0]][neighbour[1]] == "c":
                pathNeighbours.append(neighbour)
        random.shuffle(pathNeighbours)
        return pathNeighbours
    def getPath(self, cameFrom, current):
        path = [current]
        while current!= None:
            current = cameFrom[current[0]][current[1]]
            path.append(current)
        return path
    def printPath(self, cameFrom, current):
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
    def calculeDirection(self, curr, prev):
        if curr[0] - prev[0] > 0:
            return "u"
        if curr[0] - prev[0] < 0:
            return "d"
        if curr[1] - prev[1] > 0:
            return "r"
        if curr[1] - prev[1] < 0:
            return "l" 
    def findPath(self):
        cameFrom = [[ None for col in range(self.width)] for row in range(self.height)]
        g = [[ sys.maxsize for col in range(self.width)] for row in range(self.height)]
        g[self.origin[0]][self.origin[1]] = 0
        f = [[ sys.maxsize for col in range(self.width)] for row in range(self.height)]
        f[self.origin[0]][self.origin[1]] = self.h((self.origin[0],self.origin[1]))
        openSet = []
        #(f,x,y)
        heappush(openSet, Tup(f[self.origin[0]][self.origin[1]], self.origin))
        self.f.node('00', 'Origin')
        while len(openSet) > 0:
            currCell = heappop(openSet).getPair()
            
            self.render.addFrame(currCell, 2)
            self.render.drawPath(path = self.getPath(cameFrom, currCell))
                            
            if currCell == self.goal:
                self.printPath(cameFrom, currCell)
                break
            neighbours = self.calculeNeighborhood(currCell)
            for neighbour in neighbours:
                prevCol = self.render.getLastFrame()[neighbour[0]][neighbour[1]]

                self.render.addFrame(neighbour, 5)
                self.render.addFrame(neighbour, prevCol)

                preG = g[currCell[0]][currCell[1]] + self.d(currCell, neighbour)
                if preG < g[neighbour[0]][neighbour[1]]:
                    preNeighbour = Tup(f[neighbour[0]][neighbour[1]],  neighbour)
                    cameFrom[neighbour[0]][neighbour[1]] = currCell
                    g[neighbour[0]][neighbour[1]] = preG
                    f[neighbour[0]][neighbour[1]] = preG + self.h(neighbour)
                    if preNeighbour not in openSet:
                        self.render.addFrame(neighbour, 4)
                        if self.graph:
                            move = self.calculeDirection(currCell, neighbour)
                            if neighbour == self.goal:
                                self.f.attr('node', shape='doublecircle')
                            self.f.node(f'{neighbour[0]}{neighbour[1]}', f'x:{neighbour[0]}y:{neighbour[1]}' + "\nPeso: \n" + str(f[currCell[0]][currCell[1]]))
                            self.f.edge(f'{currCell[0]}{currCell[1]}', f'{neighbour[0]}{neighbour[1]}', label=move)
                        heappush(openSet, Tup(f[neighbour[0]][neighbour[1]], neighbour))
            self.render.deltePath(self.getPath(cameFrom, currCell))
            if self.graph:
                self.f.render().replace('\\', '/')
        self.render.render()  