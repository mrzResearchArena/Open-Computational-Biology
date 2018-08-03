def hammingDistance(dna1, dna2):
    C=0
    for base1, base2 in zip(dna1, dna2):
        if base1 is not base2:
            C += 1

    return C


def main():

    with open('/home/rafsanjani/Downloads/rosalind_hamm(3).txt', 'r') as File:
        dna1 = next(File).strip()
        dna2 = next(File).strip()

    # dna1 = 'GAGCCTACTAACGGGAT'
    # dna2 = 'CATCGTAATGACGGCCT'

    print(hammingDistance(dna1, dna2))

if __name__ == '__main__':
    main()
    
