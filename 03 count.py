def count_nitrogen_atoms(pdb_file):
    count = 0
    with open(pdb_file, 'r') as file:
        for line in file:
            # PDB lines start with ATOM 
            if line.startswith('ATOM'):
                # Atom name is in columns 13-16 (indices 12-16 in 0-based index)
                atom_name = line[12:16].strip()
                if atom_name == 'N':  # Check if the atom is nitrogen
                    count += 1
    return count

# Example usage
pdb_file = '1ltx.pdb'  # Replace with your actual file path
nitrogen_count = count_nitrogen_atoms(pdb_file)
print(f'The number of nitrogen (N) atoms in the PDB file is: {nitrogen_count}')