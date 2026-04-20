n=113

counter = 0
for i in range(1,n+1):
    if n%i==0:
        counter += 1
    
if counter>2:
    print("not a prime number")
else:
    print("it is a prime number")
