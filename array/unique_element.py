a=[56,34,23,64,56,34]

a.sort()
print(a)
print(len(a))


for i in range(len(a)-1,1,-1):
    if a[i-1] == a[i]:
        a.pop(i)
print(a)

b=[]

for i in a :
    if i not in b :
        b.append(i)
print(b)
        
        