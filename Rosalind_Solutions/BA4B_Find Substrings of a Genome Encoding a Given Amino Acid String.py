def reverseComplement(S):
    c = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

    newS = ''
    for base in S:
        newS = c[base] + newS
    return ''.join(newS)


table =\
    '''
    TTT F      CTT L      ATT I      GTT V
    TTC F      CTC L      ATC I      GTC V
    TTA L      CTA L      ATA I      GTA V
    TTG L      CTG L      ATG M      GTG V
    TCT S      CCT P      ACT T      GCT A
    TCC S      CCC P      ACC T      GCC A
    TCA S      CCA P      ACA T      GCA A
    TCG S      CCG P      ACG T      GCG A
    TAT Y      CAT H      AAT N      GAT D
    TAC Y      CAC H      AAC N      GAC D
    TAA *      CAA Q      AAA K      GAA E
    TAG *      CAG Q      AAG K      GAG E
    TGT C      CGT R      AGT S      GGT G
    TGC C      CGC R      AGC S      GGC G
    TGA *      CGA R      AGA R      GGA G
    TGG W      CGG R      AGG R      GGG G
    '''


table = table.split()

table = dict(zip(table[0::2], table[1::2]))


dna = 'ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA'
peptide = 'MA'
k = len(peptide)*3

def check(s, track):
    
    v = []
    for i in range(0,k,3):
        v.append(s[i:i+3])

    C=0
    for eachCodon, eachAminoAcid in zip(v, peptide):
        # print(eachCodon, eachAminoAcid)
        if table[eachCodon] != eachAminoAcid:
            break
        else:
            C = C+1
    if C == len(peptide):
        if track == 1:
            print(s)
        else:
            print(reverseComplement(s))

for i in range(len(dna)-k+1):

    check(dna[i:i+k], 1)
    check(reverseComplement(dna[i:i+k]), 2)


