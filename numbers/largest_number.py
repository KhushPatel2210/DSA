#Find the largest digit in a number

n=97428
temp=n
count=0
d=''
max_no =0
while temp>0 :
    k=temp%10
    d +=str(k)
    if k>max_no:
        max_no=k
    temp=temp//10
    count+=1

print(count)
print(int(d))
print(max_no)
