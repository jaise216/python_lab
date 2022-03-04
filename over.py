l1 = []
print("enter 5 numbers:")
for i in range(0, 5):
    l1.append(int(input()))
print(l1)
for i in range(0, 5):
    l1[i] = "over"if l1[i] >= 100 else l1[i]
print(l1)
