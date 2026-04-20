# s = "hello from khush"

# ch = 'f '

# first = -1
# last = -1

# for i in range(len(s)) :

#     if s[i] == ch :
#         if first == -1 :
#             first = i
#         last = i
# print(first)
# print(last)



# # anagram string



# a='khush'

# b='hushk'

# print(sorted(a)==sorted(b))


# fa ={}
# fb = {}

# for i in a :
#     if i in fa :
#         fa[i] += 1
#     else :
#         fa[i] =1

# for i in b :
#     if i in fb :
#         fb[i] += 1
#     else:
#         fb[i] =1

# print(fa)
# print(fb)

# if fa == fb :
#     print(True)
# else:
#     print(False)

#find the sortest word in the sentence 

s="Find the shortest word in sentence hi"

k=s.split()

print(k)


count = 0 
b = {}

for i in k :
    word = i
    for j in word:
        count += 1
    b[i] = count
    count = 0
print(b)


mine = min(b.values())

for x,y in b.items():
    if y==mine:
        print(x,y)


# count = 0

# b=[] 

# for i in k :
#     # print(i)
#     word = i
#     for j in word :
#         count += 1
#     b.append(count)
#     count=0

# print(b)

# short = b[0]

# for i in b :
#     if i < short :
#         short = i

# print(short)