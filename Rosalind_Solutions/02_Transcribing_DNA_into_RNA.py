def convertDNAtoRNA(dna):
    rna = ''
    for base in dna:
        if base is 'T':
           rna += 'U'
        else:
            rna += base
    return rna


def main():

    # dna = 'GATGGAACTTGACTACGTAAATT'
    with open('/home/rafsanjani/Downloads/rosalind_rna(1).txt', 'r') as File:
        dna = next(File).strip()
	
	# dna = dna.replace('A', 'U'); print(dna)
    print(convertDNAtoRNA(dna))
    

if __name__ == '__main__':
    main()
