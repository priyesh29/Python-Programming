#Arithmetic Operators 

#Operators are special symbols that perform special operations on variables and values.
#Arithmetic operators includes addition, multiplication, subtraction, division, floor division, modulo, power

#2 variables are taken a and b and assigned random values respectively.
a = 10
b = 5

print("Sum : ", a+b)
print(type(a+b))
print("\nSubtraction : ", a-b)
print(type(a-b))
print("\nMultiplication : ", a*b)
print(type(a*b))
print("\nDivision : ", a/b)
print(type(a/b))
print("\nModulo : ", a%b)
print(type(a%b))
print("\nFloor Division : ", a//b)
print(type(a//b))
print("\nPower : ", a**b)
print(type(a**b))


#Assignment Operators 
#Assignment Operators include Addition, Subtraction, Multiplication, Division and Exponent Assignment
a = 10
b = 5

a +=b
print(a)
#output is 15

a -=b
print(a)
#output will be a=15, b=5 i.e = (a - b) (15 - 5) = 10

a *=b
print(a)
#output will be a=10, b=5 i.e = (a * b) (10 * 5) = 50

a /=b
print(a)
#output will be a=50, b=5 i.e = (a / b) (50 / 5) = 10

a **=b
print(a)
#output will be a=10, b=5 i.e = (a ** b) (10 ** 5) = 100000



#Comparison Operator compares two variables and return a boolean result True or False
#declare two variables a and b 
a = 10
b = 5

print('a == b =', a ==b)
print('\na != b =', a !=b)
print('\na > b =', a > b)
print('\na < b =', a < b)
print('\na >= b =', a >= b)
print('\na <= b =', a <= b)


#Logical Operators
#Uses Keyword like and, or, not logical operators
#And - It returns true if both conditions are satisfied
#Or - Returns True if one of the statements are satisfied
#Not - Returns False if none of the statements are satisfied

a = 10
b = 5
c = 6

print((a>b) and (c>b))
print((a<b) and (c<b))
print((a>=b) and (c>=b))
print((a>c) and (c<a))
print((a>c) or (c<a))
print((a>=b) or (b>=c))
print((a<=b) or (b<=c))







