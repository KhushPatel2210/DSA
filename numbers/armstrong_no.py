# n=34

# temp=n
# sum = 0
# while temp>0:
#     k=temp%10
#     x=pow(k,3)
#     sum += x
#     temp=temp//10
#     print(temp)

# print(sum)

# if sum == n :
#     print("number is the armstrong no")
# else :
#     print("no")




# n=34
# b=[]
# temp=n
# sum = 0
# while temp>0:
#     k=temp%10
#     b.append(str(k))
#     temp=temp//10
#     print(temp)

# print(b)
# final="".join(b)
# print(final)
# print(int(final))


# n=3454

# temp=n
# count = 0
# while temp>0:
#     k=temp%10
#     count+=1
#     temp=temp//10

# print(count)

n=34

temp=n
maxno = 0
while temp>0:
    k=temp%10
    if k>maxno:
        maxno = k 
    temp=temp//10

print(maxno)