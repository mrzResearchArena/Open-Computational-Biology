
def hd(S1, S2):
    C=0
    for base1, base2 in zip(S1, S2):
        if base1 is not base2: C+=1
    return C

hd('ATCG', 'ATGG') # return 1


