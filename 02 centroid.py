def calculate_centroid(pdb_file):
    sum_x = sum_y = sum_z = 0.0
    atom_count = 0

    file = open(pdb_file, 'r')
    
    for line in file:
        if line.startswith("ATOM"):
            x = float(line[30:38].strip())
            y = float(line[38:46].strip())
            z = float(line[46:54].strip())
            
            sum_x += x
            sum_y += y
            sum_z += z
            
            atom_count += 1

    centroid_x = sum_x / atom_count
    centroid_y = sum_y / atom_count
    centroid_z = sum_z / atom_count

    print(f'Centroid coordinates: ({centroid_x:.3f}, {centroid_y:.3f}, {centroid_z:.3f})')

pdb_file = '1ltx.pdb'
calculate_centroid(pdb_file)
