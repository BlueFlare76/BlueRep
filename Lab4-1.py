from Bio import Entrez, SeqIO

Entrez.email = "maxim.chaly.2006@gmail.com"

species_names = ["Brassica oleracea", "Solanum lycopersicum"]

records = []

for species in species_names:
    search_handle = Entrez.esearch(db="nucleotide", term=f"{species} complete cds", retmax=5)
    search_results = Entrez.read(search_handle)
    search_handle.close()

    id_list = search_results["IdList"]

    for seq_id in id_list:
        fetch_handle = Entrez.efetch(db="nucleotide", id=seq_id, rettype="gb", retmode="text")
        records.append(SeqIO.read(fetch_handle, "genbank"))
        fetch_handle.close()

output_file = "merged_sequences.gb"

with open(output_file, "w") as output_handle:
    SeqIO.write(records, output_handle, "genbank")

print(f"Все записи успешно сохранены в {output_file}.")