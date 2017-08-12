#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint

class Graph:
    def __init__(self, vertices, directed):
        if( not isinstance(directed, bool)):
            raise Exception('Problem with args')
        self.__vertices = vertices
        self.__directed = directed
    
    def initialize_vertices(self):
        for v in self.__vertices:
            v.parent = None
            v.color = 'white'
            v.root_distance = None

    def add_vertex(self, vertex):
        self.__vertices.append(vertex)

    def remove_vertex(self, vertex):
        self.__vertices.remove(vertex)
        for v in self.__vertices:
            if(v.has_adjacent(vertex)):
                v.remove_adjacent(vertex)


    def add_edge(self, origin, destination):
        origin.add_adjacent(destination)
        if(not self.__directed):
            destination.add_adjacent(origin)

    def remove_edge(self, origin, destination):
        origin.remove_adjacent(destination)
        if(not directed):
            destination.remove_adjacent(origin)

    def print_vertices(self):
        print("Vértices atuais deste grafo:")
        for v in self.__vertices:
            print v.description

    def __str__(self):
        graph = ''
        for v in self.__vertices:
            graph += 'Vertice '
            graph += str(v.description)
            graph+= 'of color '
            graph += v.color
            graph +=  ' with adjacents: '
            for adj in v.adjacents:
                graph +=  adj.description
                graph += ' '
            graph += '\n'
        return graph

    
    
    # Busca em largura
    def bfs(self):
        fila_vertices = []
        self.initialize_vertices()
        index = randint(0, len(self.__vertices) -1)
        root = self.__vertices[index]
        root.color = 'gray'
        root.root_distance = 0
        print 'A raiz dessa busca é ', root.description
        fila_vertices.append(root)
        vertice_atual = None

        while(fila_vertices):
            vertice_atual = fila_vertices.pop()
            print 'Vertice visitado: ', vertice_atual.description
            for adj in vertice_atual.adjacents:
                print 'adj: ', adj.description
                if( adj.color == 'white'):
                    adj.color = 'gray'
                    adj.root_distance = vertice_atual.root_distance + 1
                    adj.parent = vertice_atual
                    fila_vertices.insert(0, adj)
            vertice_atual.color = 'black'

    
    def search(self, vertex):
        print 'Visited vertex: ' , vertex.description
        vertex.color = 'gray'
        for adj in vertex.adjacents:
            if(adj.color == 'white'):
                adj.parent = vertex
                self.search(adj)
        vertex.color = 'black'


    # Busca em profundidade
    def dfs(self):
        self.initialize_vertices()
        index = randint(0, len(self.__vertices) -1)
        root = self.__vertices[index]
        root.color = 'gray'
        root.root_distance = 0
        print 'A raiz dessa busca é: ', root.description
        self.search(root)

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
