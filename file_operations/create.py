# f=open("file.txt","w")
# f.close()

f=open("file.xlsx","a")
f.write("\n hello this is the four line of the file")
f.close()

f=open("file.txt","r")
print(f.read())