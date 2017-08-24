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
		
	def get_sorted_edges(self):
		edges = {}
		for v in self:
			for a in v.get_adjacents():
				edges[v.description + "," + a.description] = v.get_weight(a)
		od = collections.OrderedDict(sorted(edges.items(),  key=lambda t: t[1]))
		return od

	def get_spanning_tree(self, size):
		od = self.get_sorted_edges()
		spanningtree = {}
		st = Graph(False)

		while(len(spanningtree) != size):
			c = next(reversed(od.items()))
			'''
			todo: verificar se a inserção da aresta irá causar um ciclo
			st.add_edge(c[0][1], c[0][2], c[1])
			'''
			od.popitem()
			a = od.popitem()
			spanningtree[a[0]] = a[1]
		#print spanningtree
		print collections.OrderedDict(sorted(spanningtree.items(),  key=lambda t: t[1]))
		return spanningtree
				


