
seq1="ATGGGCTAACCCTTTGGGGGTAGGAATCG"
seq2="ATGAGCTAACCCTATGGGGGTAGGGATCG"
print(" ")
print(" ",(" ".join(list(seq1))))

for i in range(len(seq1)):
    print(seq2[i],end=" ")
    for j in range(len(seq2)):
        if(seq1[j]==seq2[i]):
            print(".",end=" ")
        else:
            print(" ",end=" ")
    print(end="\n")