def length(l2):
    j = 0
    for word in l2:
        if len(word) > j:
            j = len(word)
    print("the length of longest word is:", j)


l1 = []
n = int(input("enter the number of words : "))
print("enter the words:\n")
for i in range(0, n):
    l1.append(input())
length(l1)
