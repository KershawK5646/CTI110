# This program will calculate profit for a company from a given percentage.
# 9/20/2018
# CTI-110 P2T1 - Sales Prefiction
# Kyler Kershaw


# This line takes user input after asking for the projected sales for the year.
# It then converts the user input from a string to a flaot.
totalSales = float(input('Enter the projected total sales: '))

# This line calculates the projected profit by finding 23% of the user input (Projected sales).
profitProjection = totalSales*0.23

# This line prints the projected profit.
print('Your projected profit is $',format(profitProjection, ',.2f'))
