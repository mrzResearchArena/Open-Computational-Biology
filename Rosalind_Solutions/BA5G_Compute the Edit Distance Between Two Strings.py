
def ed(x, y):
    D = []
    for i in range(len(x)+1):
        D.append([0]*(len(y)+1))

    for i in range(len(y)+1):
        D[0][i] = i

    for i in range(len(x) + 1):
        D[i][0] = i

    for i in range(1,len(x)+1):
        for j in range(1, len(y)+1):

            horizontal = D[i][j-1]+1
            vertical =   D[i-1][j]+1

            if x[i-1] == y[j-1]:
                diagonal = D[i-1][j-1]
            else:
                diagonal = D[i-1][j-1]+1

            # diagonal = D[i-1][j-1] if x[i-1] == y[j-1] else D[i-1][j-1] + 1
            # print('i={}, j={}, horizontal = {}, vertical = {}, diagonal = {}'.format(i, j, horizontal, vertical, diagonal))

            D[i][j] = min(horizontal, vertical, diagonal)

            # D[i][j] = min(D[i][j-1]+1, D[i-1][j]+1, D[i-1][j-1] if x[i-1] == y[j-1] else D[i-1][j-1] + 1)

    return D[-1][-1]

s1 = 'PLEASANTLY'
s2 = 'MEANLY'

print(ed(s1, s2))



