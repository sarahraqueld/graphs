
class readinput:
    def get_input_file(self):
        inputfile = []
        f = open('input.txt', 'r')

        for line in f:
            vetor = line.split( )
            inputfile.append(vetor)
        return inputfile
