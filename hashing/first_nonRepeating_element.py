arr = [4, 5, 1, 2, 1, 2, 4]

freq={}

for i in arr:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)

for key,value in freq.items():
    if value==1:
        print(key,value)
        break

