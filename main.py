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
        try:
            price_score = math.floor((h52 - p)/(h52 - l52) * 100)
        except ZeroDivisionError:
            price_score = 100
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
def assess_CSV(d500):
    dict500_with_points = []
    output_list = []
    
    # Compute each company score and append a
    # (symbol, score) tuple to list dict500_with_points
    for symbol in d500.keys():
        price = d500[symbol]['price']
        pe = d500[symbol]['price_earnings']
        es =  d500[symbol]['earnings_share']
        h52 = d500[symbol]['high52']
        l52 = d500[symbol]['low52']
        ps = d500[symbol]['price_sales']
        pb = d500[symbol]['price_book']
        
        dict500_with_points.append((symbol, assess_stock(price, pe, es, h52, l52, ps, pb)))
    
    # This next line is taken from 
    # https://stackoverflow.com/questions/3121979/how-to-sort-a-list-tuple-of-lists-tuples-by-the-element-at-a-given-index
    # Although we didnt learn this in this course, this line sorts (in place) a list of tuples by the tuple's second value
    dict500_with_points.sort(key=lambda tup: tup[1])
    
    for i in range(5):
        output_list.append(dict500_with_points.pop())
    return output_list
        
    


#returns a stock rating out of 10 0=bad 10=good
def assess_input():
    print("****************************************************************\n"
          "You will need to provide us with some basic information about your\n"
          "stock. Then, we will run our algorithm to let you know how good (or\n"
          "bad) of an investment that specific stock is.\n"
          "****************************************************************")
    while True:
        sym = input("Enter a symbol (XXX if unknown): ")
        if len(sym) >= 3 and len(sym) <= 5:
            break
        else:
            print("Symbol must be 3-5 characters! Using XXX")
            sym = 'XXX'
            break
    while True:
        p = input("Enter a price per stock in $0.00: $")
        try:
            p = float(p)
            if p >= 0.0:
                break
        except ValueError:
            print("Please enter a float!")
    while True:
        pe = input("Enter a P/E ratio as a decimal: ")
        try:
            pe = float(pe)
            if pe >= 0.0:
                break
        except ValueError:
            print("Please enter a float!")
    while True:
        es = input("Enter a E/S ratio as a decimal: ")
        try:
            es = float(es)
            if es >= 0.0:
                break
        except ValueError:
            print("Please enter a float!")
    while True:
        h52 = input("Enter the 52 week high price as a decimal: ")
        try:
            h52 = float(h52)
            if h52 >= 0.0:
                break
        except ValueError:
            print("Please enter a float!")
    while True:
        l52 = input("Enter the 52 week low price as a decimal: ")
        try:
            l52 = float(l52)
            if l52 >= 0.0:
                break
        except ValueError:
            print("Please enter a float!")
    while True:
        ps = input("Enter the P/S ratio as a decimal: ")
        try:
            ps = float(ps)
            if ps >= 0.0:
                break
        except ValueError:
            print("Please enter a float!")
    while True:
        pb = input("Enter the P/B ratio price as a decimal: ")
        try:
            pb = float(l52)
            if pb >= 0.0:
                break
        except ValueError:
            print("Please enter a float!")
    print('*'*65)
    print('Here is the information of your stock plus our rating\n'
          'Score key >> 0-100 BAD | 100-200 POOR | 200-300 AVERAGE | 300-400 DECENT | 400-500 PRIME')
    print('*'*65)
    print('')
    print(f"{'Score':<5}  || {'Symbol':<6}  |  {'Price':^5}  |  {'P/E':^5}  |  {'E/S':^5}  |  {'52 Week High':^5}  |  {'52 Week Low':^5}  |  {'P/S':^5}  |  {'P/B':>5}")
    print('-'*100)
    print(f"{assess_stock(p, pe, es, h52, l52, ps, pb):>5}  ||   {sym:^3}   |  {p:>6.2f} |  {pe:>5.2f}  |"
          f"  {es:>6.2f} |     {h52:>6.2f}     |     {l52:>6.2f}    "
          f"|  {ps:>5.2f}  |   {pb:>5.2f}")
    


#main method
if __name__ == "__main__":
    dictionary500 = read_CSV()
    #intro
    print("****************************************************************\n"
          "Hello! Welcome to our stock market advisor program. The goal of\n"
          "this program is to help you choose what stock to invest your\n"
          "money in. \n\nThere are two options, press 1 if you would like to \n"
          "provide your own stock and data, or press 2 if you would like \n"
          "the program to choose 5 of the best stocks from the S&P 500.\n"
          "****************************************************************")
    #Input validation
    while True:
        try:
            choice = int(input("Please enter 1 or 2: "))
            print("\n")
        
            if choice == 1:
                 assess_input()
                 break
            elif choice == 2:
                 print("****************************************************************\n"
                       "Based on the CSV data of the S&P 500, we have scored\n"
                       "and ranked each company. The score is out of 500 where\n"
                       "500 is a perfect investment, and 0 is a terrible investment.\n"
                       "Here are our top five next best picks\n"
                       "****************************************************************\n")
                 print(f"{'Score':<5}  || {'Symbol':<6}  |  {'Price':^5}  |  {'P/E':^5}  |  {'E/S':^5}  |  {'52 Week High':^5}  |  {'52 Week Low':^5}  |  {'P/S':^5}  |  {'P/B':>5}")
                 output = assess_CSV(dictionary500)
                 for i in output:
                     d = dictionary500[i[0]]
                     print("-" * 100)
                     print(f"{i[1]:>5}  ||   {i[0]:^3}   |  {d['price']:>6.2f} |  {d['price_earnings']:>5.2f}  |"
                           f"  {d['earnings_share']:>6.2f} |     {d['high52']:>6.2f}     |     {d['low52']:>6.2f}    "
                           f"|  {d['price_sales']:>5.2f}  |   {d['price_book']:>5.2f}")
                 break
            else:
                print("Invalid input!")
                 
        except ValueError:
            print("Invalid input!")
