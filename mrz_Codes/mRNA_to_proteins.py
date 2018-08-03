
def mRNAtoProtein(mRNA):

    table = {
        'UUU': 'F', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V',
        'UUC': 'F', 'CUC': 'L', 'AUC': 'I', 'GUC': 'V',
        'UUA': 'L', 'CUA': 'L', 'AUA': 'I', 'GUA': 'V',
        'UUG': 'L', 'CUG': 'L', 'AUG': 'M', 'GUG': 'V',
        'UCU': 'S', 'CCU': 'P', 'ACU': 'T', 'GCU': 'A',
        'UCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
        'UCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A',
        'UCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
        'UAU': 'Y', 'CAU': 'H', 'AAU': 'N', 'GAU': 'D',
        'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
        'UAA': '*', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
        'UAG': '*', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
        'UGU': 'C', 'CGU': 'R', 'AGU': 'S', 'GGU': 'G',
        'UGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
        'UGA': '*', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
        'UGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'
    }

    
def sequenceToProtein(S):
    protein = ''

    for i in range(0, len(S), 3):
        if len(S[i:i + 3]) is 3:
            if table[S[i:i + 3]] is '*':
                return protein
            else:
                protein += table[S[i:i + 3]]
        else:
            return protein

    return protein

    
    
    
    ###################################################################
    
    table =\
		'''
		UUU F      CUU L      AUU I      GUU V
		UUC F      CUC L      AUC I      GUC V
		UUA L      CUA L      AUA I      GUA V
		UUG L      CUG L      AUG M      GUG V
		UCU S      CCU P      ACU T      GCU A
		UCC S      CCC P      ACC T      GCC A
		UCA S      CCA P      ACA T      GCA A
		UCG S      CCG P      ACG T      GCG A
		UAU Y      CAU H      AAU N      GAU D
		UAC Y      CAC H      AAC N      GAC D
		UAA *      CAA Q      AAA K      GAA E
		UAG *      CAG Q      AAG K      GAG E
		UGU C      CGU R      AGU S      GGU G
		UGC C      CGC R      AGC S      GGC G
		UGA *      CGA R      AGA R      GGA G
		UGG W      CGG R      AGG R      GGG G 
		'''

table = table.split()

table = dict(zip(table[0::2], table[1::2]))

print(table)
