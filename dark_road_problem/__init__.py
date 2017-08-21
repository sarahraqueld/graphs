
from graph import Graph
from vertex import Vertex
import sys
from readinput import readinput
r = readinput()

qtdArestas = 0
qtdVertices = 0

g = Graph(False)

for index, elem in enumerate(r.get_input_file()):
    if(index == 0):
        qtdArestas = elem[0]
        qtdVertices = elem[1]
    else:
        v1 = g.add_vertex(Vertex(elem[0]))
        v2 = g.add_vertex(Vertex(elem[1]))
        g.add_edge(v1, v2)
