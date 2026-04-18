# does array is already sorted or not 

a=[1,2,3,4,1]
sort = "true"

for i in range(0,len(a)-1):
    if a[i]>a[i+1]:
        print("array is not sorted")
        sort= "false"
        break

if sort=="true":
    print("array is sorted")