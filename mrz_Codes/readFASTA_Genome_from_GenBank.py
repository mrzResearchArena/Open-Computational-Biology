##############################################################################
##############################################################################
##############################################################################


from Bio import Entrez
Entrez.email = "mrzResearchArena@gmail.com" # Rafsanjani Muhammod

IDs = 'JX069768 JX469983'.split()

handle = Entrez.efetch(db='nucleotide', id=IDs, rettype='fasta')
records = handle.read()

print(records)


##############################################################################
##############################################################################
##############################################################################


from Bio import Entrez
Entrez.email = "mrzResearchArena@gmail.com" # Rafsanjani Muhammod
from Bio import SeqIO

IDs = 'JX069768'

handle = Entrez.efetch(db='nucleotide', id=IDs, rettype='fasta')
records = list(SeqIO.parse(handle, 'fasta'))  # we get the list of SeqIO objects in FASTA format
records = records[-1].seq

print(records)


##############################################################################
##############################################################################
##############################################################################



