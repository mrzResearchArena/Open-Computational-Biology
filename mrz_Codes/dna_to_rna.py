
def dnaToRNA(dna):
    rna = ''
    
    for base in dna:
        if base is 'T':
           rna += 'U'
        else:
            rna += base

    return rna


#####################################################################################    
    
def rnaToDNA(rna):
    dna = ''
    
    for base in rna:
    
        if base is 'U':
            dna += 'T'
        else:
            dna += base
            
    return dna


######################################################################################

def rnaToMRNA(rna):
    complements = {'A':'U', 'U':'A', 'C':'G', 'G':'C'}

    mRNA = ''
    for base in rna:
        mRNA += complements[base]
    return mRNA




