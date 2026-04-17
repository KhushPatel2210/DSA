a=[4,3,6,33,64,23,26]
count_even = 0

#counting even numbers
for i in a :
    if i%2==0:
        print(i)
        count_even += 1
    
print(count_even)

#counting odd numbers
count_odd = 0

for i in a :
    if i%2==1:
        print(i)
        count_odd += 1
    
print(count_odd)

#even index element
print("even index from the array")
for i in range(0,len(a)):
    if i%2==0:
        print(a[i])

#odd index element
sum_odd = 0
print("odd index from the array")
for i in range(0,len(a)):
    if i%2==1:
        print(a[i])
        sum_odd += a[i]
print("sum odd",sum_odd)

#sum of even index
sum_even = 0
for i in range(0,len(a)):
    if i%2==0:
        print(a[i])
        sum_even += a[i]
print("sum even",sum_even)