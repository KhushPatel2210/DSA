n=28

perfect = 0
for i in range(1,n):
    if n%i==0:
        print(i)
        perfect += i

print("perfect",perfect)
if perfect==n:
    print("it is the perfect number")
else:
    print("it is not a perfect number")