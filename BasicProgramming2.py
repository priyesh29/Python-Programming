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


#Find the length of 'python' and 'dragon' and make a falsy comparison statement.
#assigned variable to value to calculate len using length function
length_python = len('python')
length_dragon = len('dragon')

print('length_python is : ', length_python)
print('length_dragon is : ', length_dragon)

if length_python != length_dragon:
    print("The lengths are not equal.")
else:
    print("The lenghts are equal.")


#Use and operator to check if 'on' is found in both 'python' and 'dragon'
if 'on' in 'python' and 'on' in 'dragon':
    print("'on' is found in both 'python' and 'dragon'")
else:
    print("'on' is not found in both 'python' and 'dragon'")


#Find the length of the text python and convert the value to float and convert it to string
length_python = len('python')
print("The length of the word python is : ", length_python)
float_length = float(length_python)
str_length = str(float_length)
print("The length of the string is : ", str_length)


#Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python
#You can check if a number is even or not using the modulus operator (%)
number = 20
#use of condition using the modulus operator to check if number is even or odd
if number %2 == 0:
    print("The number is even")
else:
    print("The number is odd")


#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
a_value = 7
b_value = 3
#create a variable and use double backward slash for floor division
floor_division = a_value//b_value
print("The floor division is : ", floor_division)

