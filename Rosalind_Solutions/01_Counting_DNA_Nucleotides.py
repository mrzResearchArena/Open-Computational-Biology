
def countDNAcontent(dna):
    # return dna.count('A'), dna.count('C'), dna.count('G'), dna.count('T')
    C = {'A':0, 'C':0, 'G':0, 'T':0}
    for i in dna:
        C[i] += 1
    return C

def main():
    with open('/home/rafsanjani/Downloads/rosalind_dna(2).txt', 'r') as F:
        dna = next(F).strip()
        
    print(countDNAcontent(dna))
    
if __name__ == '__main__':
    main()
