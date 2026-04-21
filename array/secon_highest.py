# a=[50,20,40,30,70,2,35,70]
a=[3,3,3,3,3,3,3,3,3]
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            temp = a[i]
            a[i]=a[j]
            a[j]=temp
        
print(a)

for i in range(len(a)-1,0,-1):
    if a[i]==a[i-1]:
        continue
    else:
        print(a[i-1])
        break

b=a[0]
c=a[0]

for i in range(len(a)):
    if c<a[i]:
        b=c
        c=a[i]
    else:
        print("there is no second highest no")
print(b)



# for i in range(0,len(a)):
#     for j in range(i+1,len(a)):
#         if a[i] > a[j]:
#             temp=a[i]
#             a[i]=a[j]
#             a[j]=temp

# print(a)
# for i in range(len(a)-1,-1,-1):
#     if a[i]==a[i-1]:
#         continue
#     else:
#         print(a[i-1])
#         break

# b=a[0]
# c=a[0]

# for i in range(0,len(a)):
#     if a[i]>b:
#         c=b
#         b=a[i]
#         # edge case pending in this for (5,5,5,5)
# print(c)
