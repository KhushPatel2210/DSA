a=[2,6,35,2,64,29,64,2]

does_exists = 2
count = 0
for i in a :
    if i==does_exists:
        # print("exists")
        count += 1

      
    else:
        # print("false")
        count += 0

if count == 0:
    print("does not exist")
else:
    print("exist")
    print(count)  