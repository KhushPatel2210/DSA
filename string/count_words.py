# from collections import Counter

a="hey my self khush patel i"

# k = Counter(a)
# print(k)

freq = {}

for char in a :
    if char in freq :
        freq[char] += 1
    else :
        freq[char] = 1 
print(freq)

count=0 
# print(len(a))

for i in a :
    if i == "h":
        count+=1
print(count)


# k=a.split()
# print(k)
# count = 0
# k=a.replace("h","hii")
# print(k)

# for i in a :
#     count += 1
# print(count)

# for i in a :
#     # print(i)
#     if i == "h":
#        print("yes")
#        k= i.replace("h","l")
#        print(k)
#        print(a)

# b=[]

# for i in k:
#     if(len(i)==1):
#         b.append(i[0].upper())
#     else:
#         b.append(i[0].upper()+i[1:-1]+i[-1].upper())

# print(b)
# final = " ".join(b)
# print(final)