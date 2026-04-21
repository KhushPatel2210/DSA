prices = [7,1,5,3,6,4]

time= float('-inf')
b=[]
max_no=0
for i in range(0,len(prices)):
    for j in range(i+1,len(prices)):
        best=prices[j]-prices[i]
        if best>max_no:
            max_no=best

if max_no==0:
    print("there is no best time to pass buy the stock")
else:
    print(max_no)
            

