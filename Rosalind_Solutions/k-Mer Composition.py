
def motifs(S, k):
    d = {}
    for i in range(len(S)-k+1):
        kmer = S[i:i+k]

        if kmer in d:
            d[kmer] += 1
        else:
            d[kmer] = 1

    return d

def readFASTA(fileName):
    genome = ''
    with open(fileName, 'r') as file:
        for line in file:
            if line[0] != '>':
                genome += line.strip()
    return genome

genome = readFASTA('/home/rafsanjani/Downloads/rosalind_kmer.txt')

v = motifs(genome, 4)

v = sorted(v.items())

for i in v:
    print(i[1], end=' ')



