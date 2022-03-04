n = int(input("enter a number: "))
for i in range(1, n + 1):
    s = ""
    c = 1
    for j in range(c, i + 1):
        s = s + str(i * j) + " "
    print(s)
