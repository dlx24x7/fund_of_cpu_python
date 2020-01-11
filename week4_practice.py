"""
Week 4 practice project template for Python Programming Essentials
Rock-paper-scissors-lizard-Spock
"""

import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
    
def name_to_number(name):
    """
    Given string name, return integer 0, 1, 2, 3, or 4 
    corresponding to numbering in video
    """
    # convert name to number using if/elif/else
    # don't forget to return the result!
    if name == "rock":
        choice = 0
    elif name == "Spock": 
        choice = 1
    elif name == "paper":
        choice = 2
    elif name == "lizard":
        choice = 3
    elif name == "scissors": 
        choice = 4
    else: 
        print("Error: that is an invalid choice")
        return
    return choice
    
def number_to_name(number):
    """
    Given integer number (0, 1, 2, 3, or 4)
    corresponding name from video
    """
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    if number == 0:
        choice = "rock"
    elif number == 1: 
        choice = "Spock"
    elif number == 2:
        choice = "paper"
    elif number == 3:
        choice = "lizard"
    elif number == 4: 
        choice = "scissors"
    else: 
        print("Error: that is an invalid choice")
        return
    return choice

def rpsls(player_choice):
    """
    Given string player_choice, play a game of RPSLS 
    and print results to console
    """
    
    # print a blank line to separate consecutive games
    print("")
    # print out the message for the player's choice
    print("Player chooses", player_choice)
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    #print("player_number is", player_number)
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,4)
    #print("comp_number is", comp_number)
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    # print out message for computer's choice
    print("Computer chooses", comp_choice) 
    # compute difference of player_number and comp_number modulo five
    difference = (player_number - comp_number) % 5
    #print("The difference is", difference) 
    # use if/elif/else to determine winner and print winner message
    if (difference == 1) or (difference == 2): 
        print("Player wins!") 
    elif (difference == 3) or (difference == 4): 
        print("Computer wins!") 
    else: 
        print("Player and computer tie!") 
    pass
     
    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric

