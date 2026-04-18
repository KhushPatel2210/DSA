a = "abcba ioi"

# print(a[::-1])
print(a.replace(" ",""))

count = 0
for i in a:
    # print(i)
    count += 1

print(count)
b=[]
for i in range(count,0,-1):
    b.append(a[i-1])
    print(a[i-1])

final = "".join(b)
print(final)

if final == a :
    print("it is palidrom string")
else:
    print("it is not a palidrom string")

vowel = 0
consonents = 0

for i in a :
    if i == "a" :
        vowel += 1
    elif i == "e":
        vowel +=1
    elif i == "i":
        vowel +=1
    elif i == "o":
        vowel +=1
    elif i == "u":
        vowel +=1
    else:
        consonents += 1
print(vowel)
print(consonents)
