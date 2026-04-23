
num=1310
if num==0:
    print(True) 
temp=num
reverse1=0
reverse2=0
while temp>0:
    r=temp%10
    reverse1=reverse1*10+r
    temp=temp//10
print(reverse1)
while reverse1>0:
    r=reverse1%10
    reverse2=reverse2*10+r
    reverse1=reverse1//10
print(reverse2)       
if num==reverse2:
    print(True)
else :
    print(False)

        