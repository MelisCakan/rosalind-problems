file_path = "rosalind_gc_1_dataset.txt"
data = open(file_path, "r")

def parse_data(data):
    sequences = {}
    id = ""
    seq = ""       

    for line in data:
        line = line.strip()
        if line[0] == ">" :
            if id:
                sequences[id] = seq
            id = line[1:]
            seq = ""
        else:
            seq += line

        if id:
            sequences[id] = seq

    return sequences

def gc_content(dna):
    gc_count = dna.count("G") + dna.count("C")
    dna_length = len(dna)
    return (gc_count/dna_length*100)    

def find_max_content(data):
    sequences = parse_data(data)

    max_gc_content = -1
    max_gc_id = ""

    for id, seq in sequences.items():
        gc = gc_content(seq)
        if gc > max_gc_content:
            max_gc_content = gc
            max_gc_id = id

    return f"ID: {max_gc_id}\nGC Content: {max_gc_content}"        

result = find_max_content(data)
print(result)