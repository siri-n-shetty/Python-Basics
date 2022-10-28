#find prime number
x = int(input("Enter a number"))
i=1
count = 0
print("Factor of ",x,":",end=" ")
while i<=x:
    if x%i==0:
        print(i,end=" ")
        count = count + 1
    i = i + 1
print()
if count==2:
    print("It is a prime number")
else:
    print("Not a prime number")