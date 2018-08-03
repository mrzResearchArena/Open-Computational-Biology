
from itertools import permutations, product

k = 2
v = product('ACGT', repeat=k)

d = {}
for i in v:
    d[''.join(i)] = 0

print(d)


