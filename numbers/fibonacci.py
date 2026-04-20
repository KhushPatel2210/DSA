given_no =5

a=0
b=1

n=10
count=0
f=[]
while count<n :
    print(a)
    f.append(a)
    a,b = b,a+b
    count += 1
print(f)

status = False

for i in f :
    if given_no == i :
        print("this number is the fibonaccie number")
        status = True
        break
if(status==False):
    print("given number is not the fibonacci number")