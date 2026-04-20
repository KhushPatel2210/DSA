#Find the length of a string

a="khu s hy"

counter=0
for i in a :
    counter += 1
print(counter)

# into upper case & lower case
k1=a.upper()
k2=a.lower()
print(k1)
print(k2)

print(a[0])
print(a[-1])

for i in a :
    if i == "y":
        print("yes")

# find the index of the character

for i in range(0,len(a)-1):
    if a[i]=="h":
        print(i)

counter1 =0
for i in a :
    if i == " ":
        counter1+=1
print(counter1)


s1="listen"
s2 = sorted(s1)
print(s2)

s1="hello from khush"
s1=s1.replace(" ","")
print(s1)

s1="hello from khushl"
freq = {}

for i in s1:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] =1
print(freq)

max1 = max(freq.values())

for char,count in freq.items():
    # print(char,count)
    if count == max1:
        print(char,count)
# max1 = max(freq.values())
# print(max1)

# name= max(freq,key=freq.get)
# print(name)


s1="hello from khush"

# k=len(s1)
# print(k)
# r=""

# for i in range(len(s1),0,-1):
#     print(s1[i-1])
#     r += s1[i-1]
# print(r)
