import sys

sys.path.insert(0, 'C:\Users\sarahferreira\projects\graphs\graph_structure')

from graph import AbstractGraph
from graph import AbstractVertex
import collections




class Vertex(AbstractVertex):
	def __init__(self, description):
		self.visited = False
		self.distance = sys.maxint       
		self.parent = None  
		AbstractVertex.__init__(self, description)
		


class Graph(AbstractGraph):
	def __init__(self, directed):
		AbstractGraph.__init__(self, directed)
		
	def get_spanning_tree(self, size):
		edges = {}
		for v in self:
			for a in v.get_adjacents():
				edges[v.description + "," + a.description] = v.get_weight(a)
				print '( %s)'  % (v.get_weight(a))
		od = collections.OrderedDict(sorted(edges.items(),  key=lambda t: t[1]))

		spanningtree = {}

		while(len(spanningtree) != size):
			 od.popitem()
			 a = od.popitem()
			 spanningtree[a[0]] = a[1]
		#print spanningtree
		print collections.OrderedDict(sorted(spanningtree.items(),  key=lambda t: t[1]))
		return spanningtree
				


