"""
File: extension3_triangular_checker.py
Name:
--------------------------
This program asks our user for input and checks if the input is an
triangular number or not.

The triangular number (Tn) is a number that can be represented in the form of a triangular
grid of points where the first row contains a single element and each subsequent row contains 
one more element than the previous one.

We can just use the fact that the nth triangular number can be found by using a formula: Tn = n(n + 1) / 2.

The program ends when the user enter the EXIT number.
"""

EXIT = -1
def main():
    """
    To do:
    """
    print('Welcome to the triangular number checker!')
    while True:
        num = int(input('n:'))
        a = 0
        b = 0
        if num == -1:
            print('have a good one!')
            break
        else:
            while num > b:
                b = a + b
                a += 1
            if b == num:
                print(str(num)+' is a triangular number')
            else:
                print(str(num)+' is not a triangular number')
    pass


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
