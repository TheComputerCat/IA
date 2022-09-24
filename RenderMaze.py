from matplotlib import colors
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import copy

class RenderMaze:
    def __init__(self,maze, interval, cellColors):
        self.inverval = interval
        self.frames = []
        self.maze = [list(map(self.convert,array)) for array in maze]

        self.frames.append(self.maze)

        cmap = colors.ListedColormap(cellColors)
        u = list(range(len(cellColors)))
        bounds = np.concatenate(([min(u)],
                         u[:-1]+np.diff(u)/2.,
                         [max(u)]))
        norm = colors.BoundaryNorm(bounds, cmap.N)

        self.fig, self.ax = plt.subplots()
        self.mat = self.ax.imshow(self.maze, cmap=cmap, norm=norm)

        self.ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
        self.ax.set_xticks(np.arange(-.5, len(self.maze[0]), 1))
        self.ax.set_yticks(np.arange(-.5, len(self.maze), 1))

        self.ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
        self.ax.set_xticks(np.arange(-.5, len(self.maze[0]), 1))
        self.ax.set_yticks(np.arange(-.5, len(self.maze), 1))
    def convert(self, x):
        return 0 if x=="w" else 1
    def update(self,data):
        plt.gca().invert_yaxis()
        self.mat.set_data(data)
        plt.gca().invert_yaxis()
        return self.mat
    def drawPath(self, path):
        frame = self.getLastFrame()
        for step in path:
            if step != None:
                frame[step[0]][step[1]] = 2
        self.frames.append(frame)
    def deltePath(self, path):
        frame = self.getLastFrame()
        for step in path:
            if step != None:
                frame[step[0]][step[1]] = 3
        self.frames.append(frame)
    def addFrame(self, alteredCell, color):
        copyFrame = copy.deepcopy(self.frames[-1])
        copyFrame[alteredCell[0]][alteredCell[1]] = color
        self.frames.append(copyFrame)
    def getLastFrame(self):
        return self.frames[-1]
    def render(self):
        self.ax.set_yticklabels([])
        self.ax.set_xticklabels([])
        ani = animation.FuncAnimation(self.fig, self.update, self.frames, interval=self.inverval, repeat=False)
        plt.show()   


