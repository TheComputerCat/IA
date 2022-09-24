from calendar import c
import heapq as hq
class Tup:
    def __init__(self, a, tuple):
        self.a = a
        self.b = tuple[0]
        self.c = tuple[1]
    def print(self):
        print(self.a, self.b, self.c)
    def getVal(self):
        return self.a
    def getPair(self):
        return (self.b, self.c)
    def __lt__(self, nxt):
        return self.a < nxt.a