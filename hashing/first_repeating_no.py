arr = [1, 5, 3, 4, 3, 5, 6]
repeat = []

for i in arr:
    if i in repeat:
        print("your repeating element is",i)
        break
    repeat.append(i)
