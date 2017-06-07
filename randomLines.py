''' this module contains wacky line drawing and returning functions '''

import random # this could be in the body of makeRandyLine

def makeRandyLine( char1 = 'X', char2 = 'Y', char3 = 'Z' ):
    '''
        returns a line of characters passed in
        char1 is repeated from 3 to 7 times, chosen randomly
        char2 is repeated from 5 to 22 times, chosen randomly
        char3 is repeated from 2 to 14 times, chosen randomly
    '''
    return char1*( random.randomInt( 3, 7 ) ) + \
               char2*( random.randomInt( 5, 22 ) ) + \
               char3*( random.randomInt( 2, 14 ) )

def drawRandyLine( char1 = 'X', char2 = 'Y', char3 = 'Z' ):
    ''' draws a line made from the call to makeRandyLine 
        cursor is taken to the start of the next line
    '''
    print makeRandyLine( char1, char2, char3 )
