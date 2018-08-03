

with open('/home/rafsanjani/Downloads/rosalind_ba3e.txt', 'r') as F:
    kmers = []
    for line in F:
        kmers.append(line.strip())

    from collections import defaultdict
    d = defaultdict(list)

    for kmer in kmers:
        prefix = kmer[:-1]
        suffix = kmer[1:]

        if prefix in d:
            d[prefix].append(suffix)
        else:
            d[prefix].append(suffix)
        # print('{} -> {}'.format(prefix, suffix))

    # print(d)

    for key, value in d.items():
        if len(value)>1:
            print('{} -> '.format(key), end='')
            C=True
            for i in value:
                if C==True:
                    print('{}'.format(i), end='')
                else:
                    print(',{}'.format(i), end='')
                C = False
            print()
        else:
            print('{} -> {}'.format(key, value[0]))
            
            
         
         
         
