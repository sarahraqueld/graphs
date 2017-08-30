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
		print "Ordenando arestas"
		edges = {}
		for v in self:
			for a in v.get_adjacents():
				edges[v.description + "," + a.description] = v.get_weight(a)
		od = collections.OrderedDict(sorted(edges.items(),  key=lambda t: t[1], reverse = True))
		print "ARESTAS ORDENADAS:"
		print od , "----------------------------"
		return od

	def get_spanning_tree(self, size):
		print "TAMANHO DEVE SER " , size
		od = self.get_sorted_edges()
		st = Graph(False)

		while(st.get_qtd_arestas() != size and od):
			c = next(reversed(od.items()))
			print "NEXT: ", c[0][0], c[0][2], c[1]
			v = Vertex(c[0][0])
			v2 = Vertex(c[0][2])
			st.add_edge(c[0][0], c[0][2], c[1])
			
			if(st.is_cyclic()):
				print c[0][0], c[0][2]
				st.remove_edge(c[0][0], c[0][2])
				print "remove"
			a = od.popitem()
			print "pop item" , a
		#print collections.OrderedDict(sorted(spanningtree.items(),  key=lambda t: t[1]))
		return st
				


