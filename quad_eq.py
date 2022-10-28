import math
A = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))
dis = ((b**2) - (4*A*c))
if (dis>0):
    print("Real and distinct roots")
    root1 = (-b + math.sqrt(dis))/(2*A)
    root2 = (-b - math.sqrt(dis))/(2*A)
    print("The roots are", root1, "and", root2, sep = " ")
elif (dis==0):
    print("Real and equal roots")
    root1 = root2 = (-b)/(2*A)
    print("The roots are", root1, "and", root2, sep = " ")
else:
    print("Imaginary roots")
    real = (-b)/(2*A)
    img = (math.sqrt(-dis))/(2*A)
    print("The roots are", round(real,3),"+",round(img,3), "and", round(real,3),"-",round(img,3) , sep = " ")