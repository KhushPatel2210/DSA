a=[34,63,24,62,37,34,74,48,26,59,4,74,34]

# max element from the array
max_no=a[0]

for i in a :
    if max_no<i:
        max_no = i
    
print(max_no)

#min element from the array
min_no = a[0]

for i in a :
    if min_no>i:
        min_no = i

print(min_no)

# sum of all element 

sum = 0

for i in a :
    sum += i
print(sum)

# to find the length of the array
count = 0

for i in a:
    count += 1
print(count)

#average of the array
average = int(sum/count)
print(average)

#second highest no from the array 

# have to implement the sort logic manually 
a.sort()
print(a)

for i in range(len(a)-1,1,-1):
    if(a[i]==a[i-1]):
        continue
    else:
        print(a[i-1])
        break

#Check if a number exists in the array

if 26 in a :
    print("found it")
else:
    print("not found")

#find index of the given number

for i in range(1,len(a)):
    if a[i]==26:
        print(i)

print(a.index(26))

# this will give the index 2 bcz we already sorted the array in the above code 

#count how many time a number repeat
no_of_count = 0
for i in a:
    # print(i)
    if i == 34:
        no_of_count += 1

print(no_of_count)

