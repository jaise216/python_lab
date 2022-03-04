import math
l1 = []
start = int(input("enter the first four digit number:"))
end = int(input("enter the last four digit number:"))
for j in range(start, end, 1):
    i = str(j)
    c = 0
    for k in i:
        dig = int(k)
        if dig % 2 == 1:
            c = 1
            break
    if c == 0:
        sq = math.sqrt(j)
        sq = math.trunc(sq)
        if (sq * sq) == j:
            l1.append(j)
print(l1)
