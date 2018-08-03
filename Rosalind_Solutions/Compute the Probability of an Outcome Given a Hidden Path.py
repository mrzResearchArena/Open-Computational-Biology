
d = {
    ('A', 'x'):0.388, ('A', 'y'):0.446, ('A', 'z'):0.166,
    ('B', 'x'):0.492, ('B', 'y'):0.463, ('B', 'z'):0.045,
}

xyz = 'yzyzzxxxxzzyyzxyyxxyyxxyyyzyxxyyyxyxyxzxyyxzzyzyzx'
AB = 'ABAAABAAAAABBBABABBBAABBABABBABBBABAAABBABAAABAAAA'

result = 1.0
for one, two in zip(AB, xyz):
    result *= d[(one, two)]

print(result)


