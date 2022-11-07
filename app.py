print('''		|----------------------------------|	
			Calculator Made by
	 		 H I T M A N#1403
	 |----------------------------------|	''')

num1 = float(input('Enter the first number here: '))
num2 = float(input('Enter the second number here: '))

operator1 = '+'
operator2 = '-'
operator3 = '*'
operator4 = '/'

operator_options = input("Select the operator for the calculation: ")

def addition():
	if operator_options == operator1:
		print('The solution for adding num1 and num2 is', num1 + num2)
	elif operator_options != operator1:
		print('Addition: NA')
addition()

def subtraction():
	if operator_options == operator2:
		print('The solution for subtracting num1 and num2 is', num1 - num2)
	elif operator_options != operator2:
		print('Subtraction: NA')
subtraction()

def multiplication():
	if operator_options == operator3:
		print('The solution for multiplication for num1 and num2 is', num1 * num2)
	elif operator_options != operator3:
		print('Multiplication: NA')
multiplication()

def divide():
	if operator_options == operator4:
		print('The solution for divide for num1 by num2 is', num1 / num2)
	elif operator_options != operator4:
		print('Divide: NA')
divide()
