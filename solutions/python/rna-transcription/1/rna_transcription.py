def to_rna(dna_strand):
    l = []
    for item in dna_strand : 
        if item == "G" :
            new_item = "C"
        elif item == "C" : 
            new_item = "G"
        elif item == "T" : 
            new_item = "A"
        elif item == "A" :
            new_item = "U"
        l.append(new_item)
    new = "".join(l)
    return new
