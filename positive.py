n = int(input("enter the limit:"))
print("enter the numbers:")
l1 = []
for i in range(n):
    l1.append(int(input()))
print(l1)
l2 = [i for i in l1 if i > 0]
print("positive numbers are:", l2)
