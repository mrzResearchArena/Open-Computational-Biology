from Bio import ExPASy
from Bio import SwissProt

# id = 'Q5SLP9'
id = 'Q6IN36'

handle = ExPASy.get_sprot_raw(id)
record = SwissProt.read(handle=handle)

for x in record.cross_references:
    if x[0] == 'GO' and x[2][0] == 'P':
        print(x[2][2:])
        


