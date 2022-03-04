name = input("enter your name:")
m1 = int(input("enter the marks of 1st subject"))
m2 = int(input("enter the marks of 2nd subject"))
m3 = int(input("enter the marks of 3rd subject"))
m4 = int(input("enter the marks of 4th subject"))
m5 = int(input("enter the marks of 5th subject"))
total = m1+m2+m3+m4+m5
per = (total/500)*100
print("name:", name, "\ntotal:", total, "\npercentage:", per)
