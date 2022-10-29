#Sum ofn natural n numbers
n = int(input("Enter number till where sum is to be calculated: "))
sum = 0
i=1
while i<=n:
    sum+=i
    i+=1
print(sum)