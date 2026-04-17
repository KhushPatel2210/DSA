a=[4,3,6,33,64,23]

max_elemet = 0
# print(max_elemet)
k=len(a)
print(k)

for i in range(1,k) :
    if a[i]>max_elemet:
        max_elemet = a[i]

print(max_elemet)