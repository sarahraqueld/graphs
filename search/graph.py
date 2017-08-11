#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Graph:
    def __init__(self, vertices, directed):
        if( not isinstance(directed, bool)):
            raise Exception('Problem with args')
        self.__vertices = vertices
        self.__directed = directed
    
    @property
    def vertices(self):
        return self.__vertices
    @property
    def directed(self):
        return self.__directed

    def removeVertex(self, vertex):
        self.__vertices.remove(vertex)
        for v in self.__vertices:
            if(v.has_adjacent(vertex)):
                v.remove_adjacent(vertex)


    def print_vertices(self):
        print("Vértices atuais deste grafo:")
        for v in self.__vertices:
            print v.description

    def add_edge(self, origin, destination):
        origin.add_adjacent(destination)
        if(not directed):
            destination.add_adjacent(origin)

    def remove_edge(self, origin, destination):
        origin.remove_adjacent(destination)
        if(not directed):
            destination.remove_adjacent(origin)

    # Busca em profundidade
    def dfs():
        return 'dfs'

    def is_connected(self):
        dfs()
        for v in self.__vertices:
            if(v.color == 'white'):
                return False
        return True