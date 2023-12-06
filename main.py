"""
 - Duncan Starkenburg & Luke Herren -
 -   UVM CS 1210 - Final Project    -
 -   Python Simple Market Advisor   -
"""

import csv
import math

#returns nested dictionary
def read_CSV():
    dictionary500 = {}
    
    with open("S&P500-stocks.csv") as file_read:
        reader = csv.reader(file_read)
        next(reader)
        for row in reader:
            symbol = row[0]
            price = float(row[2])
            price_earnings = float(row[3])
            earnings_share = float(row[4])
            high52 = float(row[5])
            low52 = float(row[6])
            price_sales = float(row[7])
            price_book = float(row[8])
            dictionary500[symbol] = {'price': price,
                                     'price_earnings': price_earnings,
                                     'earnings_share': earnings_share,
                                     'high52': high52,
                                     'low52': low52,
                                     'price_sales': price_sales,
                                     'price_book': price_book}
    return dictionary500


#return the integer point value of one stock out of 500 pts, 100 per cat.
def assess_stock(p, pe, es, h52, l52, ps, pb):
    price_score = 0
    price_earn_score = 0
    earn_share_score = 0
    price_sale_score= 0
    price_book_score = 0
    
    # Calculate a score based on how close the current price is to the stocks 52 week lowest price
    if p > h52:
        price_score = 0
    elif p < l52:
        price_score = 100
    else:
        price_score = math.floor((h52 - p)/(h52 - l52) * 100)
        
    # Calculate a score based on the price vs earned value over 52 weeks
    # The closer a P/E value is to 0 the better the stock
    if pe < 0:
        price_earn_score = 0
    elif pe > 100:
        price_earn_score = 0
    else:
        price_earn_score = 100 - math.floor(pe)
        
    # Calculate a score based on the earnings per share value over 52 weeks
    # The larger the earnings per share, the better the stock.
    # The best stock in our data set has a E/S of (rounded) 45$
    if es < 0:
        earn_share_score = 0
    elif es > 40:
        earn_share_score = 100
    elif es >= 20:
        earn_share_score = 75
    elif es >= 10:
        earn_share_score = 50
    elif es >= 9:
        earn_share_score = 45
    elif es >= 8:
        earn_share_score = 40
    elif es >= 7:
        earn_share_score = 35
    elif es >= 6:
        earn_share_score = 30
    elif es >= 5:
        earn_share_score = 25
    elif es >= 4:
        earn_share_score = 20
    elif es >= 3:
        earn_share_score = 15
    elif es >= 2:
        earn_share_score = 10
    else:
        earn_share_score = 5
        
    # Calculate a score based on the price to sales ratio over 52 weeks
    # Most investors seek companies with a ratio between 1 and 2
    # The following algorithm assigns a score based on how close to this range the value is
    if ps <= 1.0:
        price_sale_score = math.floor(ps * 100)
    elif ps > 1.0 and ps < 2.0:
        price_sale_score = 100
    elif ps > 10.0:
        price_sale_score = 0
    else:
        price_sale_score = math.floor(100 - ((ps - 1) * 10))
        if price_sale_score < 0:
            price_sale_score = 0
    
    # Calculate a score based on the price to books ratio over 52 weeks
    # Most investors seek companies with a ratio below one.
    # Any stock over 6 is undesirable and is trading at a high premium
    if pb > 6.0:
        price_book_score = 0
    elif pb < 1.0:
        price_book_score = 100
    elif pb > 5.0:
        price_book_score = 5
    elif pb > 4.0:
        price_book_score = 25
    elif pb > 3.0:
        price_book_score = 45
    elif pb > 2.0:
        price_book_score = 65
    else:
        price_book_score = 85
    
    totalscore = price_score + price_earn_score + earn_share_score + price_sale_score + price_book_score
    return totalscore
## I stopped here! let me know if this algorithm is working for you or not!
    
#returns top five of a sorted list highest to lowest
def assess_CSV():
    dictionary500 = read_CSV()
    dict500_with_points = []
    output_list = []
    
    # Compute each company score and append a
    # (symbol, score) tuple to list dict500_with_points
    for symbol in dictionary500.keys():
        price = dictionary500[symbol]['price']
        pe = dictionary500[symbol]['price_earnings']
        es =  dictionary500[symbol]['earnings_share']
        h52 = dictionary500[symbol]['high52']
        l52 = dictionary500[symbol]['low52']
        ps = dictionary500[symbol]['price_sales']
        pb = dictionary500[symbol]['price_book']
        
        dict500_with_points.append((symbol, assess_stock(price, pe, es, h52, l52, ps, pb)))
    dict500_with_points.sort(key=lambda tup: tup[1])
    for i in range(5):
        output_list.append(dict500_with_points.pop())
    return output_list
        
    


#returns a stock rating out of 10 0=bad 10=good
#def assess_input():
    
    
    


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
        #try:
            choice = int(input("Please enter 1 or 2: "))
        
            if choice == 1:
                 print("input")
                 print(assess_input())
                 break
            elif choice == 2:
                 print("csv")
                 print(assess_CSV())
                 break
            else:
                print("Invalid input!")
                 
       # except ValueError:
           # print("Invalid input!")
