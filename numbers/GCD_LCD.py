import math 

#inbuild method
print(math.gcd(60,80))
print(math.lcm(60,80))

a=500
b=80

# for gcd
while b != 0 :
    a , b = b,a%b
print(a)

