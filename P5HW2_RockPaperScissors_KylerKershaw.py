# This program is a game of rock, paper, scissors.
# 11/11/2018
# CTI-110 P5HW2 - Rock, Paper, Scissors Game
# Kyler Kershaw
#

# Generate a random number between 1 and 3 (including 1 and 3)
# Assign the number to either Rock, Paper, or Scissors.
# Have the user input their number (1-3 corresponds to computer's assignments)
# Display the computer and user choices.
# Declare a winner based on rock, paper, scissors rules.
# If there is a draw, force a rematch.
import random

def main():
    # Create a variable to control the loop.
    play_again = 'y'

    # Begin the game loop.
    while play_again == 'y' or play_again == 'Y':

        # Randomly make computer selection
        comp_number = random.randint(1,3)

        # Assign the computer's selection to the proper name.
        comp_choice = assign_comp_choice(comp_number)

        # Ask user for their choice.
        player_number = int(input('Make your selection...Rock(1), Paper(2), or Scissors(3)'))
        player_choice = assign_player_choice(player_number)

        # Display the selections.
        print('You chose... ', player_choice)
        print('I chose... ', comp_choice)

        # Determine the winner.
        find_winner(player_choice, comp_choice)

        # Ask the user to play again
        if player_choice == comp_choice:
            print('Rematch!')
            play_again = 'y'
        else:
            play_again = input('Would you like to play again? Enter y for yes.')


    # Game over prompt.
    else:
        print('G A M E  O V E R')

            
        
# The assign_comp_choice function takes the computer's random number
# and assigns it the corresponding selection from rock, paper, or scissors.
def assign_comp_choice(comp_number):
    # Assign names for computer choices.
    if comp_number == 1:
        comp_choice = 'rock'
    elif comp_number == 2:
        comp_choice = 'paper'
    else:
        comp_choice = 'scissors'
    return comp_choice


# The assign_player_choice function takes the players number input
# and assigns it the corresponding selection from rock, paper, or scissors.
def assign_player_choice(player_number):
    # Loop to make sure players selection is within limits. 
    while player_number > 3 or player_number < 1:
        print('That was not a valid selection.')
        player_number = int(input('Please make your selection...Rock(1), Paper(2), or Scissors(3)'))

    # Assign names for player choices.
    else:
        if player_number == 1:
            player_choice = 'rock'
        elif player_number == 2:
            player_choice = 'paper'
        else:
             player_choice = 'scissors'
    return player_choice


# The find_winner function looks at the results of the game
# and determines if there is a winner.
def find_winner(player_choice, comp_choice):
    # In the event of a draw.
    if player_choice == comp_choice:
        print("It's a draw!")

    # Rock outcome
    elif player_choice == 'rock' and comp_choice == 'paper':
        print('You lose!')

    elif player_choice == 'rock' and comp_choice == 'scissors':
        print('You win!')


    # Paper outcome.
    elif player_choice == 'paper' and comp_choice == 'scissors':
        print('You lose!')

    elif player_choice == 'paper' and comp_choice == 'rock':
        print('You win!')


    # Scissors outcome.
    elif player_choice == 'scissors' and comp_choice == 'rock':
        print('You lose!')

    elif player_choice == 'scissors' and comp_choice == 'paper':
        print('You win!')


#Calling main
main()
