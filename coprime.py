#Method-1 Using Nexted loops

a = int(input("Enter first input: "))
b = int(input("Enter second input: "))
i=1
while i<=a:
    if a%i==0 and b%i==0:
        hcf = i
    i+=1
if hcf==1:
    print(a,b," are co-prime")
else:
    print(a,b," are not co-prime")

#Method-2 Using math module

x = int(input("Enter first input: "))
y = int(input("Enter second input: "))
import math 
if math.gcd(x, y) == 1:
    print(x,y, " are co-prime")
else:
    print(x,y, " are not co-prime")