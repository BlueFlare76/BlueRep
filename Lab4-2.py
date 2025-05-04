from Bio import  SeqIO
input_file = 'merged_sequences.gb'
records = []

for record in SeqIO.parse(input_file, 'genbank'):
    gc_content = (record.seq.count('G') + record.seq.count('C')) / len(record.seq)
    records.append((record.id, str(record.description), gc_content))

records.sort(key=lambda x: x[2])

for record in records:
    print(f"{record[0]}: {record[1]} gene, complete cds, GC = {record[2]:.16f}")