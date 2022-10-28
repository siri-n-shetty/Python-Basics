n = int(input("Enter n: "))
i=1
while i<=n:
    j=1
    while j<=i:
        print(j,end=" ")
        j+=1
    j-=2
    while j>=1:
        print(j,end=" ")
        j-=1
    i+=1
    print()