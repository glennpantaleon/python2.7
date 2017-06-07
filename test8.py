







def askUserFirstName():
    '''Gets the user's first name.'''
    first_name = raw_input("What is your first name? ")
    return first_name

def askUserLastName():
    '''Gets the user's last name.'''
    last_name = raw_input("What is your last name? ")
    return last_name

def sketchLineOfXs(totalOfX):
    '''Displays a line of X's as a box base '''
    print 'X'*totalOfX

def displaySpaceLine(totalOfSpace):
    '''Displays two X's on a line with a space in between'''
    print 'X'+' '*totalOfSpace+'X'
    

def displayCharatOnX(first_name, last_name):
    '''Displays a character bewteen X'''
    print 'X '+ str(first_name,last_name) + ' X'
    

def pauseInitials():
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


    

def main():
    first_name = askUserFirstName()
    last_name = askUserLastName()
    sketchLineOfXs(9)
    displaySpaceLine(7)
    displayCharatOnX(first_name)
    displaySpaceLine(7)
    sketchLineOfXs(9)
    
    sketchLineOfXs(13)
    displaySpaceLine(11)
    displayCharatOnX(last_name)
    displaySpaceLine(11)
    sketchLineOfXs(13)
    pauseInitials()
    
    
if __name__== '__main__' :
    main()
    
