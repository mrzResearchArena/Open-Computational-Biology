
def longestCommonPrefix(S1, S2):
    i = 0
    while i < len(S1) and i < len(S2) and S1[i] == S2[i]:
        i += 1
    return S1[:i]
    
    


