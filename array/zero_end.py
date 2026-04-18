a = [0,1,0,3,12]
i=0
n=len(a)

while i<n:
    if a[i]==0:
        a.pop(i)
        a.append(0)
        n -= 1
    else:
        i+=1    



print(a)