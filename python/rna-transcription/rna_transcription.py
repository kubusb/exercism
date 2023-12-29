def to_rna(dna_strand):
    rna_strand = ""
    for letter in dna_strand:
        if letter == "":
            rna_strand += ""
        if letter == "G":
            rna_strand += "C"
        if letter == "C":
            rna_strand += "G"
        if letter == "T":
            rna_strand += "A"
        if letter == "A":
            rna_strand += "U"
    return rna_strand
