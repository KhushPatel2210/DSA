arr = [2,2,1,1,1,2,2]

n=len(arr)//2
print(n)

count = 0

freq={}

for i in arr:
    if i in freq:
        freq[i]+=1
    else:
        freq[i] = 1
    
print(freq)

for key,value in freq.items():
    if value>n:
        print("key",key,"value",value)
