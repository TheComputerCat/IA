import astar
import uniform
import mazeGenerator
import greedy
a=[
["c",	"c",	"c",	"c",	"c"],
				
["c",	"c",	"c",	"w",	"c"],
				
["c",	"c",	"c",	"w",	"c"],
				
["c",	"w",	"w",	"w",	"c"],
				
["c",	"c",	"c",	"c",	"c"]]

m = mazeGenerator.Maze(21,21)

U = uniform.Uniform((0,0),(-1,-1), m.getMaze(), 10)
U.findPath()

G = greedy.Greedy((0,0),(-1,-1), m.getMaze(), 10)
G.findPath()

AS = astar.AStar((0,0),(-1,-1), m.getMaze(), 10)
AS.findPath()