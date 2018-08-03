
with open('/home/rafsanjani/Downloads/rosalind_ba3c.txt', 'r') as F:
    kmers = []
    for line in F:
        kmers.append(line.strip())

    def equal(kmer):
        for i in kmers:
            if i[:-1] == kmer[1:]:
                return i
        return '*'


    for kmer in kmers:
        v = equal(kmer)

        if v == '*': None
        else:
            print('{} -> {}'.format(kmer, v))




