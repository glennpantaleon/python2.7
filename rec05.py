'''
cs1114 

Submission: rec05

Programmer: Glenn Pantaleon
Username: gpanta01@students.poly.edu

Purpose of program: to make a money converter and 

constraints: none
assumptions: none


'''


PESO_RATE = 0.0778

import math


def printAsUsDollars(usDollarAmount, currencyStyle = '$'):
    '''Gives the amount of money in US currency rounding to the next penny.'''
    print currencyStyle, "%.2f" % usDollarAmount
    


def convertPesosToUsDollars(pesosAmount, currencyStyle = '$'):
    '''Converts amount of Pesos into US currency.'''
    pesoDollar = pesosAmount * PESO_RATE
    print currencyStyle, "%.2f" % pesoDollar



def printDollarBillsToCoins(usBillAmount):
    '''Converts US dollars inot US coins'''
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
    
    



def quanityOfCoins(dollarCoin,quarterCoin,dimeCoin,nickleCoin,pennyCoin):
    '''Prints out amount of coins within bill amount'''
    print " You have ", int(dollarCoin), " Dollars"
    print " You have ", int(quarterCoin)," Quarters"
    print " You have ", int(dimeCoin), "Dimes"
    print " You have ", int(nickleCoin), "Nickles"
    print " You have ", int(pennyCoin), "Cent(s)"
