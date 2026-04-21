a = [2,4,6,8]

sum=0
for i in range(len(a)):
    sum += a[i]
    a[i]=sum
print(a)


#Maximum Subarray Problem  
# brute force problem

arr = [-2,1,-3,4,-1,2,1,-5,4]

b=[]
max_sum = float('-inf')
for i in range(len(arr)):
    sum = arr[i]
    max_sum=max(max_sum,sum)
    for j in range(i+1,len(arr)):
        sum += arr[j]
        max_sum=max(max_sum,sum)
print(max_sum)
  
#Kadane’s Algorithm (Maximum Subarray Sum)