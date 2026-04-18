
# normal count occurance
a=[2,6,35,2,64,29,64,2]
freq = {}

count = 0
for i in a :
    if i == 2:
        count += 1
print(count)

for i in a :
    if i in freq :
        freq[i] +=1
    else :
        freq[i] = 1
print(freq)

# automatic for all no. count is pending