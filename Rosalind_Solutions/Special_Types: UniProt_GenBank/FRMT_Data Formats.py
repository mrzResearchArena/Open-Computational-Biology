
from Bio import Entrez
Entrez.email = "mrzResearchArena@gmail.com" # Rafsanjani Muhammod
from Bio import SeqIO

IDs = 'JX308821 BT149867 NM_001159758 JX317624 JQ867090 NM_001133698 JX914595 NM_002133 JX398977'.split()

# print(IDs)

d = {}
v = []
for i in IDs:
    handle = Entrez.efetch(db="nucleotide", id=i, rettype="fasta")
    # records = handle.read()
    records = list(SeqIO.parse(handle, "fasta"))  # we get the list of SeqIO objects in FASTA format
    d[i] = len(records[-1].seq)


v = sorted(d.items(), key = lambda x:x[1])
# print(v)

handle = Entrez.efetch(db="nucleotide", id=v[0][0], rettype="fasta")
records = handle.read()
print(records)




