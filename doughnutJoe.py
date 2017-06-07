'''
A program designed for the purpose of selling coffee and donuts.
The coffee and donut shop only sells one flavor of coffee and donuts at a fixed price.
Each cup of coffee cost seventy seven cents and each donut cost sixty four cents.
This program will imediately be activated upon a business.


\/\/\/\\/\/\/\
DOUGHNUT JOE
\/\/\/\\/\/\/\

__ cups of coffee: $__.__
    __  doughnuts: $__.__
              tax: $__.__

        Amount Owed: $_____

Thank you for purchasing local.

'''

import os

tax_rate = 0.0846
coffee_cost = 0.77
donut_cost = 0.64

def getOrder ():
    '''Retrives the customer's order.'''
    number_of_donuts = raw_input("How many donuts would you like to order? ")
    donut = int(number_of_donuts)
    number_of_coffee = raw_input("How many cups of coffee do you want? ")
    coffee = int(number_of_coffee)
    return donut,coffee

def calcAmount (donut,coffee):
    '''Calculates the total amount of money paid for the coffee and donuts.'''
    total_cost_of_donuts = donut * donut_cost
    total_cost_of_coffee = coffee * coffee_cost
    bill_before_tax = total_cost_of_donuts + total_cost_of_coffee
    total_tax = bill_before_tax * tax_rate
    total_cost = bill_before_tax + total_tax
    return total_cost_of_donuts,total_cost_of_coffee,bill_before_tax,total_tax,total_cost

def presentBill (total_cost_of_donuts,total_cost_of_coffee,bill_before_tax,total_tax,total_cost,donut,coffee):
    '''Presents the bill after the calculations are done.'''
    print "/\/\/\/\/\/\/\/\/\/\\"
    print "     DOUGHNUT JOE   "
    print "/\/\/\/\/\/\/\/\/\/\\"
    print str(coffee) + " cups of coffee: $" + str (total_cost_of_coffee)
    print str(donut) + " doughnuts: $" + str (total_cost_of_donuts)
    print "Tax: $" + str (total_tax)
    print "Amount Owed: $" + str (total_cost)
    print '''

Thank you for buying

'''

def main():
    donut,coffee = getOrder ()
    total_cost_of_donuts,total_cost_of_coffee,bill_before_tax,total_tax,total_cost = calcAmount (donut,coffee)
    presentBill (total_cost_of_donuts,total_cost_of_coffee,bill_before_tax,total_tax,total_cost,donut,coffee)
    os.system ("pause")
main()
