
import graph
import vertex


v1 = vertex.Vertex('1')
v2 = vertex.Vertex('2')
v3 = vertex.Vertex('3')
v4 = vertex.Vertex('4')
g = graph.Graph([v1, v2, v3, v4], True)

g.add_edge(v1, v2)
#g.add_edge(v2, v1)
g.add_edge(v2, v3)
#g.add_edge(v3, v2)
g.add_edge(v2, v4)
#g.add_edge(v4, v2)


if (g.is_connected()):
    print 'is connected'
# g.dfs()
#g.bfs()
#g.print_vertices()
#g.remove_vertex(v1)
#g.print_vertices()
