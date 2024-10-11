sequence1 = "MKTAYIAKQRQISFVKSHFSRQDILDLWIYHTQGYFPDWQNYTPGPGIRYPLTF"
sequence2 = "QFTAYIAKQRQISFVKSHFSRQDILRLWIYHTHGYMPDWQNYTPGPGIRYPQRF"

aascore = {"A" : 1, "C" : 5, "D" : 3, "E" : 3.5, "F" : 7, "G" : 6, "H" : 8, "I" : 2, "K" : 7.5, 
           "L" : 2, "M" : 4, "N" : 6, "P" : 6, "Q" : 4, "R" : 8, "S" : 4, "T" : 6, "V" : 3, "W" : 10, "Y": 9 }
hsp = {}

for j in aascore.keys():
    for l in aascore.keys():
        for m in aascore.keys():
            print(j, l, m)
            print((aascore[j] + aascore[l] + aascore[m]) / 3)  
            if (aascore[j] + aascore[l] + aascore[m]) / 3 > 3.0:
                triplet_aa = j + l + m
                hsp[triplet_aa] = 1


triplet_dict1 = {}
triplet_dict2 = {}

for i in range(0, len(sequence1) - 2):
    triplet = sequence1[i:i+3]
    if triplet in triplet_dict1.keys():
        val = triplet_dict1[triplet]
        val = val + 1
        triplet_dict1[triplet] = 1
    else:
        triplet_dict1[triplet] = 1

for i in range(0, len(sequence2) - 2):
    triplet = sequence2[i:i+3]
    if triplet in triplet_dict2.keys():
        val = triplet_dict2[triplet]
        val = val + 1
        triplet_dict2[triplet] = val
    else:
        triplet_dict2[triplet] = 1

for k in triplet_dict1.keys():
    if k in triplet_dict2.keys():
        print (k[2], end= " ")
    else:
        print ("-", end= " ")
        
print()
