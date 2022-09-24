from ast import Delete
from heapq import heappop, heappush
import sys
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from matplotlib import colors
import numpy as np

import copy

from specialTuple import Tup

class AStar:
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

        self.fg = []

        self.fgMtx = [list(map(self.convert,array)) for array in maze]
        #self.fgMtx[self.origin[0]][self.origin[1]] = 2
        #self.fgMtx[self.goal[0]][self.goal[1]] = 3
        self.fg.append(self.fgMtx)

        cmap = colors.ListedColormap(['black', 'white', 'blue', 'red','green','brown'])
        u = [0,1, 2, 3, 4, 5]
        bounds = np.concatenate(([0],
                         u[:-1]+np.diff(u)/2.,
                         [5]))
        norm = colors.BoundaryNorm(bounds, cmap.N)

        self.fig, self.ax = plt.subplots()
        self.mat = self.ax.imshow(self.fgMtx, cmap=cmap, norm=norm)
        #self.ax.imshow(self.fgMtx, cmap=cmap, norm=norm)

        self.ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
        self.ax.set_xticks(np.arange(-.5, self.width, 1))
        self.ax.set_yticks(np.arange(-.5, self.height, 1))


        
    def isInRange(self,cell):
        return cell[0] <= self.height and cell[0] >= 0 and cell[1] <= self.width and cell[1] >= 0
    def d(self, start, final):
        return abs(start[0] - final[0]) + abs(start[1] - final[1])
    def h(self, cell):
        return abs(cell[0] - self.goal[0]) + abs(cell[1] - self.goal[1])
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
    def convert(self, x):
        return 0 if x=="w" else 1
    def update(self,data):
        plt.gca().invert_yaxis()
        self.mat.set_data(data)
        plt.gca().invert_yaxis()
        return self.mat
    def drawPath(self, cell, fg, cameFrom):
        path = self.getPath(cameFrom, cell)
        for step in path:
            if step != None:
                fg[step[0]][step[1]] = 2
        self.fg.append(fg)
    def deltePath(self, cell, fg, cameFrom):
        path = self.getPath(cameFrom, cell)
        for step in path:
            if step != None:
                fg[step[0]][step[1]] = 3
        self.fg.append(fg)
    def findPath(self):
        iterFg = copy.deepcopy(self.fgMtx)
        cameFrom = [[ None for col in range(self.width)] for row in range(self.height)]
        g = [[ sys.maxsize for col in range(self.width)] for row in range(self.height)]
        g[self.origin[0]][self.origin[1]] = 0
        f = [[ sys.maxsize for col in range(self.width)] for row in range(self.height)]
        f[self.origin[0]][self.origin[1]] = self.h((self.origin[0],self.origin[1]))
        openSet = []

        #(f,x,y)
        heappush(openSet, Tup(f[self.origin[0]][self.origin[1]], self.origin))
        while len(openSet) > 0:
            currCell = heappop(openSet).getPair()

            iterFg = copy.deepcopy(iterFg)
            iterFg[currCell[0]][currCell[1]] = 2
            self.fg.append(iterFg)

            self.drawPath(currCell, iterFg, cameFrom)

            if currCell == self.goal:
                self.printPath(cameFrom, currCell)
                break
            neighbours = self.calculeNeighborhood(currCell)
            for neighbour in neighbours:

                prevCol = iterFg[neighbour[0]][neighbour[1]]
                iterFg = copy.deepcopy(iterFg)
                iterFg[neighbour[0]][neighbour[1]] = 5
                self.fg.append(iterFg)

                iterFg = copy.deepcopy(iterFg)
                iterFg[neighbour[0]][neighbour[1]] = prevCol
                self.fg.append(iterFg)

                preG = g[currCell[0]][currCell[1]] + self.d(currCell, neighbour)
                if preG < g[neighbour[0]][neighbour[1]]:
                    preNeighbour = Tup(f[neighbour[0]][neighbour[1]],  neighbour)
                    cameFrom[neighbour[0]][neighbour[1]] = currCell
                    g[neighbour[0]][neighbour[1]] = preG
                    f[neighbour[0]][neighbour[1]] = preG + self.h(neighbour)
                    if preNeighbour not in openSet:
                        iterFg = copy.deepcopy(iterFg)
                        iterFg[neighbour[0]][neighbour[1]] = 4
                        self.fg.append(iterFg)

                        heappush(openSet, Tup(f[neighbour[0]][neighbour[1]], neighbour))
            self.deltePath(currCell, iterFg, cameFrom)
        #print(self.fg)
        self.ax.set_yticklabels([])
        self.ax.set_xticklabels([])
        ani = animation.FuncAnimation(self.fig, self.update, self.fg, interval=10, repeat=False)
        plt.show()   