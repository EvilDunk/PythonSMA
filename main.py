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
            earnings_share = row[4]
            high52 = row[5]
            low52 = row[6]
            price_sales = row[7]
            price_book = row[8]
            
            dictionary500[symbol] = {'price': price,
                                     'price_earnings': price_earnings,
                                     'earnings_share': earnings_share,
                                     'high52': high52,
                                     'low52': low52,
                                     'price_sales': price_sales,
                                     'price_book': price_book,
                                     } 
            
    return dictionary500
    
    
    
#returns sorted list highest to lowest
def assess_CSV():
    dictionary500 = read_CSV()
    
    for symbol in dictionary500.items():
        price = dictionary500[symbol]['price']
        #I left off here!!
        #This isn't workings, says hashable error. The read_CSV() function is good
        
        
        
    


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