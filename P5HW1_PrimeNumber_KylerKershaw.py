# This program gets a number from the user and determines if it is prime or not.
# 11/11/2018
# CTI-110 P5HW1 - Prime Numbers
# Kyler Kershaw
#

# Get a number from the user.
# Find out if that number is prime or not using the remainder operator.
# Display whether or not the number is prime.
import math

# Main function.
def main():
    # Get a number from the user.
    number = int(input('Enter a number and I will see if it is a prime number: '))
    # Use a boolean to determine if the number is prime.
    # True is prime.
    # False is not prime.
    if is_prime(number): 
        print('The number is prime.')
    else:
        print('The number is not prime.')


def is_prime(number):
    if number > 1:
        # Check for factors
        for i in range (2, number):
            if (number % i)== 0:
                status = False # If a factor is found, the Boolean is returned as false.
                break
        else:
            status = True #If the boolean finds no factors, the Boolean is returned as true.
    else:
        status = False
    return status #This returns either true or false.

#Calls the main function
main()
