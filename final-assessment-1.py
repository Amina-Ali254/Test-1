# 1. Explain five application of python?
    # a) Data science
    # b) 
    # c) 
    # d) 
    # e) 

# 2. Give and explain five examples of datatypes?
    # a) string
    # b) 
    # c) list
    # d) interger
    # e) float

# 3. Give four variables nameing rules and their examples?
    # a) 
    # b) 
    # c)
    # d)

# 6. Create a function named multiply_numbers that takes three parameters and returns their product
def multiply_numbers (a, b, c):
    return a * b * c
result = multiply_numbers (5, 6 ,2)
print (result)

# 7. Create a Python program to print the perimeter of a triangle, get the length of the sides from the user using input using variables.
# Formula - perimeter = add all sides (3) = a + b + c
def calculate_perimeter(a, b, c):
    return a + b + c
side_a = float(input("Enter the length of the first side: "))
side_b = float(input("Enter the length of the second side: "))
side_c = float(input("Enter the length of the third side: "))
perimeter = calculate_perimeter(side_a, side_b, side_c)
print(perimeter)

# 8. Create a Python program using functions to calculate the area of a circle.
# Formula - area = 3.142 * radius * radius
def calculate_circle_area(radius):
    return 3.142 * radius * radius
radius = float(input("Enter the radius of the circle: "))
area = calculate_circle_area(radius)
print(f"The area of the circle is: {area}")

# 9. Create a Python program using functions to calculate the area of a triangle.
# Formula - area = 0.5 * base * height
def calculate_triangle_area(base, height):
    return 0.5 * base * height
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area = calculate_triangle_area(base, height)
print(f"The area of the triangle is: {area}")

# #  10. Create a Python program using functions to calculate the area of a rectangle.
def calculate_rectangle_area(length, width):
    return length * width
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = calculate_rectangle_area(length, width)
print(f"The area of the rectangle is: {area}")
