from Bio import Entrez

data = open("NCT00000107.xml")

records = Entrez.read(data)

for record in records:
	print  record['breif_title']

	