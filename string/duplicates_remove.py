a="abcabcabcabcabad"

unique = ""
duplicate = ""

for i in a :
    if i not in unique:
        unique += i
    else:
        if i not in duplicate:
            duplicate += i
    
print(unique)
print(duplicate)

