l1 = []
n = int(input("enter the limit: "))
print("enter the numbers:\n")
for i in range(0, n):
    l1.append(int(input()))
print("created list is: ", l1)
l2 = [i for i in l1 if i % 2 != 0]
print("list after the deletion of even numbers: ", l2)
