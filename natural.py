n = int(input("enter the limit:"))
l1 = []
for i in range(n):
    l1.append(i)
l2 = [i*i for i in l1]
print(l1)
print("squares are:", l2)
