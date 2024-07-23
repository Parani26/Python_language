# CS1010S --- Programming Methodology
# Mission 7

# Note that written answers are stored in """multi-line strings"""
# to allow us to run your code easily when grading your problem set.

import csv

def read_csv(csvfilename):
    rows = ()
    with open(csvfilename) as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            rows += (tuple(row), )
    return rows


##########
# Task 1 #
##########

def replicate(dna_strand):
    dna_base_pairings = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G"
    }
    new_strand = ""
    for base in dna_strand:
        new_strand += dna_base_pairings[base]
    return new_strand[::-1]


print("## Q1 ##")
print(replicate("AAATGC"))     # 'GCATTT'
print(replicate("ATTGGGCCCC")) # 'GGGGCCCAAT'

with open("dna.txt") as f:
    dna = f.read()
print(replicate(dna)[:10])    #'AATAGTTTCT'


##########
# Task 2 #
##########

def find_transcription_region(dna_strand):
    index = [0, 0]
    for i in range(len(dna_strand)):
        if dna_strand[i:i+4] == "TATA":
            index[0] = i + 4
            break
    for i in range(len(dna_strand)):
        if dna_strand[i:i+4] == "CGCG":
            index[1] = i + 4
            break
    if index == [0, 0]:
        return None
    else:
        return dna_strand[index[0]:index[1]]


print("## Q2 ##")
print(find_transcription_region("AGCTTAGCTATATCGTTAATTGCAGAGACGCGA"))
# 'TCGTTAATTGCAGAGACGCG'
print(find_transcription_region("TATAAGCTTAGCTATATAGCGTACAGTCCGCGACGCG"))
# 'AGCTTAGCTATATAGCGTACAGTCCGCG'
print(find_transcription_region("AGCGAGCGTAGC"))
# None


##########
# Task 3 #
##########

def transcribe(dna_strand):
    dna_strand = find_transcription_region(dna_strand)
    dna_replicated = replicate(dna_strand)
    rna = ""
    for base in dna_replicated:
        if base == "T":
            rna += "U"
        else:
            rna += base
    return rna

def reverse_transcribe(rna_strand):
    reversal = {
        "A": "T",
        "U": "A",
        "G": "C",
        "C": "G"
    }
    dna = ""
    for base in rna_strand:
        dna += reversal[base]
    return dna[::-1]


print("## Q3 ##")
print(transcribe("AGCTTAGCTATATCGTTAATTGCAGAGACGCGA"))
 # 'CGCGUCUCUGCAAUUAACGA'
print(transcribe("TATAATTGGGCCCCCGCG"))
 # 'CGCGGGGGCCCAAU'

print(reverse_transcribe("CGCGUCUCUGCAAUUAACGA")) 
# 'TCGTTAATTGCAGAGACGCG'
print(reverse_transcribe("CGCGGGGGCCCAAU")) 
# 'ATTGGGCCCCCGCG'

rna = transcribe(dna)
print(rna[:10])
# 'CGCGGCAUAG'
print(reverse_transcribe('CGCGGCAUAG'))
# 'CTATGCCGCG'


##########
# Task 4 #
##########

def get_mapping(csvfilename):
    data = read_csv(csvfilename)
    dic = {}
    for pairing in data[1:]:
        dic[pairing[0]] = pairing[3]
    return dic

print("## Q4 ##")
codon2amino = get_mapping("codon_mapping.csv")

# Uncomment to test your function
# print(codon2amino["ACA"]) # 'T'
# print(codon2amino["AUU"]) # 'I'
# print(codon2amino["CUC"]) # 'L'
# print(codon2amino["ACU"]) # 'T'
# print(codon2amino["UAG"]) # '_'
# print(codon2amino["UGA"]) # '_'


##########
# Task 5 #
##########

def translate(rna_strand):
    codon2amino = get_mapping("codon_mapping.csv")

    def find_translation_region(rna_strand):
        a = rna_strand + "A"
        index = ["x", "x"]
        n = 0
        for i in range(len(a)):
            if a[i:i+3] == 'AUG':
                index[0] = i
                n = i % 3
                break
        if index[0] != "x":
            for i in range(len(a)):
                if i > index[0] + 2 and i % 3 == n:
                    if (a[i:i+3] == 'UAA') or (a[i:i+3] == 'UAG') or (a[i:i+3] == 'UGA'):
                        index[1] = i + 4
                        break
        if index[0] == "x" or index[1] == "x":
            return None
        else:
            return a[index[0]:index[1]]

    active_rna = find_translation_region(rna_strand)
    codons = []
    if active_rna is None:
        return None
    else:
        for i in range(len(active_rna)):
            if i % 3 == 0 and (i + 2) <= len(active_rna):
                codons += [active_rna[i] + active_rna[i+1] + active_rna[i+2]]
        final_protein = ""
        for codon in codons:
            final_protein += codon2amino[codon]
        return final_protein


print("## Q5 ##")
print(translate("AUGUAA"))           # 'M_'
print(translate("AGAGAUGCCCUGAGGG")) # 'MP_'

protein = translate(rna)
print(protein) # 'MNLLKLLSTNSLGISKLNGGFELYFCTCLVNCM_'
print(protein == 'MNLLKLLSTNSLGISKLNGGFELYFCTCLVNCM_') # True
