import numpy as np


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

# v = readFASTA('/home/rafsanjani/Downloads/rosalind_cons(1).txt')
v = readFASTA('/home/rafsanjani/Downloads/rosalind_cons(2).txt')

# for i in v:
#     print(i)


m = len(v)
n = len(v[0])



profile = np.zeros((4, n), dtype=int)


A = []
C = []
G = []
T = []

def maximumNucleotide(d):
    maximum = max(d.values())
    base = '*'

    for key, value in d.items():
        if value == maximum:
            base = key
    return base


S = ''
for i in range(n):
    d = {'A':0, 'C':0, 'G':0, 'T':0}
    for j in range(m):
        d[v[j][i]] += 1

    S += maximumNucleotide(d)

    A.append(d['A'])
    C.append(d['C'])
    G.append(d['G'])
    T.append(d['T'])

def displayOneByOne(v):
    for i in v:
        print(i, end=' ')
    print()

print(S)
print('A: ', end=''); displayOneByOne(A)
print('C: ', end=''); displayOneByOne(C)
print('G: ', end=''); displayOneByOne(G)
print('T: ', end=''); displayOneByOne(T)


S = ''
for a, c, g, t in zip(A, C, G, T):
    d = {'A':a, 'C':c, 'G':g, 'T':t}
    S += maximumNucleotide(d)

# print(S)


