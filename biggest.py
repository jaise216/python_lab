a = int(input("enter first number:"))
b = int(input("enter second number:"))
c = int(input("enter third number"))
if a > b and a > c:
    print("the biggest number is:", a)
elif b > a and b > c:
    print("the biggest number is", b)
else:
    print("the biggest number is:", c)
