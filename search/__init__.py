
import graph
import vertex
import sys



v1 = vertex.Vertex('1')
v2 = vertex.Vertex('2')
v3 = vertex.Vertex('3')
v4 = vertex.Vertex('4')
g = graph.Graph([v1, v2, v3, v4], False)

g.add_edge(v1, v2)
#g.add_edge(v2, v1)
g.add_edge(v2, v3)
#g.add_edge(v3, v2)
g.add_edge(v2, v4)
#g.add_edge(v4, v2)

if(sys.argv[1] == '-bfs'):
    g.bfs()
elif(sys.argv[1] == '-dfs'):
    g.dfs()
elif(sys.argv[1] == '-c'):
    g.is_connected()
else:
    print 'Invalid args. Try: -bfs for breadth-first search, -dfs for depth first search, of -c to know if the graph is connected'
