a=[5,3,35,26,31,4,76,37,4]
b=[4,76,43,23,3,5]


# a = [1,2,2]
# b = [2]

c=[]
for i in a :
    for j in b :
        if i==j and i not in c :
            c.append(i)

print(c)

c.sort()
print(c)
print(set(c))

