a="abcabcabcabc"

k=set(a)
result = "".join(k)
print(result)

result = "".join(dict.fromkeys(a))
print(result)


result= ""

for i in a :
    if i not in result :
        result += i
print(result)


# length = 0

# for i in a:
#     length += 1
# # print(length)
# b=[]

# for i in range(0,length):
#     if a[i] == "a":
#         b.append(i)
    
# print(b)
# print(b[1]-b[0])