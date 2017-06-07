'''
cs1114

Submission: boxxyStuff.py

Programmer: Glenn Pantaleon
Username:  gpanta01@students.poly.edu

Purpose of program: Draws Boxes

constraints: none
assumtions: none

boxxyStuff module

'''
import lineOcharStuff

def drawFilledBox(amountInBox):
    '''Draws a filled in box.'''
    lineOcharStuff.drawsLine(amountInBox)
    lineOcharStuff.drawsLine(amountInBox)
    lineOcharStuff.drawsLine(amountInBox)
    lineOcharStuff.drawsLine(amountInBox)


def drawsSpaceBox(amountInBox,areaInBox):
    '''Draws a box with space inside.'''
    lineOcharStuff.drawsLine(amountInBox)
    lineOcharStuff.spacingLine(areaInBox)
    lineOcharStuff.spacingLine(areaInBox)
    lineOcharStuff.spacingLine(areaInBox)
    lineOcharStuff.drawsLine(amountInBox)


def drawsCharBox(amountInBox,areaInBox,charInBox):
    '''Draws a box with character inside.''' 
    lineOcharStuff.drawsLine(amountInBox)
    lineOcharStuff.spacingLine(areaInBox)
    lineOcharStuff.displayCharacter(charInBox)
    lineOcharStuff.spacingLine(areaInBox)
    lineOcharStuff.drawsLine(amountInBox)

    
