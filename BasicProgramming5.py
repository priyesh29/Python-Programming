#explicit type conversion = manual conversion 
num_string = '12'
num_int = 20

print("Data type of num_string before converting it : ", type(num_string))
num_string = int(num_string)

print("Data type of num_string after converting it : ", type(num_string))

num_sum = num_string + num_int
print("The Sum is : ", num_sum)


#implicit type conversion = automatic conversion
integer_number = 24
floating_number = 12.6
new_number = integer_number + floating_number
print("The New Number is : ", new_number)
print(type(new_number))




