'''

cs1114 

Submission: rec07

Programmer: Glenn Pantaleon
Username: gpanta01@students.poly.edu

Purpose of program: To pick colors out of random 

constraints: none
assumptions: none


'''

import random



def pickRandomColors():
    '''Returns random colors through a number value.'''
    randomColors= random.randint(1,8)

    if randomColors == 1:
        return "Red"

    elif randomColors == 2:
        return "Orange"

    
    elif randomColors == 3:
        return "Yellow"


    elif randomColors == 4:
        return "Green"

    elif randomColors == 5:
        return "Blue"

    elif randomColors == 6:
        return "Indigo"


    elif randomColors == 7:
        return "Violet"

    else:
        return "Black"
