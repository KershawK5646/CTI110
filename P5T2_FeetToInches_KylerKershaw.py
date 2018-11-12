# This program will convert feet to inches.
# 11/11/2018
# CTI-110 P5T2_FeetToInches
# Kyler Kershaw
#

# Get number of feet to turn into inches.
# Calculate number of inches.
# Display number of inches.

INCHES_PER_FOOT = 12

# Define the main function.
def main():
    # Get a number of feet from the user.
    feet = int(input('Enter a number of feet: '))
    # Convert that to inches.
    print(feet, 'equals', format(feet_to_inches(feet), ',.0f'), 'inches')

# Converts feet to inches.
def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT


# Calls the main function.
main()
