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
a = [["c" for col in range(20)] for row in range(20)]
csv = open("MazeExamples/maze_50x50.csv").read()
csv = csv.splitlines()
csv = [a.split(",") for a in csv]
csv2 = []
print(csv)
for i in csv:
    if len(i) > 1:
        csv2.append(i)

m = mazeGenerator.Maze(3,3)
print(csv2)
U = uniform.Uniform((0,0),(-1,-1), m.getMaze(), 10)
U.findPath()

G = greedy.Greedy((0,0),(-1,-1), m.getMaze(), 10)
G.findPath()


AS = astar.AStar((0,0),(-1,-1), m.getMaze(), 10)
AS.findPath()