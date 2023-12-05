"""
 - Duncan Starkenburg & Luke Herren -
 -   UVM CS 1210 - Final Project    -
 -   Python Simple Market Advisor   -
"""

#returns dictionary
#def readCSV(file_name):
    



if __name__ == "__main__":
    
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
                 break
            elif(choice == 2):
                 print("csv")
                 break
            else:
                print("Invalid input!")
                 
        except ValueError:
            print("Invalid input!")