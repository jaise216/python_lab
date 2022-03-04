a = int(input("enter the first number:"))
b = int(input("enter the second number:"))
ope = input("enter the operator of the operation to be performed:")
if ope == "+":
    print("the sum is:", a+b)
elif ope == "-":
    if a >= b:
        print("the difference is:", a-b)
    else:
        print("the difference is:", b-a)
elif ope == "*":
    print("the product is:", a*b)
elif ope == "/":
    print("the quotient is:", a/b)
else:
    print("enter the correct operator")
