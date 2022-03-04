i = int(input("enter the first four digit number:"))
s = str(i)
c = 0
for i in s:
    j = int(i)
    if j % 2 == 1:
        c = 1
        break
    print(j)
