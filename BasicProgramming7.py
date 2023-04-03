#Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?

hours_pay = float(input("Enter the hours per pay : "))
rate_pay = float(input("Enter the rate per hour : "))

pay_person = hours_pay * rate_pay

print("Pay : $", str(pay_person))
