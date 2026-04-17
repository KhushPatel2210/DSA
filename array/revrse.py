a=[4,3,6,33,64,23,26]
reverse=[]

# in-built method
# a.reverse()
# print(a)



for i in range(len(a),0,-1):
    print(a[i-1])
    reverse.append(a[i-1])

print(reverse)


# slicing method 
b=a[::-1]
print(b)