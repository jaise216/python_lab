vow = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
w = input("enter a word:")
l1 = [letter for letter in w if letter in vow]
print(l1)
