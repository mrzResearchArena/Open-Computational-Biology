
def hd(x, y):
    C=0
    for i, j in zip(x, y):
        if i != j:
            C += 1
    return C

def f(dna, d):
    import itertools
    k = len(dna)
    v = list(itertools.product('ACTG', repeat=k))

    kmers = []
    for i in v:
        kmers.append(''.join(i))


    for kmer in kmers:
        if hd(kmer, dna)<=d:
            print(kmer)


dna = 'acg'.upper()
d = 1

f(dna, d)



