s = 'ACGT'

def f(dna, k):
    C = {}

    for a in s:
        for b in s:
            for c in s:
                for d in s:
                    for e in s:
                        for f in s:
                            for g in s:
                                C['{}{}{}{}{}{}{}'.format(a, b, c, d, e, f, g)] = 0

    for i in range(len(dna)-k+1):
        kmer = dna[i:i+k]
        C[kmer] += 1

    return C


dna = 'ATCGGATA'

v = f(dna, 7)

for key, value in v.items():
    print(value, end=' ')

#############################################################################################


s = 'ACGT'

from itertools import permutations, product

k = 7
v = product(s, repeat=k)

d = {}
for i in v:
    d[''.join(i)] = 0


dna = 'ATCGGGGG'
for i in range(len(dna)-k+1):
    kmer = dna[i:i+k]

    d[kmer] += 1

for key, value in d.items():
    print(value, end=' ')


