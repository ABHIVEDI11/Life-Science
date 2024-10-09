f = open("gene_expression.txt", 'r')
lines = f.readlines()
sum = 0
count = 0
level = 0
for line in lines:
    try:
        level = float(line)
       
    except ValueError:
        print("line is not a number:", line)
        print(level)
    sum += level
    count += 1
    
print("average:", sum/float(count))
f.close()
