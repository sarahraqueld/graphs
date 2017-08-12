class Vertex:
    def __init__(self, description):
        self.__adjacents = []
        self.__color = 'white'
        self.__parent = None
        self.__root_distance = None
        self.__description = description
    
    def has_adjacent(self, vertex):
        for a in self.__adjacents:
            if(a == vertex):
                return True
        return False

    def print_adjacents(self):
        for a in self.__adjacents:
                print a.__description

    def add_adjacent(self, vertex):
        self.__adjacents.append(vertex)

    def remove_adjacent(self, vertex):
        self.__adjacents.remove(vertex)
        print('Adjacente do vertice ', self.description, ' foi removido: ' , vertex.description)
    

    ###### Properties #####
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, d):
        self.__description = d
    
    @description.setter
    def parent(self, p):
        self.__parent = p
    
    @description.setter
    def root_distance(self, d):
        self.__root_distance = d

    @description.setter
    def color(self, c):
        if(c == 'white' or c == 'black' or c == 'gray'):
            self.__color = c
        else:
            raise Exception('Invalid color, setting to white')
            self.__color = 'white'
    
    @property
    def adjacents(self):
        return self.__adjacents

    @property
    def parent(self):
        return self.__parent

    @property
    def root_distance(self):
        return self.__root_distance