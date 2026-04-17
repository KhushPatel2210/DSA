a=[4,3,6,33,64,23,26]
count_even = 0

for i in a :
    if i%2==0:
        print(i)
        count_even += 1
    
print(count_even)


count_odd = 0

for i in a :
    if i%2==1:
        print(i)
        count_odd += 1
    
print(count_odd)

#even index element

for i in range(0,len(a)):
    if i%2==0:
        print(a[i])

#odd index element
for i in range(0,len(a)):
    if i%2==1:
        print(a[i])
