#Declare your height as a integer variable
age_integer = 24
print(age_integer)
print(type(age_integer))

#Declare your height as a float variable
height_float = 179.5
print(height_float)
print(type(height_float))

#Declare a variable that store a complex number
number_data = complex(3, 4)
print(number_data)

#Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle
base_triangle = float(input("Enter the base : "))
height_triangle = float(input("Enter the height : "))
#calculate area of the triangle
area = 0.5 * base_triangle * height_triangle
print("The area of the triangle is : ", area)


#Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle
side_a = int(input("Enter side a : "))
side_b = int(input("Enter side b : "))
side_c = int(input("Enter side c : "))
#calculate perimeter of the triangle
perimeter_of_all_sides = side_a + side_b + side_c
print("The Perimeter of all the sides are : ", perimeter_of_all_sides)


#Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length_rectangle = int(input("Enter the length of rectangle : "))
width_rectangle = int(input("Enter the width of rectangle : "))
#calculate the area and perimeter of the rectangle 
area_of_rectangle = length_rectangle * width_rectangle
perimeter_rectangle = 2 *(length_rectangle + width_rectangle)
print("The area of rectangle is : ", area_of_rectangle)
print("The perimeter of rectangle is : ", perimeter_rectangle)


#Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
pi = 3.14
radius = float(input("Enter the radius of the circle : "))
#Calculate area and circumference of the circle 
area_of_circle = pi * radius * radius
circumference_of_circle = 2 * pi * radius
print("The area of the circle is : ", area_of_circle)
print("The Circumference of the circle is : ", circumference_of_circle)


#Calculate the slope, x-intercept and y-intercept of y = 2x -2
intercept_x = int(input("Enter the intercept of x : "))
#y=2x - 2 is the formula being used here
intercept_y = 2 * intercept_x - 2
print("The Slope value is : ", intercept_y)


#Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
import math

# Define the coordinates of the two points
x1, y1 = 2, 2
x2, y2 = 6, 10

# Calculate the slope using the formula m = (y2 - y1) / (x2 - x1)
slope = (y2 - y1) / (x2 - x1)

# Calculate the Euclidean distance using the formula d = sqrt((x2 - x1)^2 + (y2 - y1)^2)
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Print the results
print("Slope:", slope)
print("Distance:", distance)
