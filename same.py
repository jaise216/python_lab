l1 = []
l2 = []
l3 = []
s1 = 0
s2 = 0
n = int(input("enter the range of first list"))
m = int(input("enter the range of second list"))
print("enter values to first list")
for i in range(0, n):
    l1.append(int(input()))
    s1 = s1 + l1[i]
print("enter values to second list")
for i in range(0, m):
    l2.append(int(input()))
    s2 = s2 + l2[i]
for i in range(0, n):
    for j in range(0, m):
        if l1[i] == l2[j]:
            l3.append(l1[i])
if len(l1) == len(l2):
    print("they have same length")
else:
    print("they have different length")
if s1 == s2:
    print("their sums are equal")
else:
    print("their sums are not equal")
print("common elements are:", l3)
