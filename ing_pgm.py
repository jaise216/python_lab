def ing(s):
    if s.endswith("ing"):
        s = s + "ly"
    else:
        s = s + "ing"
    print(s)


str1 = input("enter a string:")
ing(str1)
