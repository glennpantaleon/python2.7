'''
cs1114 

Submission: coinWorks

Programmer: Glenn Pantaleon
Username: gpanta01@students.poly.edu

Purpose of program: To convert dollar bill values to coin values

constraints: none
assumptions: none

'''


def moneyToCoins(usBillAmount):
    '''Converts US dollars into US coins'''
    dollarAmnt = usBillAmount * 100
    dollarCoin = dollarAmnt//100
    quarterAmnt = (dollarAmnt - (dollarCoin * 100))
    quarterCoin = quarterAmnt//25
    dimeAmnt = quarterAmnt - (quarterCoin*25)
    dimeCoin = dimeAmnt//10
    nickleAmnt = dimeAmnt - (dimeCoin*10)
    nickleCoin = nickleAmnt//5
    pennyAmnt = nickleAmnt - (nickleCoin*5)
    pennyCoin = pennyAmnt//1
    return dollarCoin,quarterCoin,dimeCoin,nickleCoin,pennyCoin
    
    



def showCoins(dollarCoin,quarterCoin,dimeCoin,nickleCoin,pennyCoin):
    '''Prints out amount of coins within bill amount'''
    print " You have ", int(dollarCoin), " Dollars"
    print " You have ", int(quarterCoin)," Quarters"
    print " You have ", int(dimeCoin), "Dimes"
    print " You have ", int(nickleCoin), "Nickles"
    print " You have ", int(pennyCoin), "Cent(s)"
