sequence1 = "MKTAYIAKQRQISFVKSHFSRQDILDLWIYHTQGYFPDWQNYTPGPGIRYPLTF"
sequence2 = "QFTAYIAKQRQISFVKSHFSRQDILRLWIYHTHGYMPDWQNYTPGPGIRYPQRF"
blosum = open("BLOSUM62.csv", 'r').readlines()

blosum62 = hsp = triplet_dict1 =triplet_dict2 = {}

aalabels = blosum[0].rstrip("\n").split(",")[0:20]

for j in range(1,21):
    tempdata = blosum[j].rstrip("\n").split(",")

    for i in range(1, 21):
        tempkey = aalabels[j-1]+"_"+aalabels[i-1]
        blosum62[tempkey] = tempdata[i]
        if (aalabels[j-1] == aalabels[i-1]):
            hsp[aalabels[i-1]]= tempdata[i]
    

for i in range(0, len(sequence1) - 2):
    triplet = sequence1[i:i+3]
    tripletscore = 0
    for j in range(0,3):
        tripletscore = tripletscore + int(hsp[triplet[j]])
        print (triplet, tripletscore)

    # print(blosum62)
    # print(hsp)
   

aascore = {"A" : 1, "C" : 5, "D" : 3, "E" : 3.5, "F" : 7, "G" : 6, "H" : 8, "I" : 2, "K" : 7.5, 
           "L" : 2, "M" : 4, "N" : 6, "P" : 6, "Q" : 4, "R" : 8, "S" : 4, "T" : 6, "V" : 3, "W" : 10, "Y": 9 }

triplet_dict1 = {}
triplet_dict2 = {}

for i in range(0, len(sequence2) - 2):
    triplet = sequence2[i:i+3]
    tripletscore = 0
    for j in range (0,3):
        tripletscore = tripletscore + int(hsp[triplet[j]])
    if (tripletscore >= 18):
        if triplet in triplet_dict1.keys():
            val = triplet_dict1[triplet]
            val = val + 1
            triplet_dict1[triplet] = 1
        else: 
            triplet_dict1[triplet] = 1

for i in range(0, len(sequence1) - 2):
    triplet = sequence1[i:i+3]
    if triplet in triplet_dict1.keys():
        val = triplet_dict1[triplet]
        val = val + 1
        triplet_dict1[triplet] = 1
    else:
        triplet_dict1[triplet] = 1


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