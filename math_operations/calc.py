import arithmetic
import geometry
operation = input("Enter the operation you want to perfrom: ").lower().strip()
if operation == "addition":
    a= int(input("Enter the value of a: "))
    b= int(input("enter the value of b: "))
    sum = arithmetic.add(a,b)
    print(sum)
elif operation == "substraction":
    a= int(input("Enter the value of a: "))
    b= int(input("enter the value of b: "))
    difference = arithmetic.substract(a,b)
    print("difference")
elif operation == "multiplication":
    a= int(input("Enter the value of a: "))
    b= int(input("enter the value of b: "))
    product = arithmetic.product(a,b)
    print(product)
elif operation == "division":
    a= int(input("Enter the value of a: "))
    b= int(input("enter the value of b: "))
    division = arithmetic.divide
    print(division)
elif operation == "power":
    a= int(input("Enter the value of a: "))
    b= int(input("enter the value of b: "))
    power = arithmetic.power(a,b)
    print(power)
elif operation == "circle area":
    radius=int(input("enter the radius: "))
    circleArea = geometry.area_of_circle(radius)
    print(circleArea)
elif operation == "circle perimeter":
    radius=int(input("enter the radius: "))
    circlePerimeter = geometry.perimeter(radius)
    print(circlePerimeter)
elif operation == "rectangle area":
    length=int(input("enter the length: "))
    width =int(input("enter the width: "))
    rectangleArea = geometry.area_of_rectangle(length, width)
    print(rectangleArea)
elif operation == "rectangle perimeter":
    length=int(input("enter the length: "))
    width =int(input("enter the width: "))
    rectanglePerimeter = geometry.perimeter_of_rectangle(length, width)
    print(rectanglePerimeter)
elif operation == "triangle area":
    base = int(input("enter the base: "))
    height =int(input("enter the height"))
    triangleArea = geometry.area_of_triangle(base, height)
    print(triangleArea)
elif operation == "circle area":
    side1 = int(input("enter the side1: "))
    side2 = int(input("enter the side2"))
    side3 = int(input("enter side3"))
    trianglePerimeter= geometry.perimeter_of_triangle(side1,side2,side3)
    print(trianglePerimeter)
else:
    print("operation not found")