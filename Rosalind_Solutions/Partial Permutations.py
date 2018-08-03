def nPr(begin, end):
    result = 1
    for i in range(begin, end):
        result *= i
    return result % 1000000


n=97
r=8
begin = n-r
print(nPr(begin+1, n+1))


