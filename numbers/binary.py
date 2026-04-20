n=10

if n==0:
    print("0")
temp=n
binary=''
while temp>0:
    k=temp%2
    binary=str(k)+binary
    temp=temp//2
print(binary)

counter=0
for i in binary:
    counter+=1
# print(counter)

sum_binary=0
power=0

for i in range(counter-1,-1,-1):
    # print("binary",binary[i])
    k=int(binary[i])*pow(2,power)
    power+=1
    sum_binary += k
    # print(k)

print(sum_binary)