a = "hello from khush am i"
k=a.split()
result=[]

for i in k :
    if len(i)==1:
        result.append(i[0].upper())
    else:
        result.append(i[0].upper()+i[1:-1]+i[-1].upper())

final = " ".join(result)
print(final)