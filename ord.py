print("enter your first and last name:")
l1 = []
for i in range(2):
    l1.append(input())
l2 = [ord(element)for sub in l1 for element in sub]
print(l2)
