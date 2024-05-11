k=input()
sum=0
for i in k:
    for j in i:
        if j=="a" or j=="A":sum+=4
        elif j=="e" or j=="E":sum+=3
        elif j=="i" or j=="I":sum+=1
        elif j=="o" or j=="O":sum+=0
        elif j=="u" or j=="U":sum+=0
print(sum)