from Bio import SeqIO
from Bio.Seq import Seq


def translate_orfs(dna_sequence):  # Ищем возможные белковые посл.
    start_codon = 'M'
    stop_codons = {'TAA', 'TAG', 'TGA'}

    def find_proteins(seq): # Перевод ДНК в белковые посл.
        proteins = set()
        for frame in range(3):
            protein = '' # Для записи текущей аминопосл.
            start_found = False
            for i in range(frame, len(seq) - 2, 3):
                codon = seq[i:i + 3]
                amino_acid = Seq(codon).translate()  # Превращ. ДНК в аминокислоту
                if amino_acid == start_codon:
                    start_found = True
                    protein = start_codon
                elif amino_acid == '*':
                    if start_found:
                        proteins.add(protein)
                        start_found = False
                        protein = ''
                elif start_found:
                    protein += amino_acid
        return proteins

    # Генерируем 6 возможных рамок считывания
    forward_frames = find_proteins(dna_sequence)
    reverse_frames = find_proteins(str(Seq(dna_sequence).reverse_complement()))

    return forward_frames | reverse_frames


with open("KF731659.fasta") as fasta_file:
    record = next(SeqIO.parse(fasta_file, "fasta"))
    dna_seq = str(record.seq)
    proteins = translate_orfs(dna_seq)

for protein in proteins:
    print(protein)