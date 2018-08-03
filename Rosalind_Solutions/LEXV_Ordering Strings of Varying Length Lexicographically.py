# Avoiding warning
import warnings
def warn(*args, **kwargs): pass
warnings.warn = warn
# _______________________________


import itertools

v = []
n = 4
s = 'DOJNRFHCZGY'
for i in range(1,n+1,1):
    C = itertools.product(s, repeat=i)
    for j in C:
        v.append(''.join(j))


v = sorted(v, key=lambda word: [s.index(i) for i in word])

for i in v:
    print(i)
    
    
