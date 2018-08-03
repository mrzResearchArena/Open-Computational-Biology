
def clump(S, k, L, t):
    selected = {}
    d = {}
    for i in range(len(S)-L+1):
        window = S[i:i+L]
        for i in range(len(window) - k + 1):
            kmer = window[i:i + k]
            if kmer in d:
                d[kmer] += 1
            else:
                d[kmer] = 1

        for key, value in d.items():
            if value >= t:
                selected[key] = value

        d.clear()
        # print(d)


    v = sorted(selected.items(), key=lambda x:x[1], reverse=True)
    return v


dna = 'CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC'

v = clump(dna, 5, 75, 4)


for i in v:
    print(i[0], end=' ')
    
    
