"""
File: extension2_number_checker.py
Name:
------------------------
This program asks our user for input and checks if the input is a
perfect number、deficient number or an abundant number.

A number is said to be perfect if it is equal to the sum of all its
factors (for obvious reasons the list of factors being considered does
not include the number itself).

A number is considered to be abundant if the sum of its factors
(aside from the number) is greater than the number itself.

And a number is said to be deficient if it is bigger than the sum of all its
factors(aside from the number itself).

The program ends when the user enter the EXIT number.
"""

EXIT = -1
def main():
    """
    TODO:
    """
    print('Welcome to the number checker!')
    while True:
        num = int(input('n:'))
        a = 1
        total = 0
        if num == -1:
            print('Have a good one')
            break
        else:
            for i in range(num-1):
                if num%a==0:
                   total+=a
                a = a+1

        if num == total:
            print(str(num) +' is a perfect number')

        elif num>total:
            print(str(num)+' is a abundant number')

        else:
            print(str(num)+' is a deficient number')
    pass
# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
