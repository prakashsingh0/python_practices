#create lower triangular matrix
#row maroj order
ltm = 1
matrix = []
for i in range(1,4):
    for j in range(1,4):
        if i >= j:
          matrix.append(ltm+1)  
        else:
           matrix.append(0)
    
        ltm += 1
print(matrix)