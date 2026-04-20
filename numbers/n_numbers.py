n=10
sum=0
sum_even=0
sum_odd=0

for i in range(1,n+1):
    sum+=i
    print(i)
    if i%2==0:
        sum_even += i
    else:
        sum_odd += i

print(sum)
print(sum_odd)
print(sum_even)

