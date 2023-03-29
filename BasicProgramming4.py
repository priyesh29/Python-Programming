import keyword

print("The list of keywords in Python are :")

#printing all keywords at once using "kwlist"
print(keyword.kwlist)


#Print first name, last name and full name as the value
first_name = 'Priyesh'
last_name = 'Kumar'
fullName = first_name + last_name
print("\nThe Full Name is : ", fullName)

#Print number, first name, last name, personal information as the values 
number = 10
first_name = 'Eric'
last_name = 'Cantona'
num1 = 2
num2 = 4
person_info = {
   'firstname':'Priyesh',
   'lastname':'Kumar',
   'country':'India',
   'city':'Mumbai'
   }

print("Personal information : ", person_info)
print(num1, num2)
print(first_name, last_name)


#list literal
fruits = ["apple", "mango", "orange"] 
print(fruits)

#type function is used to know which class a variable or a value belongs to 
print(type(fruits))

#[]indexing is used to find the position of the items inside a variable
print(fruits[0])
print(fruits[2])

#tuple literal
numbers = (1, 2, 3) 
print(numbers)
print(type(numbers))
print(numbers[1])

#dictionary literal
alphabets = {'a':'apple', 'b':'ball', 'c':'cat'} 
print(alphabets)
print(type(alphabets))

#set literal
vowels = {'a', 'e', 'i' , 'o', 'u'} 
print(vowels)
print(type(vowels))

#string literal
strings = 'Eric'
print(strings)
print(type(strings))
print(strings[1])


num1 = 5
print(num1, 'is of type', type(num1))
num2 = 2.0
print(num2, 'is of type', type(num2))


#int to float
num_int = 10
print('num_int',num_int)      
num_float = float(num_int)
print('num_float:', num_float)   

#float to int
gravity = 9.81
print(int(gravity))            

#int to str
num_int = 10
print(num_int)                 
num_str = str(num_int)
print(num_str)               

#str to int or float
num_str = 10.6
print('num_int', int(num_str))    
print('num_float', float(num_str))  

#str to list
first_name = 'Usha'
print(first_name)               
first_name_to_list = list(first_name)
print(first_name_to_list) 


