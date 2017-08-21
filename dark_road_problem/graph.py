#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint

class Graph:
    def __init__(self, directed):
        if( not isinstance(directed, bool)):
            raise Exception('Problem with args')
        self.__vertices = []
        self.__directed = directed
    
    def initialize_vertices(self):
        for v in self.__vertices:
            v.parent = None
            v.color = 'white'
            v.root_distance = None

    def add_vertex(self, vertex):
        for v in self.__vertices:
            if(v.description == vertex.description):
                return v
        self.__vertices.append(vertex)
        return vertex

    def remove_vertex(self, vertex):
        self.__vertices.remove(vertex)
        for v in self.__vertices:
            if(v.has_adjacent(vertex)):
                v.remove_adjacent(vertex)


    def add_edge(self, origin, destination, weight):
        origin.add_adjacent(destination, weight)
        if(not self.__directed):
            destination.add_adjacent(origin, weight)

    def remove_edge(self, origin, destination):
        origin.remove_adjacent(destination)
        if(not directed):
            destination.remove_adjacent(origin)

    def print_vertices(self):
        print("Vértices atuais deste grafo:")
        for v in self.__vertices:
            print v.description

    def print_edges(self):
        print("Arestas atuais deste grafo:")
        for v in self.__vertices:
            print v.print_adjacents()

    def __str__(self):
        graph = ''
        for v in self.__vertices:
            graph += 'Vertice '
            graph += str(v.description)
            graph+= 'of color '
            graph += v.color
            graph +=  ' with adjacents: '
            for adj in v.adjacents:
                graph +=  adj[0].description
                graph += ' '
            graph += '\n'
        return graph
    

    def is_connected(self):
        self.dfs()
        for v in self.__vertices:
            if(v.color == 'white'):
                print 'Is not connected'
                return False
        print 'Is connected'
        return True

    # Properties #

    @property
    def vertices(self):
        return self.__vertices
    @property
    def directed(self):
        return self.__directed
