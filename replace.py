w = input("enter a word:")
print("string before replacement:", w)
c = w[0]
w = w.replace(c, '$')
w = c+w[1:]
print("string after replacement:", w)
