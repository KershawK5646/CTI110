# This program will convert a given distance from Kilometers to miles.
# 11/11/2018
# CTI-110 P5T1_KilometerConverter
# Kyler Kershaw
#

# Ask user for input in Kilometers.
# Convert Kilometers to Miles. (Miles = Kilometers * 0.6214)
# Display the distance in miles.

CONVERSION_FACTOR = 0.6214

# Define the main function.
def main():
    
    # Get the distance in Kilometers.
    kilometers =float(input('Enter the distance in kilometers: '))
    # Display the distance converted to miles
    show_miles(kilometers)


def show_miles(km):

    # Calculate miles.
    miles = km * CONVERSION_FACTOR
    # Display the miles.
    print(format(km, ',.2f'),'kilometers equals', format(miles,',.2f'), 'miles.')


# Calls the main function.
main()
