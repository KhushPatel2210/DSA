with open("data.txt","w") as file:
    pass


with open("data.txt","r") as file :
    k=file.read()
print(k)

for i in range(0,5):
    print(i)
    with open ("data.txt","a") as file :
        file.write("hello\n")

text = input("please enter the text")

with open("data.txt",'a') as file:
    file.write(text+"\n")

with open("data.txt",'r') as file:
    k = file.read()
print(k)

k1=k.split()
print(k1)
k2=[]
result=''
for i in range(len(k1)):
    print(k1[i])
    a=k1[i]
    # print(len(a))
    for j in range(len(a)-1,-1,-1):
        result+=a[j]
    k2.append(result)
    result =''

# print(k2)

result=" ".join(k2)
print(result)