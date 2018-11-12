# This program simulates the toss of a coin 10 times.

import random

# Constants
HEADS = 1
TAILS = 2
TOSSES = 10

def main():
    for toss in range(TOSSES):
        # Simulate the coin toss.
        if random.randint(HEADS, TAILS) == HEADS:
            print('Heads')
        else:
            print('Tails')

# Call the main function.
main()
