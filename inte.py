n = int(input("enter a number: "))
s = 0
for i in range(1, 4):
    c = 1
    for j in range(0, i):
        c = c * n
    s = s + c
print("final result of the form, n+nn+nnn, of the number", n, "is:", s)
