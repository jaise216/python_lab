x = lambda l, b: l * b
y = lambda l, b: 0.5 * b * l
l1 = int(input("enter the length of rectangle:"))
b1 = int(input("enter the breadth of rectangle:"))
print("area of rectangle is:", x(l1, b1))
s1 = int(input("enter the side of square:"))
print("area of square is:", x(s1, s1))
b2 = int(input("enter the breadth of triangle:"))
l2 = int(input("enter the length of triangle:"))
print("area of triangle is:", y(l1, b1))
