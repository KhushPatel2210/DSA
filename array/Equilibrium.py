# arr = [1,3,5,2,2]
# arr = [1, 3, 5, 4, 2, 2]
arr = [2, 0, 0, 0]

sum_right=0
sum_left=0
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        sum_right+=arr[j]
    r=sum_right    
    # print(sum_right)
    sum_right=0
    for k in range(i-1,-1,-1):
        sum_left+=arr[k]
    l=sum_left   
    # print(sum_left)
    sum_left=0

    if r==l:
        print("i of the index",i)



