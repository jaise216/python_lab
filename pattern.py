for i in range(5):
    s = ""
    for j in range(5):
        if j <= i:
            s = s + "*"
    print(s)
for i in range(1, 6):
    s = ""
    for j in range(5, 0, -1):
        if j > i:
            s = s + "*"
    print(s)
