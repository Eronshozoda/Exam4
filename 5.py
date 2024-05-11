a1 = int(input())
a2=a1
sum=0
while a1 > 0:
    digit = a1 % 10
    a1 = a1 // 10
    sum+=digit
if a2%sum==0:
    print(True)
else : 
    print(False)