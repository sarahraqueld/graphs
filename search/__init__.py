
import graph
import vertex


v1 = vertex.Vertex(1)
v2 = vertex.Vertex(2)
v1.add_adjacent(v2)
v2.add_adjacent(v1)

g = graph.Graph([v1, v2], True)
g.print_vertices()
g.removeVertex(v1)
g.print_vertices()
