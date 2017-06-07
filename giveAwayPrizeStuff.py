'''

cs1114 

Submission: rec07

Programmer: Glenn Pantaleon
Username: gpanta01@students.poly.edu

Purpose of program: To generate a prize system based on the number of
dollars, quarters, dimes, and pennies.

constraints: none
assumptions: none


'''

import random
import colourStuff



def giveAwayPrize(dollars,quarters,dimes,pennies):
    '''Gives away prizes.'''

    if dollars == 1 and quarters == 0 and dimes == 1 and pennies == 3:
        return "You won the Grand Prize! A(n) " + colourStuff.pickRandomColors()+ " T SHIRT !"

    
    elif (dollars == 2 or dollars == 3 and quarters == 2 or quarters == 1 \
         and dimes and pennies == 4 or pennies == 2):
        return "You won the Second Prize! You got 17 cents."

    elif dollars and quarters and dimes and pennies in range(7,11):
        return "You won the Thrid Prize! You got 3 cents."

    else:
        return "You won the Consolation Prize! You got 2 cents."


    
