
blosum = open("BLOSUM62.csv", 'r').readlines()
blosum62 = {}
hsp = {}
aalabels = blosum[0].rstrip("\n").split(",")[0:20]

for j in range(1,21):
    tempdata = blosum[j].rstrip("\n").split(",")
    
    for i in range(1, 21):
        # print(aalabels[j-1], end="_")  
        # print(aalabels[i-1])
        tempkey = aalabels[j-1]+"_"+aalabels[i-1]
        blosum62[tempkey] = tempdata[i]
        # print (tempkey, tempdata[i])
        if (aalabels[j-1] == aalabels[i-1]):
            hsp[aalabels[i-1]]= tempdata[i]

    print(blosum62)
    print(hsp)


    