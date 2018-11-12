# This program demonstrates a bad local veriable.
# Define the main function.

def main():
    get_name()
    print('Hello', name) # This causes an error!

# Definition of the get_nanme function.
def get_name():
    name = input('Enter your name: ')

# Call the main function.
main()
