a = "hello from khush"
b=[]

# for i in range(len(a),0,-1):
#     b.append(a[i-1])
# print(b)

# final="".join(b)
# print(final)


k=a.split()
print(k)

for i in range(0,len(k)):
    word = k[i]
    temp=""
    for j in range(len(word)-1,-1,-1):
        temp += word[j]
    b.append(temp)
print(b)

final = " ".join(b)
print(final)