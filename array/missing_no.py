a=[1,2,4,5,6,7]

for i in range(len(a),1,-1):
    k = a[i-1]-a[i-2]
    if k==1:
        continue
    else:
        print(a[i-2]+1)
        break