# function to calculate volume of a atom

radii = {'H': 120, 'O': 152, 'C':170, 'N': 155, 'S': 180}

def volume(radius):
	vol = (4/3) * 3.14 * (radius**3)
	return vol

total_volume = 0

pdbfile = open('1ltx.pdb', 'r')
for line in pdbfile.readlines():

	if line.rstrip()[0:4] == 'ATOM':
		#print(line.rstrip())
		if line[13:14] == 'C':
			total_volume += volume(radii['C'])
		elif line[13:14] == 'N':
			total_volume += volume(radii['N'])

print(f'Total volume of atom :{total_volume:.3f}')
