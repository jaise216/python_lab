year = int(input("enter current year:"))
limit = int(input("enter the limit you want:"))
for yr in range(year, limit):
    if (yr % 4 == 0 and yr % 100 != 0) or (yr % 400 == 0):
        print(yr)
