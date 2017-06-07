#!C:\Python27\python.exe
'''
cs1114 

Submission: rec12

Programmer: Glenn Pantaleon
Username: gpanta01@students.poly.edu

Purpose of program, assumptions, constraints:

The program level documentation goes here
What the program does
Any special tricks
Any assumtions
Any constraints
etc..

'''

class HydroCarbMole(object):
    ''' '''
    def __init__(self,numOfCarbAtom,numOfHydroAtom,formulaName):   
        self.__numOfCarbAtom = numOfCarbAtom
        self.__numOfHydroAtom = numOfHydroAtom
        self.__formulaName = formulaName
        
    def getNumOfCarAtom(self):
        '''Returns number of Carbon Atoms'''
        return self.__numOfCarbAtom

    def getNumOfHydroAtom(self):
        '''Returns number of Hydron Atoms'''
        return self.__numOfHydroAtom

    def getFormulaName(self):
        '''Returns Formula Name'''
        return self.__formulaName

    def __str__(self):
        return "C" + str(self.__numOfCarbAtom) + "H" +str(self.__numOfHydroAtom)+ ": " + str(self.__formulaName)
    

#butane = HydroCarbMole(2,2,"C4H10")
#print butane
   
def addMoleculeList(lissy,object):
    '''Adds molecules in a list'''
    lissy.append(object)
    return lissy





    #def __cmp__(self,other):
        #if self.__numOfCarbAtom > other.__numOfCarbAtom and self.__numOfHydroAtom > other.numOfHydroAtom:
            #return 1
        #elif self.__numOfCarbAtom < other.__numOfCarbAtom and self.__numOfHydroAtom < other.numOfHydroAtom:
            #return -1
        #else:
            #return 0


def main():
    mollyList=[]
    butane = HydroCarbMole(4,10,"butane")
    print butane
    lissy = addMoleculeList(mollyList, butane)


if __name__=='__main__':
    main()
