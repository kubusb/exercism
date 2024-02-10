PROTEIN_MATRIX = {
    "Codon" :   "Protein",
    "AUG"   :	"Methionine",
    "UUU"   :   "Phenylalanine",
    "UUC"	:   "Phenylalanine",
    "UUA"   :   "Leucine",
    "UUG"	:   "Leucine",
    "UCU"   :   "Serine",
    "UCC"   :   "Serine",
    "UCA"   :   "Serine",
    "UCG"   :	"Serine",
    "UAU"   :   "Tyrosine",
    "UAC"   :	"Tyrosine",
    "UGU"   :   "Cysteine",
    "UGC"	:   "Cysteine",
    "UGG"   :   "Tryptophan",
    "UAA"   :   "STOP",
    "UAG"   :   "STOP",
    "UGA"   :   "STOP"
    }

def proteins(strand):
    result = []
    split_strands = []
    current_protein_code = ""
    for index, letter in enumerate(strand):
        current_protein_code += letter
        if (index + 1) % 3 == 0:
            if current_protein_code == "UAA" or current_protein_code == "UAG" or current_protein_code == "UGA":
                break
            split_strands.append(current_protein_code)
            result.append(PROTEIN_MATRIX[current_protein_code])
            current_protein_code = ""
    return result
            