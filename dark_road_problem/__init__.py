import sys
sys.path.append('/home/sarahraqueld/graphs/graph_structure')


from graph import AbstractGraph
from graph import AbstractVertex
from readinput import readinput
r = readinput()

g = AbstractGraph(False)



for index, elem in enumerate(r.get_input_file()):
    if(index == 0 or (elem[0] == '0' and elem[1] == '0')):
    	pass
    else:
        v1 = g.add_vertex(elem[0])
        v2 = g.add_vertex(elem[1])
        g.add_edge(elem[0], elem[1], int(elem[2]))

for v in g:
    for w in v.get_adjacents():
        vid = v.description
        wid = w.description
        print '( %s , %s, %3d)'  % ( vid, wid, v.get_weight(w))

for v in g:
    print 'Vertices: %s %s ' %(v.description, g.vertices[v.get_description()])
