import sys
class Prims():
    def __init__(self, vertices, graphMtx):
        self.vertices = vertices
        self.graphMtx = graphMtx
    def minVertexInCutSet(self, minEdgeWgtInCutSet, mstSet): 
        min = sys.maxsize
        minIndex =  None
        for v in range(self.vertices):
            if minEdgeWgtInCutSet[v] < min and mstSet[v] == False:
                min = minEdgeWgtInCutSet[v]
                minIndex = v
        return minIndex
    def primsMST(self):
        # minEdgeWgtInCutSet saves the min edge weight that connects a
        # edge not in the mstSet to this, this in order no keep track
        # of the edges in the cut set and easily select the min
        minEdgeWgtInCutSet = [sys.maxsize] * self.vertices
        mstSet = [False] * self.vertices
        parent = [None] * self.vertices
        # initiali the only vertex in the mstSet is the origin
        minEdgeWgtInCutSet[0] = 0
        parent[0] = -1

        for vertex in range(self.vertices):
            # selects the vertex with  the min weight that is in the cut
            minVtxInCut = self.minVertexInCutSet(minEdgeWgtInCutSet, mstSet)
            # add selected vertex to mstSet
            mstSet[minVtxInCut] = True


            for neighbor in range(self.vertices):
                # update the edge that conects each vertex of the neigbor to the mstSet
                if (self.graphMtx[minVtxInCut][neighbor] > 0 and mstSet[neighbor] == False 
                    and self.graphMtx[minVtxInCut][neighbor] < minEdgeWgtInCutSet[neighbor]):
                    minEdgeWgtInCutSet[neighbor] = self.graphMtx[minVtxInCut][neighbor]
                    parent[neighbor] = minVtxInCut

        return {"parent": parent, "graphMtx": self.graphMtx}
p = Prims(5, [[0, 2, 0, 6, 0],
               [2, 0, 3, 8, 5],
               [0, 3, 0, 0, 7],
               [6, 8, 0, 0, 9],
               [0, 5, 7, 9, 0]])
print(p.primsMST())