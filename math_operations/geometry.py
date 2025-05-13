import math
print("geometry module successfully loaded")
def area_of_circle(radius):
    return math.pi * radius * radius
def perimeter(radius):
    return 2*math.pi * radius
def area_of_rectangle(length,width):
    return length * width
def perimeter_of_rectangle(length,width):
    return 2*(length+ width)
def area_of_triangle(base, height):
    return 0.5 * base *height
def perimeter_of_triangle(side1,side2,side3):
    return side1 + side2 +side3