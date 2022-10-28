num1 = int(input("Enter first number: "))
opr = input("Enter the operator(+,-,*,/): ")
num2 = int(input("Enter second number: "))
if opr=="+":
    add = num1+num2
    print(add)
elif opr=="-":
    minus = num1-num2
    print(minus)
elif opr=="x":
    mul = num1*num2
    print(mul)
else:
    div = num1/num2
    print(float(div))