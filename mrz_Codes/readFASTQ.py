
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
        
S, Q = readFASTQ('/home/rafsanjani/MyDrive/Education/Bioinformatics/in.fastq')

