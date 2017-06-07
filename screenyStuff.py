'''
cs1114

Submission: screenyStuff.py

Programmer: Glenn Pantaleon
Username:  gpanta01@students.poly.edu

Purpose of program: clears and pauses the screen

constraints: none
assumtions: nonne

screenyStuff module

'''

def clearScreen():
    '''Clears the Screen.'''
    print '[---screen is clear here---]'
    

    
def askUserFirstName():
    '''Ask user's first name.'''
    first_name = raw_input("What is your first name?\n")
    return first_name


def askUserLastName():
    last_name = raw_input("What is your last name?\n")
    return last_name





def pauseScreen():
    '''Programmer credits himself by displaying his initials'''
    raw_input('''\nThanks for using my wonderful program.
BTW : I'm:\n\n\n
GGGGGGGGGGGGG       PPPPPPPPPPPPP
GGGGGGGGGGGGG       PPPP      PPP
GGGG                PPPP      PPP
GGGG                PPPP      PPP
GGGG     GGGG       PPPPPPPPPPPPP
GGGG      GGG       PPPP
GGGG      GGG       PPPP
GGGGGGGGGGGGG       PPPP
GGGGGGGGGGGGG       PPPP                waiting for that any key...''')
