
####################################################
# Complement
####################################################


def complement(S):
    c = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}

    newS = ''
    for base in S:
        newS += c[base]
    return newS
    

####################################################
# Reversed Complement
####################################################


def reverseComplement(S):
    c = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}

    newS = ''
    for base in S:
        newS = c[base] + newS
    return newS
    
    


    


