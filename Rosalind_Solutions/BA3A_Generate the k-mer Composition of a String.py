
def kmers(dna, k):
    v = []
    for i in range(len(dna) - k + 1):
        v.append(dna[i:i + k])
    return v


v = kmers('TCCAAAACCTTACCGCGCTTTCAGTCCT', 5)

# print(v)

for i in v:
    print(i)
    
    
