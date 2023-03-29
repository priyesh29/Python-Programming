#assign a variable first name 
#assign a variable last name
#assign a variable to find country, city, age, date of birth
#find len of first name and last name
#use type function (built in function) to know data type
#find indexing of first name and last name


first_name = "Usha"
last_name = "Ahirwar"
country = "India"
city = "New Delhi"
age = 24
date_of_birth = 1999
is_married = False

first_name, last_name, country = "Usha", "Ahirwar", "India"
x, y, z = 1, 2, 3

personal_information = date_of_birth 

print("Full Name is : ", first_name + " " + last_name)
print(len(first_name))
print(len(last_name))
print(first_name[2])
print(last_name[0])
print("\nCountry and City are : ", country + " " + city)
print("\nDate of Birth is : ", personal_information)
print(type(personal_information))
print("\nAge is :", age)
print(type(age))
print(first_name, last_name, country)
print(x, y, z)


#declaration and initialization of values assigned to variables num_one and num_two
#Floor division is a mathematical operation in Python (and many other programming languages) that performs division between two numbers and returns the quotient rounded down to the nearest integer
num_one = 5
num_two = 4

#functions used to add, subtract, multiply, divide, floor division, Modulus & power of numbers
num_add = num_one + num_two
num_subtract = num_one - num_two
num_product = num_one * num_two
num_divide = num_one / num_two
num_calculate_power = num_one ** num_two
num_floor_division = num_one // num_two
num_modulus = num_one % num_two

#print the output of the above functions
print("The Sum of two Numbers is : ", num_add)
print(type(num_add))

print("\nThe Subtraction of two Numbers is : ", num_subtract)
print(type(num_subtract))

print("\nThe Product of two Numbers is : ", num_product)
print(type(num_product))

print("\nThe Division of two Numbers is : ", num_divide)
print(type(num_divide))

print("\nThe Power of two Numbers is : ", num_calculate_power)
print(type(num_calculate_power))

print("\nThe Floor Division of two Numbers is : ", num_floor_division)
print(type(num_floor_division))

print("\nThe Modulus of two Numbers is : ", num_modulus)
print(type(num_modulus))

