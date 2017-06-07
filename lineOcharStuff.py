'''
cs1114

Submission: lineOcharStuff.py

Programmer: Glenn Pantaleon
Username:  gpanta01@students.poly.edu

Purpose of program: Draws Lines

constraints: none
assumtions: none

linOcharStuff module

'''



def drawsLine(lineLength,optionLineStyle= 'X'):
    '''Draws a line with a linestyle.'''
    print lineLength*optionLineStyle
    

def spacingLine(amountOfSpace,lineStylePointOne = 'X',lineStylePointTwo = 'X'):
    '''Displays a space between line style endpoints.'''
    print lineStylePointOne+' '*amountOfSpace+lineStylePointTwo
    

def displayCharacter (lineCharacter,endLineStyleOne = 'X',endLineStyleTwo = 'X'):
    '''Displays a character between the line style endpoints.'''
    print endLineStyleOne+' '+lineCharacter+' '+endLineStyleTwo


def blankLine():
    '''Creates a blank line and moves cursor on the next line.'''
    print
    
