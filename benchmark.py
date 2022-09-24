import astar
import uniform
import mazeGenerator
a=[
["c",	"c",	"c",	"c",	"c"],
				
["c",	"c",	"c",	"w",	"c"],
				
["c",	"c",	"c",	"w",	"c"],
				
["c",	"w",	"w",	"w",	"c"],
				
["c",	"c",	"c",	"c",	"c"]]

m = mazeGenerator.Maze(21,21)
AS = astar.AStar((0,0),(-1,-1), a)
AS.findPath()
#U = uniform.Uniform((0,0),(-1,-1), a)
#U.findPath()
#m.printMaze()
#print(a)