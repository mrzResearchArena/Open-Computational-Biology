def hammingDistance(dna1, dna2):
    C=0
    for base1, base2 in zip(dna1, dna2):
        if base1 is not base2:
            C += 1

    return C

import numpy as np

def hamm( s1 , s2 ):

    a = np.fromstring(s1)
    b = np.fromstring(s2)

    print(a)
    print(b)
    # return np.sum( a != b )


def main():

    # with open('/home/rafsanjani/Downloads/rosalind_hamm(3).txt', 'r') as File:
    #     dna1 = next(File).strip()
    #     dna2 = next(File).strip()
    #
    # # dna1 = 'GAGCCTACTAACGGGAT'
    # # dna2 = 'CATCGTAATGACGGCCT'
    #
    # print(hammingDistance(dna1, dna2))

    # s1 = 'GAGCCTACTAACGGGAT'
    # s2 = 'CATCGTAATGACGGCCT'
    # # print(sum([a != b for (a, b) in zip(s1, s2)]))
    #
    # print(hamm(s1, s2))

    # alphabets = list('ABCDE')
    # layers = 4
    # print(list('ABCD'))


    # table ={
    #
    #     'A':71.03711,
    #     'C':103.00919,
    #     'D':115.02694,
    #     'E':129.04259,
    #     'F':147.06841,
    #     'G':57.02146,
    #     'H':137.05891,
    #     'I':113.08406,
    #     'K':128.09496,
    #     'L':113.08406,
    #     'M':131.04049,
    #     'N':114.04293,
    #     'P':97.05276,
    #     'Q':128.05858,
    #     'R':156.10111,
    #     'S':87.03203,
    #     'T':101.04768,
    #     'V':99.06841,
    #     'W':186.07931,
    #     'Y':163.06333,
    # }
    #
    # aminoAcid = 'ILPAKDIECWAAIRFIQLQYICKVTHVGPQVMNEWYCPSQIWGEYIKLDPNHDRRKSANQEYMCWFNIEEKIFNCSRWQSLPIQDIFLLNHPVFTCPHVEHTFDVAQTECVCTAKAKWTPCKSCAWVNHSMCVIVWINEASYRTKKDTCKNQQASYYMNTHQMTFMNYEWDCNGGHHYACSAQALAMENRPMHGTIRILHCCRIQIMNTVREMPRFFESLWGGHDDTGMNSQKMTTWMESPPKWCLVMFKFPTPAEEIHIQRKTDPEQDGLEFLFNGAIQVTSIIDALTQHWCPQPNCQKNHGDIWEYRKMLRRIKHNNVRHNFMSQRAGSVQTTRDSSIKNFHMCAMRSSGYGDNRRHNDLMYRYNQWTGYQCMPQNFNACSPCFMHLSSFIACTKCVKMSYKPHQYGPVRINMYALGFCCCCHPKQAYMWYDDFRKMARWKETNLFYLYNMVGRVLEWDMKKKTFNLLPQQHEICMGPHWGQLSWYNMQSECCHSRACTFYECSEERAVYSMNGRLGTNAWKTPKHNTQTYPTASCEEIYRVMMVLQWFDHDRTYFYEYEPYNSRIKFGEEAVWMYLPIFQHPDNVFQDFQQVACVEFYECMMWFHANELGDNGPKPFQMEATLKRFGATVNFTEYHHQEHLHKTHCRVSCTQTPNLWQPEPVRQPTGRFRWKIHFQWKYGTKHAYSIMVVLVHWLIKWQRQKGFKQAYFYRMTEWDMMWKQYVLQPSSTMSHIYKQNHFRRRRIWMLMESGHFHNVRCYDCMDYVCFVGGYAKKTSRATQRRDQNLTDQGGVYWIRTHTRAVLEPTACAENFNVYRQGGRRTIMSSVSQQWKHCYHPMFWNMCMKMHHYPAPYSPRHGMTWPLPMELKARSWCNYSDYFTIEPQHHNYWMKWDFEHTQFLYWHHKLHSKNLLTWWRENVFIMWFNTYEWSHNKFYSNELRNEWFM'
    # C=0
    # for acid in aminoAcid:
    #     C += table[acid]
    # print('{0:0.3f}'.format(C))

    # def fibonacci(n):
    #     if n==0: return 0
    #     else:
    #         if n==1:
    #             return 1
    #         else:
    #             return fibonacci(n-1)+fibonacci(n-2)
    #
    #
    # print(fibonacci(24))
    # n1 = int(input())
    # n2 = int(input())
    #
    # A1 = map(int, input().split())
    # A2 = map(int, input().split())
    #
    # print(n1)
    # print(n2)
    # print(A1)
    # print(A2)

    # A1 = [int(i) for i in input().split()]
    # with open('/home/rafsanjani/Downloads/rosalind_bins(1).txt', 'r') as File:
    #     _, _, A1, A2 = [line.strip().split('\n') for line in File.readlines()]
    #     A1 = [int(i) for i in A1[0].split()]
    #     A2 = [int(i) for i in A2[0].split()]
    #
    #
    # d = {}
    # C=1
    # for i in A1:
    #     d[i] = C
    #     C += 1
    #
    # # A2 = [int(i) for i in input().split()]
    #
    # for i in A2:
    #     try:
    #         print(d[i], end=' ')
    #     except:
    # #         print(-1, end=' ')
    # def longestCommonPrefixes(S1, S2):
    #     i=0
    #     while i<len(S1) and i<len(S2) and S1[i] == S2[i]:
    #         i += 1
    #     return S1[:i]
    #
    # def rc(s):
    #     complement = {'A':'T', 'C':'G', 'T':'A', 'G':'C'}
    #     dna = ''
    #     for base in s:
    #         dna = complement[base] + dna
    #     return dna
    #
    def gcContent(dna):
        total = len(dna)
        C=0
        for base in dna:
            if base == 'C' or base == 'G':
                C+=1

        return (C/total)*100

    # print(gc('CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT'))

    # /home/rafsanjani/MyDrive/Education/Bioinformatics/lambda_virus.fa

    names = []
    percentage = []

    # with open('/home/rafsanjani/Downloads/rosalind_gc(1).txt', 'r') as file:
    #     genome = ''
    #     for line in file:
    #         if line[0] == '>':
    #             names.append(line.strip()[1:])
    #             if len(genome)>0:
    #                 # print(gcContent(genome))
    #                 percentage.append(gcContent(genome))
    #             genome = ''
    #         else:
    #             genome += line.rstrip()
    #
    #     percentage.append(gcContent(genome))
    #
    #     # print(names)
    #     # print(percentage)
    #
    #     d = dict(zip(names, percentage))
    #
    #     # print(d)
    #
    #     print(sorted(d.items(), key=lambda x:x[0]))
    #
    # #     import bisect
    #
    # def ASCIItoQ(v):
    #     return ord(v)-33
    # # def QtoPhred33(v):
    # #     return chr(v+33)
    #
    # print(ASCIItoQ(':'))

    def ASCIItoQ(v):
        return ord(v)-33




    S, Q = readFASTQ('/home/rafsanjani/MyDrive/Education/Bioinformatics/in.fastq')
    # print(len(S))
    # print(len(Q))
    # print(ASCIItoQ('I'))

    # def createHistogram(Q):
    #     H = [0]*50
    #     for eachQ in Q:
    #         for phred in eachQ:
    #             # print(phred)
    #             q = ASCIItoQ(phred)
    #             H[q] += 1
    #     return H
    #
    # H = createHistogram(Q)
    import matplotlib.pyplot as pl
    # pl.plot(range(len(H)), H)
    # pl.show()
    #
    # print(len(S[999]))
    # print(len(Q))

    def findGCbyPosition(S):
        gc = [0]*100 #len(Q[0])
        total = [0]*100 #len(Q[0])
        # print(gc)

        for eachS in S:
            for i in range(len(eachS)):
                if eachS[i] == 'C' or eachS[i] == 'G':
                    gc[i] += 1
                total[i] += 1
        #
        for i in range(len(gc)):
            gc[i] = gc[i] / total[i]
            # print(gc[i], total[i])
        # return gc
        # print(gc)

        return gc

    gc = findGCbyPosition(S)
    # pl.plot(range(len(gc)), gc)
    # pl.show()

    C60plus = 0
    C50to60 = 0
    C50below = 0

    C50to55 = 0
    C55to60 = 0

    C55to56 = 0
    C56to57 = 0
    C57to58 = 0
    C58to59 = 0
    C59to60 = 0

    for p in gc:
        if p>0.60:
           C60plus += 1

        if p<0.5:
            C50below += 1

        if 0.5<=p<=.60:
            C50to60 += 1

        if 0.5<=p<=0.55:
            C50to55 += 1

        if 0.55<=p<=0.60:
            C55to60 += 1

        if 0.55<=p<0.56:
            C55to56 += 1

        if 0.56<=p<0.57:
            C56to57 += 1

        if 0.57 <= p < 0.58:
            C57to58 += 1

        if 0.58 <= p < 0.59:
            C58to59 += 1

        if 0.59 <= p < 0.60:
            C59to60 += 1

    print(C60plus)
    print(C50below)
    print(C50to60)
    print(C50to55)
    print(C55to60)

    print(C55to56)
    print(C56to57)
    print(C57to58)
    print(C58to59)
    print(C59to60)



    # from collections import Counter
    # C = Counter()
    #
    # for eachS in S:
    #     C.update(eachS)
    # print(C)

def reverseComplements(s):
    complement = {'A':'T', 'C':'G', 'T':'A', 'G':'C', 'N':'N'}
    dna = ''
    for base in s:
        dna = complement[base] + dna
    return dna

def naive(t, p):
    occurrences = []
    for i in range(len(t) - len(p) + 1):
        match = True
        for j in range(len(p)):
            if t[i+j] != p[j]:
                match = False
                break
        if match:
            occurrences.append(i)
    return occurrences



def readFASTQ(fileName):
    with open(fileName, 'r') as file:
        S = []
        Q = []

        while True:
            _ = file.readline()
            eachS = file.readline().strip()
            _ = file.readline()
            eachQ = file.readline().strip()
            if len(eachS)==0: break
            S.append(eachS)
            Q.append(eachQ)
        return S, Q

def run():
    text = 'AGCTTAGATAGC'
    pattern = 'AG'

    print(len(text))
    print(naive(text, pattern))

import random
def generateReads(genome, numReads, readLen):
    ''' Generate reads from random positions in the given genome. '''
    reads = []
    for _ in range(numReads):
        start = random.randint(0, len(genome)-readLen) - 1
        reads.append(genome[start : start+readLen])
    return reads


def bioinformatics():
    fileName = '/home/rafsanjani/MyDrive/Education/Bioinformatics/phix.fa'
    genome = readGenome(fileName)
    # print(genome)

    # Generate 100 reads of length 100
    reads = generateReads(genome, 100, 100)

    # Count how many reads match the genome exactly
    numMatched = 0
    for r in reads:
        matches = naive(genome, r)
        # print(matches)
        if len(matches) > 0:
            numMatched += 1
    print('%d / %d reads matched the genome exactly!' % (numMatched, len(reads)))

    S, _ = readFASTQ('/home/rafsanjani/MyDrive/Education/Bioinformatics/ERR.fastq')

    numMatched = 0
    n = 0
    for r in S:
        matches = naive(genome, r[:30])
        n += 1
        if len(matches) > 0:
            numMatched += 1
    print('%d / %d reads matched the genome exactly!' % (numMatched, n))

    numMatched = 0
    n = 0
    for r in S:
        r = r[:30]  # just taking the first 30 bases
        matches = naive(genome, r)
        matches.extend(naive(genome, reverseComplements(r)))
        n += 1
        if len(matches) > 0:
            numMatched += 1
    print('%d / %d reads matched the genome exactly!' % (numMatched, n))

def readGenome(fileName):
    genome = ''
    with open(fileName, 'r') as file:
        for line in file:
            if line[0] != '>':
                genome += line.strip()
    return genome



if __name__ == '__main__':
    # main()
    # bioinformatics()
    dna1 = 'CATAACGGCGCCGGACTCATACATGCGATCGACCAGATTAATATGTCGTGTGCAAAACGGCACGATGTGAAGCGTGTTTACGAGAGGTAAATAGGTGCGGGATCTCGGAATGTGTGTCGGTTGGACTACAGGGTTAGAGGTCGGGAAAGATGATACGATTTGAGCACAATTCCTGGTCGCACGGGGATCCAGGGCAGCTGAGGATGCATCCCCCGAAGATGGACGCCCTAGGCGTGTTCGAGCATACTCAAGCTATCGTCCAATCGTCACTGTGCAGACCCAACACTACAGTGGCTATATTCCGCCATCCCGCTGTACTTTCTGGCTGTCAACGTCGCGCATCTCCAGAACGACTGGTCTGCACTTGGAGGATTCCCCCAATGTGCCTCATCACGAATGAACCCCATCATAAACGGGTGCGTAGTTGAGTTTTCTCCTGGTCGGCCCAAGAAAATATGCCAGTGCGTTGTCGAATTCAACCTTTCCCTAAACAAAGAACCAACTTCTAAGGCTCGCCATTCTCCCATAGCGACACTAGTGGGAAATCCCCATGGACATATGGGAAAACAGGTCCAATCCTGTGACGCGTGCGATTTACTACCAGCTATGACGACAGAACGTAGAATACTTGTTTCGGCTTCAGAGGGAGGTCTATGTACTCGTTATTTCGAGCCAATCCGGTTGACCGTTACAAGCGATGGCGTCCACCGTACTTTCGTAAGTCTGTTGGCTAAAATGTGTTATAACGATTCTGGAAATGTCGGCCTGTAGCTATTGTTCATATAGCCATCGTGATGCCCACACCATTAAAAAATTTCTCTAACTGTATGATTGCTGGGTCTCGGTGTCAGGAAATTGGTCTAGGGTAGTCTTCGATAAACCCATAGGCAGGGACATTGAAGCCCCATACCCCCCTACAAGCCTGTTTTTCGGATTTGTTCCGGGACCTGTGAAAATTGCGCCAGGATTACACCGCGGATTTTTTATTACGGATTTTAGGATCAC'
    dna2 = 'CCCTAAACCACGCTTCCTCCTTAATATGTCTGACAAGGATTATACTAAGCGAATCACATCCTCTGTATCTGTTAAGACCATTCTCCGCCTAATAGTACCTAAGTCGGAATGGAGTGGGAACATCTATCCCTTTCGCACGCCATTCCCTGTTCAGCACCGGTATGGAAATACAACACCATAGGGACCTCCTTAATGATGTTGCTTTCTAATATATAGGGGGCCCCCAATCTCAAGTGTTGTCGTAAATATGCGCCTCCGTGCATGTTCTGAGATTCAAAACCCATGATATGGTGAAGCGCTATCCTATACCTTTACACCCATGCGCAGTGAATTACCGGCGTTATATATAAATATTCCTCCTGTGACTCAACAAAACGTCAATTCTAGTGTAGTAGGTGACCCCGTAGGGTATAAATCCTACGTTGATCTTGTCTTTTGTGTGTGTATCGAAGTAGTAAGAAGGATTCCGCAGGTTATTTGTGGTCGATGCGGACCGACGCATGGACCCTGTGGAGTTGGGCAAAGGTGTTGATACGCTGCAGATCGCCTATACTCTGTACCAGTTATAGACCACCGGGAGACGAACTAGCTACCCGGTAACGCCCGGCACGGTAGTGGAGTTGACGTTCCCCCGACAACCTCCAGGAGCAGGCCATATATTCAGTGTACTGGGCGTGTAGATGGGAGGCTCTGTATCTCGGCTGCTTCTTAGACGGAAGTCCCATCACTAACATGCCGCAAGGACGTGAGAAAGATTCGTAGGGCCCGGGCTTATCAAGTGTGACCAACTGGGCCGCAAGCATTCCGGCGGAGCCATAATGTTGCCCTGAGGTAATTCATCCCGTCACTTCTAACACAGGTAGGTAGCTCTCATCCAACGCCGTACCGTTTGGTGACGAGAATCGGTGTTCCAGAGTAATCGAGTAGATGCGAAGTCAAATGACCAGCGATCCTTATACGATGAGTTAAATCATACTGCGAGATAATATCTTCATTCCAGAGAAC'

    print(hammingDistance(dna1, dna2))
    
    
