# Solution #1 ##############################################

reads='''
GCTTGTGT
CTTGTGTG
TTGTGTGG
'''.split()

v = reads[0]
for read in reads[1:]:
    v += read[-1]

print(v)


# Solution #2 ##############################################

kmers = '''
ACCGA
CCGAA
CGAAG
GAAGC
AAGCT
'''.split()

def search(pattern):
    for i in kmers:
        if i.startswith(pattern):
            return i
    return ''

seq = ''
ensure = True
for kmer in kmers:
    v = search(kmer[1:])
    if ensure == True:
        seq += kmer
        ensure = False
    if len(v) > 0:
        seq += v[-1]

print(seq)

