"""
 - Duncan Starkenburg & Luke Herren -
 -   UVM CS 1210 - Final Project    -
 -   Python Simple Market Advisor   -
"""

import csv

#returns nested dictionary
def read_CSV():
    dictionary500 = {}
    
    with open("S&P500-stocks.csv") as file_read:
        reader = csv.reader(file_read)
        next(reader)
        for row in reader:
            symbol = row[0]
            price = row[2]
            price_earnings = row[3]
            dictionary500[symbol] = {'price': price, 'price/earnings': price_earnings} 
            
    return dictionary500
    
#returns sorted list highest to lowest
def assess_CSV():
    print(read_CSV())
    


#returns a stock rating out of 10 0=bad 10=good
#def assess_input():
    
    
    
#return the point value of one stock out of 500 pts, 100 per cat.
#def assess_stock():



#main method
if __name__ == "__main__":
    
    #intro
    print("Hello! Welcome to our stock market advisor program. The goal of "
          "this program is to help you choose what stock to invest your "
          "money in. \n\nThere are two options, press 1 if you would like to "
          "provide your own stock and data, or press 2 if you would like "
          "the program to choose 5 of the best stocks from the S&P 500.")
    
    #Input validation
    while True:
        try:
            choice = int(input("Please enter 1 or 2: "))
        
            if(choice == 1):
                 print("input")
                 print(assess_input())
                 break
            elif(choice == 2):
                 print("csv")
                 print(assess_CSV())
                 break
            else:
                print("Invalid input!")
                 
        except ValueError:
            print("Invalid input!")