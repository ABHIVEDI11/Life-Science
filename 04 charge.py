# Open and read the PDB file
pdb_file = open("1ltx.pdb", 'r').readlines()

# Dictionary to store charge values
charge_dict = {
    'LYS': 1,  # Lysine
    'ARG': 1,  # Arginine
    'ASP': -1, # Aspartic Acid
    'GLU': -1  # Glutamic Acid
}

# Variable to store total charge
total_charge = 0

# Loop through each line in the PDB file
for line in pdb_file:
    if line.startswith("ATOM"):
        # Get the residue name
        residue_name = line[17:20].strip()
        
        # Check if residue name corresponds to charged amino acids
        if residue_name in charge_dict:
            total_charge += charge_dict[residue_name]

# Print total charge of the protein
print(f"Total charge of the protein: {total_charge}")
