def fact(x):
    f = 1
    for i in range(x, 1, -1):
        f = f * i
    print("factorial of the number is:", f)


n = int(input("enter a number:"))
fact(n)
