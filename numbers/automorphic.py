def fun(n):
    if n%3==0 and n%5==0:
        print("succes")
    else:
        print("not fit")


def spy(n):
    sum=0
    mul=1
    temp=n
    while temp>0:
        reminder=temp%10
        sum+=reminder
        mul *= reminder
        temp=temp//10
    print(sum)
    print(mul)

    if sum==mul:
        print("number is the spy number")
    else:
        print("number is not a spy number")




a = int(input("please enter the number"))

spy(a)



if a%5==0:
    if a%2==0:
        print("number is not a automorphic number")
    else:
        print("number is a automorphic number")

else:
    print("number is not automorphic number")


