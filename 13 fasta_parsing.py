f = open("sequence.fasta", 'r')
lines = f.readlines()
f.close()

seq_dict = {}
seq_name = None  
for line in lines:
    if line.startswith('>'):
        seq_name = line[1:].strip()
        seq_dict[seq_name] = ""
    else:
        if seq_name:  
            seq_dict[seq_name] += line.strip()
print(seq_dict)
