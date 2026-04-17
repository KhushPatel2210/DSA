a=[34,63,24,62,37,34,74,48,26,59,4,74,59,24,1,3,6]

b=[1,1,1,1,1]

c=[1,2,3,4,6,7]



sum = 0

for i in range(0,len(a)):
    if i%2==0:
        print(a[i])
print(sum)

# ## 15 swap the first and last element 

# temp = a[0]
# a[0] = a[-1]
# a[-1] = temp

# print(a)


## 26 remove the duplicate from the array

k = set(a)
print(k)


## 28 find common element from the 2 array

# for i in c:
#     for j in a :
#         if i==j:
#             print(i)


# ## 29 count element greater then x
# x=50
# count = 0

# for i in a:
#     if i<x:
#         count += 1
# print(count)




# ## 24 find the product of all item in array 

# mul =1

# for i in range(0,len(c)):
#     mul *= c[i]

# print(mul)

# ## 23 multipie all the elements with 2

# for i in range(0,len(c)):
#     c[i]=c[i]*2
# print(c)



## 22 find the diff btw the max and min 
# max = a[0]
# min = a[0]

# for i in a:
#     if max<i:
#         max = i

# print(max)

# for i in a:
#     if min>i:
#         min = i
# print(min)

# diff = max-min
# print(diff)


## 21 find the missing no of the 1 to N
# for i in range(1,len(c)):
#     if c[i]-c[i-1] != 1 :
#         print("missing no",c[i-1]+1)
          
    
## 20 move all zero at the end PENDING
# nums = [0,1,0,3,0,12]

# count = 0
# k=[]

# for i in range(0,len(nums)-1):
#     # print(nums[i])
#     if nums[i] == 0:
#         count +=1
#         print(i)
#         k.append(i)

# print(k)

# for i in range(1,len(k)):
#     print(k[i])
#     nums.pop(k[i])

# print(nums)
# print(count)



## 19 kth smallest element 

# for i in range(0,len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]>a[j]:
#             temp = a[i]
#             a[i]=a[j]
#             a[j]=temp
# print(a)

# k = int(input("enter the number"))
# print(a[k-1])

## 18 array is already sorted or not ?

# for i in range(len(b)-1,0,-1):
#     if b[i-1]<=b[i]:
#         print("true")
#     else:
#         print("false")
#         break





# ## 16 sorting in ascending order 

# for i in range(0,len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]>a[j]:
#             temp = a[i]
#             a[i] = a[j]
#             a[j] = temp
# print(a)


# ## 17 sorting in decending order
# c=[]

# for i in range (len(a),0,-1):
#     c.append(a[i-1])
# print(c)



## 14 Check if array is a palindrome

# c=[]

# for i in range(len(b),0,-1):
#     print(b[i-1])
#     c.append(b[i-1])

# print(c)






## rotate array to the left & right by 1
# lenght = 0
# for i in a :
#     lenght +=1
# print(lenght)

## 12 rotate from the left side 
# k=2
# for i in range(0,k):

#     last_element = a[lenght-1]
#     print(last_element)

#     a.pop()
#     # print(a)

#     a.insert(0,last_element)
#     print(a)

## 13 rotate from the right side 

# for i in range(0,k):
#     first_element = a[0]
#     print("first_element")

#     a.pop(0)

#     a.insert(lenght,first_element)
#     print(a)

## 9 find all duplicate no from the array

# a.sort()
# print(a)
# b=[]
# for i in range(1,len(a)):
#     if a[i-1] == a[i]:
     
#             b.append(a[i])
    
# print(b)

#issue if we have same no more that 2 time than it will repeat again in the b array


## 10 count even odd no from the array 
# count_even=0
# count_odd=0

# for i in a :
#     if i%2==0:
#         count_even += 1
#     else :
#         count_odd += 1

# print(count_odd)
# print(count_even)

# 11 revrse array


# b=[]
# for i in range(len(a),0,-1):
#     # print(a[i-1])
#     b.append(a[i-1])

# print(b)



