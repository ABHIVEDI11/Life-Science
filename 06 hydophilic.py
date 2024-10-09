aa_hydro=['ALA','ILE','LEU','MET','PHE','PRO','VAL','TRP','TYR']

count = 0
pdbfile = open(input("please type your PDB filename:")).readlines()
#print (pdbfile)

for i in range (0,len(pdbfile)):
	line = pdbfile[i].rstrip()
	if line.startswith('ATOM'):
		count += 1

print(count)
		
	
