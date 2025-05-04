from Bio import SeqIO

genbank_file = "merged_sequences.gb"

for record in SeqIO.parse(genbank_file, "genbank"):

    print(f"Обработка записи: {record.id}")

    for feature in record.features:
        if feature.type == "mRNA":
            protein_sequences = []
    
            for location in feature.location:

                if location.type == "CDS":

                    seq = record.seq[location.start:location.end]

                    protein = seq.translate()
                    protein_sequences.append(str(protein))
                    print(f"Белковая последовательность: {protein}")