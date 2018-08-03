import itertools

k=5 ### k (input)
v = itertools.product('ACGT', repeat=k)

C = {}
for i in v:
	C[''.join(i)] = 0

### Sequence (input)
dna = 'AAAAAAAAATTTTTTTTTCCCCCCCCCCCGGGGGGGGGGGG'
d = 2 ### d (input)


def hd(S1, S2):
    C=0
    for base1, base2 in zip(S1, S2):
        if base1 is not base2: C+=1
    return C


def reverseComplement(S):
	c = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

	newS = ''
	for base in S:
		newS = c[base] + newS
	return ''.join(newS)


def count(dna, kmer, d):
	C=0
	for i in range(len(dna)-k+1):
		if hd(dna[i:i+k], kmer)<(d+1):
			C += 1
	return C


for key, value in C.items():
	v = count(dna, key, d)  + count(dna, reverseComplement(key), d)
	C[key] = v

v = max(C.values())

# print(sorted(C.items(), key=lambda x:x[1], reverse=True))

# print(v)

for key, value in C.items():
	if v == value:
		print(key, end=' ')
		
		
		
