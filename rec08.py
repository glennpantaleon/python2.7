#!C:\Python27\python.exe

'''
cs1114 

Submission: rec08

Programmer: Glenn Pantaleon
Username: gpanta01@students.poly.edu

Purpose of program: To create a stamp dispenser program

constraints: none
assumptions: The user will give valid input that will always be more than or equal to the
amount owed


'''

import stampMachine

STAMP1 = 0.10
STAMP2 = 0.15
STAMP3 = 0.25
MANAGER = "Manager"


def getName():
    ''''''
    name = raw_input("Enter your name: ")
    return name

def managerMenuChoices():
    '''Displays Manager Menu''' 
    print "Hello Manager!"
    print 

def getManagerChoice():
    '''Gets user's input value '''
    choice = int(raw_input("Please pick the following: "))

    return choice


    
def main():
    while True:
        print "Welcome to the Stamp Machine!"
        name = getName()
        if name == MANAGER:
            choice = getManagerChoice()
            if choice == 0: 
                break
            elif choice == 1:
                showCurrentStats()
                choiceOptions = int(raw_input("What would you like to do? "))
                if choiceOptions == 1:
                    stockOnStamps()
                elif choiceOptions == 2:
                    stockOnCoins()
"show stats"                    
        else:
            processCustomer()            

if __name__ == '__main__'
    main()





'''Please pick the following: 
A.) Update Machine Stats
B.) Exit '''











    
    
