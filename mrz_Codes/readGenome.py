
def readGenome(fileName):
    genome = ''
    with open(fileName, 'r') as file:
        for line in file:
            if line[0] != '>':
                genome += line.strip()
    return genome

genome = readGenome('/home/rafsanjani/in.fasta')

