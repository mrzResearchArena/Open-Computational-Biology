def motifs(S, k):
    d = {}

    for i in range(len(S) - k + 1):
        kmer = S[i:i + k]

        if kmer in d:
            d[kmer] += 1
        else:
            d[kmer] = 1

    return d



