"""
File: extension1_factorial.py
Name: 
-------------------
This program will continually ask our user to give a number
and will calculate the factorial result of the number and print it on the console.

The program ends when the user enter the EXIT number.
"""


def main():
	print('Welcome to stanCode factorial master!')
	while True:
		a = 1
		total = 1
		num = int(input('Give me a number,and I will list the answer of factorial: '))
		if num >= 1:
			for i in range(num):
				total = a * total
				a += 1
			print('Answer: ' + str(total))
		else:
			print('- - - - - - See ya!-------------')
			break
	pass




# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
	main()