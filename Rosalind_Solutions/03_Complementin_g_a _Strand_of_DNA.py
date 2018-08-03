def complementElements(dna):
    complement = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}

    newDNA = ''
    for base in dna:
        newDNA += complement[base]
    return newDNA

def main():

    # dna = 'AAAACCCGGT'
    with open('/home/rafsanjani/Downloads/rosalind_revc(2).txt', 'r') as File:
        dna = next(File).strip()

    dna = dna[::-1]
    print(complementElements(dna))

if __name__ == '__main__':
    main()


