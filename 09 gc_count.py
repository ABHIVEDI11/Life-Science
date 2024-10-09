# Step 1: Open the file and read the sequence
file_path = "gene.fasta"
with open(file_path, 'r') as file:
    sequence = file.read().replace('\n', '')

# Step 2: Calculate GC content
def calculate_gc_content(sequence):
    """Calculate the GC content of a DNA sequence."""
    gc_count = sequence.count('G') + sequence.count('C')
    return (gc_count / len(sequence)) * 100

# Step 3: Generate reverse complement
def reverse_complement(sequence):
    """Generate the reverse complement of a DNA sequence."""
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    rev_comp = ''.join(complement[base] for base in sequence[::-1])
    return rev_comp

# Step 4: Process the FASTA file
gc_content = calculate_gc_content(sequence)
rev_comp = reverse_complement(sequence)
print(f"GC Content: {gc_content:.2f}%")
print(f"Reverse Complement: {rev_comp}")
