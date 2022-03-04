class Rect:
    def __init__(self, l, b):
        self.length = l
        self.breadth = b
        self.area = self.breadth * self.length

    def compare(self, other):
        if self.area > other.area:
            print("area of first rectangle is greater")
        else:
            print("area of second rectangle is greater")


l1 = int(input("enter the length of first rectangle "))
b1 = int(input("enter the breadth of first rectangle "))
l2 = int(input("enter the length of second rectangle "))
b2 = int(input("enter the breadth of second rectangle "))
x1 = Rect(l1, b1)
x2 = Rect(l2, b2)
x1.compare(x2)
