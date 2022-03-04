class Rectangle:
    def __init__(self, l, w):
        self.__length = l
        self.__width = w
        self.area = self.__width * self.__length

    def __lt__(self, other):
        if self.area < other.area:
            print("area of second rectangle is greater")
        elif other.area < self.area:
            print("area of first rectangle is greater")
        else:
            print("They have equal area!")


l1 = float(input("Enter length of 1st rectangle: "))
w1 = float(input("Enter width of 1st rectangle: "))
R1 = Rectangle(l1, w1)
l1 = float(input("Enter length of 2nd rectangle: "))
w1 = float(input("Enter width of 2nd rectangle: "))
R2 = Rectangle(l1, w1)
res = R1 < R2
