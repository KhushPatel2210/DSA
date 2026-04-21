a=[23,64,26,27,48,37,79,2]

# for i in range(1,3):
#     k=a[0]
#     a.pop(0)
#     a.append(k)
# print(a)

for i in range(1,4):
    k=a[len(a)-1]
    print(k)
    a.pop()
    a.insert(0,k)
print(a)