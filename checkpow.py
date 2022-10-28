n = int(input("Enter a number ")) 
num = n
if (n==0):
    print(num,"not a power of 2", sep=" ")
else:
    while (n!=1):
        if (n%2!=0):
            print(num,"is not a power of 2", sep = " ")
            break
        n = n//2
    else:
        print(num,"is a power of 2", sep = " ")