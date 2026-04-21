a = [1,2,3,2,4,1,5]


a.sort()
print(a)


for i in range(len(a)-1,0,-1):
    if a[i] == a[i-1]:
        a.pop(i)
print(a)

freq = {}

for i in a:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print(freq)

for i in freq:
    if freq[i]!=1:
        print(i)

# this method gives output in the hash or dic if we have specific output in the array have to use another method
# freq={}

# for i in a :
#     if i in freq:
#         freq[i] +=1
#     else:
#         freq[i] = 1


# print(freq)

# for i in freq:
#     if freq[i]!=1:
#         print(i)


# for i in freq:
#     if freq[i] ==1:
#         print(i)


# for i in range(0,len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]>a[j]:
#             temp=a[i]
#             a[i]=a[j]
#             a[j]=temp

# print(a)

# for i in range(1,len(a)):
#     if a[i]==a[i-1]:
#         print("dupicate no",a[i])

# for i in range(1,len(a)-1):
#     if a[i] != a[i-1] and a[i] != a[i+1] :
#         print("unique elements",a[i])