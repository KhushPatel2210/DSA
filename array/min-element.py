a=[4,3,6,33,64,23]

# inbuilt method
# print(min(a))

#using sort method
# a.sort()
# print(a[0])

#manual way
min = a[0]
# print(min)
for i in a :
    if min>i:
        min = i

# for i in range(1,len(a)):
#     if min>a[i]:
#         min = a[i]

print(min)