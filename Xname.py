#!C:\Python27\python.exe
'''
CS1114


Name: Glenn Pantaleon
Username: gpanta01@students.poly.edu

Purpose of this program: To create a box around a name or phrases

constraints: yes

'''

def lineOfXs (totalOfXs):
    ''' Creates a line consisting of X's.'''
    print'X'*totalOfXs

def spaceOfXs (totalOfSpaces):
    ''' Forms a space between two X's at each end.'''
    print'X'+' '*totalOfSpaces+'X'

def phraseInX (phrase):
    ''' Displays a name between the X's at each end.'''
    print 'X  '+ phrase + '  X'


def main():
    lineOfXs(12)
    spaceOfXs(10)
    phraseInX ('Glenn ')
    phraseInX ('  is  ')
    phraseInX ('Great ')
    spaceOfXs(10)
    lineOfXs(12)

if __name__== '__main__' :
    main()
    
