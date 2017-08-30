import sys
from readinput import readinput
from spanningTree import Graph
from spanningTree import Vertex

r = readinput()

g = Graph(False)

vertices_number= 0

for index, elem in enumerate(r.get_input_file()):
    if(index == 0):
    	vertices_number = int(elem[0])
    elif(elem[0] == '0' and elem[1] == '0'):
        pass
    else:
        v1 = g.add_vertex(elem[0])
        v2 = g.add_vertex(elem[1])
        g.add_edge(elem[0], elem[1], int(elem[2]))

   

print "Spanning tree deve ter " , (vertices_number - 1)*2, " arestas"
st = g.get_spanning_tree((vertices_number-1)*2)

for v in st:
    for w in v.get_adjacents():
        vid = v.description
        wid = w.description
        print '( %s , %s, %3d)'  % ( vid, wid, v.get_weight(w))

print "quantidade economizada::::::::::::"
print g.get_weight() - st.get_weight()
