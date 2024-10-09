# Read the FASTA file and remove newline characters
with open('gene.fasta', 'r') as file:
    sequence = file.read().replace('\n', '')

# Initialize counts for each base and errors
counts = {'A': 0, 'T': 0, 'G': 0, 'C': 0, 'error': 0}

# Count each base in the sequence using if, elif, and else
for base in sequence:
    if base == 'A':
        counts['A'] += 1
    elif base == 'T':
        counts['T'] += 1
    elif base == 'G':
        counts['G'] += 1
    elif base == 'C':
        counts['C'] += 1
    else:
        counts['error'] += 1

# Calculate total count of bases
total_count = sum(counts.values())

# Calculate percentages for each base
percentages = {base: (count / total_count) * 100 for base, count in counts.items()}

# Print base counts
print("Base Counts:")
for base, count in counts.items():
    print(f"{base}: {count}")

# Print base percentages
print("\nBase Percentages:")
for base, percentage in percentages.items():
    print(f"{base}: {percentage:.2f}%")
