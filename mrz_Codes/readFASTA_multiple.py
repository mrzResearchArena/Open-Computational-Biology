
def readFASTA(fileName):
    with open(fileName, 'r') as file:
        v = []
        genome = ''
        for line in file:
            if line[0] != '>':
                genome += line.strip()
            else:
                v.append(genome)
                genome = ''
        v.append(genome)
        del v[0]
        return v


v = readFASTA('/home/rafsanjani/Downloads/rosalind_cons(2).txt')


###########################################################################



def readFASTA(strings):
    strings = sorted(strings.split())
    
    v = []
    for i in strings:
        if i[0] == '>': None
        else:
            v.append(i)
    return v
    

v = readFASTA('/home/rafsanjani/Downloads/rosalind_cons(2).txt')


