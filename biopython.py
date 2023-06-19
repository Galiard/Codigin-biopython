import Bio
from Bio.Seq import Seq 

seq1 = Seq("ACGTAGCTACGATCACAGCTA")
print("Minha sequência é", seq1)
print('_'*50)
rc = seq1.reverse_complement()
print("O reverso complementar é", rc)
print('_'*50)
rna = seq1.transcribe()
print("A sequência transcrita é", rna)
print('_'*50)
protein = seq1.translate()
print("A sequência da proteína é", protein)
print('_'*50)


# Tabela de código genético
codigo_genetico = {
    'A': 'Alanina',
    'R': 'Arginina',
    'N': 'Asparagina',
    'D': 'Ácido aspártico',
    'C': 'Cisteína',
    'Q': 'Glutamina',
    'E': 'Ácido glutâmico',
    'G': 'Glicina',
    'H': 'Histidina',
    'I': 'Isoleucina',
    'L': 'Leucina',
    'K': 'Lisina',
    'M': 'Metionina',
    'F': 'Fenilalanina',
    'P': 'Prolina',
    'S': 'Serina',
    'T': 'Treonina',
    'W': 'Triptofano',
    'Y': 'Tirosina',
    'V': 'Valina',
    '*': 'Códon de parada'
}

protein_sequence = protein  

for amino_acid in protein_sequence:
    if amino_acid in codigo_genetico:
        print(f"Aminoácido: {amino_acid} | Nome: {codigo_genetico[amino_acid]}")
    else:
        print(f"Aminoácido: {amino_acid} | Nome: Desconhecido")