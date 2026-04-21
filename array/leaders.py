arr = [16,17,4,3,5,2]

counter = 0
for i in arr:
    counter += 1

print(counter)
leader=[]
l=float('-inf')

for i in range(counter-1,-1,-1):
        if arr[i]>l:
            leader.append(arr[i])
            l=arr[i]
print(leader)
