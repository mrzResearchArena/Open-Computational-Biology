
d = { ('A','A'):0.509, ('A','B'):0.491, ('B','A'):0.402, ('B','B'):0.598,}

S = 'BAAABAAAABAAABABBAAAABBBBBBABAAABABAAABAABABBAABBB'

result = 0.50

for x,y in zip(S, S[1:]):
    result *= d[(x, y)]

print(result)

