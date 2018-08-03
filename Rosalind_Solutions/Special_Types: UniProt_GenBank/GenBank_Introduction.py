
from Bio import Entrez

def geneBank(genus, begin, end):
    Entrez.email = ''
    term = '{}[Organism] and ({}[PDAT]:{}[PDAT])'.format(genus, begin, end)
    handle = Entrez.esearch(db='nucleotide', term=term)
    record = Entrez.read(handle)
    return record['Count']

genus = 'Hydrogenobaculum'
begin = '2005/07/14'
end = '2011/07/31'

print(geneBank(genus, begin, end))


