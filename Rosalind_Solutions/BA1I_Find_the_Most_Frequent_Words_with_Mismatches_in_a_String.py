
import itertools

k = 4
v = itertools.product('ACGT', repeat=k)

C = {}
for i in v:
	C[''.join(i)] = 0

dna = 'AAAAAATTTTTTTTCCCCCCCCCCCCGGGGGGGGGGGG'
d = 1

def hd(S1, S2):
    C=0
    for base1, base2 in zip(S1, S2):
        if base1 is not base2: C+=1
    return C

def count(dna, kmer, d):
	C=0
	for i in range(len(dna)-len(kmer)+1):
		if hd(dna[i:i+len(kmer)], kmer)<(d+1):
			C += 1
	return C

for key, value in C.items():
	v = count(dna, key, d)
	C[key] = v

# print(sorted(C.items(), key=lambda x:x[1], reverse=True))

v = max(C.values())

for key, value in C.items():
	if v == value:
		print(key, end=' ')
		
		
		
