import sys

sys.path.insert(0, '/home/sarahraqueld/graphs/graph_structure')

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

	

	def is_cyclic_visit(self, vertex):
		print "Visited vertex: " , vertex.description
		vertex.color = 'gray'

		for adj in vertex.get_adjacents():
			if (adj.color == 'gray' and adj != vertex.parent):
				return True
			if (adj.color == 'white'):
				adj.parent = vertex
				if(self.is_cyclic_visit(adj)):
					return True
		vertex.color = 'black'
		return False


	def is_cyclic(self):
		for v in self.vertices.values():
			if(v.color == 'white'):
				if(self.is_cyclic_visit(v)):
					return True

		return False


	def get_spanning_tree(self, size):
		od = self.get_sorted_edges()
		spanningtree = {}
		st = Graph(False)

		while(len(spanningtree) != size and od):
			c = next(reversed(od.items()))
			v = Vertex(c[0][0])
			v2 = Vertex(c[0][2])
			st.add_edge(c[0][0], c[0][2], c[1])
			print c[0][0], c[0][2], c[1]
			if(st.is_cyclic()):
				print "IS CYCLIC"
				print c[0][0], c[0][2]
				st.remove_edge(c[0][0], c[0][2])
			else:
				print "IS NOT"

			od.popitem()
			a = od.popitem()
			spanningtree[a[0]] = a[1]
		#print spanningtree
		#print collections.OrderedDict(sorted(spanningtree.items(),  key=lambda t: t[1]))
		return st
				


