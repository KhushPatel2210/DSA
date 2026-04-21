nums1 = [4,9,5,8]
nums2 = [9,4,9,8,4]

common = []

for i in nums1 :
    for j in nums2:
        if i==j and i not in  common:
            common.append(i)
print(common)

#union 
union=[]

for i in nums1 :
    if i not in union:
        union.append(i)
for j in nums2:
    if j not in union:
        union.append(j)
print(union)