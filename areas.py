from graphics.threeDgraphics import cuboid
from graphics.threeDgraphics import sphere
import graphics.rectangle
import graphics.circ
print("RECTANGLE")
l = int(input("Enter length "))
b = int(input("Enter breadth "))
graphics.rectangle.rectangle(l, b)
print("CIRCLE")
r = int(input("Enter radius "))
graphics.circ.circle(r)
print("CUBOID")
l = int(input("Enter length "))
w = int(input("Enter width "))
h = int(input("Enter height "))
graphics.threeDgraphics.cuboid.cuboid(l, w, h)
print("SPHERE")
r = int(input("Enter radius "))
graphics.threeDgraphics.sphere.sphere(r)
