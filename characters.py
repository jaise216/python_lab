str1 = input("enter a string: ")
str1 = str1.lower()
str2 = set(str1)
print("the characters and its count are")
for i in str2:
    count = 0
    for j in range(0, len(str1)):
        if i == str1[j]:
            count = count + 1
    print(i, "-", count)
