#!/usr/bin/env python
# -*- coding: utf-8 -*-

class AbstractVertex:
    def __init__(self, description):
        self.__adjacents = {}
        self.__parent = None
        self.__description = description
    
    def add_adjacent(self, adjacent, weight=0):
        self.__adjacents[adjacent] = weight

    def __str__(self):
        retorno = self.__description + ' with adjacents: '
        for a in self.__adjacents:
             retorno += a.__description
        return retorno

    def get_weight(self, adjacent):
        return self.__adjacents[adjacent]

    def get_description(self):
        return self.__description

    def get_adjacents(self):
        return self.__adjacents.keys()

    ###### Properties #####
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, d):
        self.__description = d
    
    @property
    def adjacents(self):
        return self.__adjacents

class AbstractGraph:
    def __init__(self, directed):
        if( not isinstance(directed, bool)):
            raise Exception('Problem with args')
        self.vertices = {}
        self.__directed = directed

    def add_vertex(self, description):
	if description in self.vertices:
		return self.vertices[description]
        vertex = AbstractVertex(description)
        self.vertices[description] = vertex
        return vertex

    def __iter__(self):
        return iter(self.vertices.values())

    def add_edge(self, origin, destination, weight):
        if origin not in self.vertices:
            self.add_vertex(origin)
        if destination not in self.vertices:
            self.add_vertex(destination)
        self.vertices[origin].add_adjacent(self.vertices[destination], weight)
        if(not self.__directed):
            self.vertices[destination].add_adjacent(self.vertices[origin], weight)

    def get_vertices(self):
        return self.vertices.keys()

    # Properties #

    @property
    def directed(self):
        return self.__directed

if __name__ == '__main__':

    g = Graph(False)

    g.add_vertex('a')
    g.add_vertex('b')
    g.add_vertex('c')
    g.add_vertex('d')
    g.add_vertex('e')
    g.add_vertex('f')

    g.add_edge('a', 'b', 7)  
    g.add_edge('a', 'c', 9)
    g.add_edge('a', 'f', 14)
    g.add_edge('b', 'c', 10)
    g.add_edge('b', 'd', 15)
    g.add_edge('c', 'd', 11)
    g.add_edge('c', 'f', 2)
    g.add_edge('d', 'e', 6)
    g.add_edge('e', 'f', 9)

    for v in g:
        for w in v.get_adjacents():
            vid = v.description
            wid = w.description
            print '( %s , %s, %3d)'  % ( vid, wid, v.get_weight(w))

    for v in g:
        print 'Vertices: %s %s ' %(v.description, g.vertices[v.get_description()])
