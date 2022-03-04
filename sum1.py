s = 0
l1 = []
n = int(input("enter the limit: "))
print("enter the values to the list:\n")
for i in range(0, n):
    j = int(input())
    l1.append(j)
    s = s+j
print("the list is: ", l1, "\nthe sum is: ", s)
