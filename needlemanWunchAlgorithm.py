sequence1= "AGTGAAAGTGTTCAGTTAGGAGCCCCTTTAGATAATGC"
sequence2= "AAGTGATAGTGTTCAGTTAGGAGTCCCTTTAGATAATGC"
# sequence1="TGGTG"
# sequence2="ATCGT"

match=1
mismatch=-1
gap=-2
matrix=[]



for j in range(len(sequence2)+1): #(len(sequence1)):
    #evertime we reach a a new row add a list
    newList=[]
    matrix.append(newList)

    for i in range (len(sequence1)+1):
        print("j is",j)
        print("i is",i)

        #variables to store values of diagonal,left and up
        d=0
        l=0
        u=0
        diagonal=False
        matched=False
        #for getting diagonal value
        if(j-1>=0 and i-1>=0):
            d=matrix[j-1][i-1]
            diagonal=True
            #if matched
            if(i<len(sequence2) and sequence2[j-1]==sequence1[i-1]):
                d=d+1
                matched=True
                print("*************")
            else:
                d=d-1

        #for getting up value
        if(j-1>=0 ):
            u=matrix[j-1][i]+gap
            
        #for getting left value
        if(i-1>=0 ):
            l=matrix[j][i-1]+gap
        
        print("d=",d)
        print("l=",l)
        print("u=",u)
        print("len of j in matrix  is ",len(matrix))
        print("len of i in matrix is ",len(matrix[0]))
        
        if(diagonal and not(matched)):
             maxValue=max(d,l,u)
             print("max value is ",maxValue)
             matrix[j].append(maxValue)
             print(matrix)
        elif(diagonal and matched):
            # maxValue=max(d,l,u)
            # print("max value is ",maxValue)
            # matrix[j].append(maxValue)
            matrix[j].append(d)
            print(matrix)
        else:
            minValue=min(d,l,u)
            print("min value is ",minValue)
            matrix[j].append(minValue)
            print(matrix)

#printing the matrix
print("        ",end="")
txt="{:^4}"
for i in range(len(sequence1)):
    print(txt.format(sequence1[i]),end="")
print()
        


for i in range (len(matrix)):
    if(i!=0 ):
        print(txt.format(sequence2[i-1]),end="")
    else:{
            print(txt.format(" "),end="")
    }
    for j in range(len(matrix[i])):
        
        print(txt.format(matrix[i][j]),end="")
    print()



