# Open the PDB file and read it
file_path = open('1ltx.pdb', 'r').readlines()

# Extract residues and their amino acid names from chain B
residues = []
amino_acids = {}
for line in file_path:
    if line.startswith('ATOM') and line[21] == 'B':
        residue = int(line[22:26].strip())
        amino_acid = line[17:20].strip()
        if residue not in residues:
            residues.append(residue)
            amino_acids[residue] = amino_acid

# Find the center most residue and its corresponding amino acid
midpoint = len(residues) // 2
center_residue = residues[midpoint]
center_amino_acid = amino_acids[center_residue]

# Output the result
print("The center most residue in chain B is:", center_residue)
print("The corresponding amino acid is:", center_amino_acid)
