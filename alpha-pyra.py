n = int(input("Enter a number: "))
a = 65
i = 0
while i<n:
    j=0
    while j<(n-i):
        print(chr(a+i+j), end = " ")
        j+=1
    i+=1
    print()