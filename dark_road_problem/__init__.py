
from graph import Graph
from vertex import Vertex
import sys
from readinput import readinput
r = readinput()

g = Graph(False)

for index, elem in enumerate(r.get_input_file()):
    if(index == 0 or (elem[0] == '0' and elem[1] == '0')):
    	pass
    else:
        v1 = g.add_vertex(Vertex(elem[0]))
        v2 = g.add_vertex(Vertex(elem[1]))
        g.add_edge(v1, v2, elem[2])

print g