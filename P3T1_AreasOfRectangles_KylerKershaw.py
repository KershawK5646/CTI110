# This program will determine which rectangle between two has the greater area.
# 10/6/2018
# CTI-110 Tutorial 1 - Areas Of Rectangles
# Kyler Kershaw
#

# Pseudocode:
# Input the dimensions of rectangle 1
# Input the dimensions of rectangle 2
# Calculate the areas of both rectangles
# If Area1 > Area2
#   Display "Rectangle one is larger."
# else if Area2 > Area1
#   Display "Rectangle two is larger."
# else Area1 == Area2
#   Display "These two are the same size."


# This block has the user enter the dimensions of the rectangles.
length1 = int(input('Enter the length of the first rectangle: '))
width1 = int(input('Enter the width of the first rectangle: '))
length2 = int(input('Enter the length of the second rectangle: '))
width2  = int(input('Enter the width of the second rectangle: '))

# This calculates the areas of both rectangles.
area1 = length1*width1
area2 = length2*width2

#Testing the math and inputs:
#print(area1)
#print(area2)

#Determining which rectangle has the greater area.
if area1 > area2:
    print('Rectangle 1 has the greater area.')
elif area2 > area1:
    print('Rectangle 2 has the greater area.')
else:
    print('Both rectangles have the same area.')

