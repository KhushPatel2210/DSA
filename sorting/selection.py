a=[3,13,6,34,7,1,4,5]

for i in range(len(a)):
    min_element=i
    for j in range(i+1,len(a)):
        if a[j]<a[min_element]:
            min_element= j
    a[i],a[min_element]=a[min_element],a[i]
print(a)




