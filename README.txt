# PythonSMA

Duncan Starkenburg & Luke Herren CS1210A 12/7/23

A VERY basic stock market application that uses rudimentary stock data 
(given in CSV format) and uses our algorithm to sort socks in order of "best stocks to invest in"

No pip-installable modules used

How to test:
	choice 2 is pretty easy, it just returns the best stocks from our CSV list of stock info.
	Just make sure the CSV file is in the same folder as main.py and the program will run correctly
	
	choice 1 requires you to enter some information about a stock. You can look up some numbers on 
	yahoo finance or something, or just enter some random ones. It will return a point value based on
	how good our algorithm thinks your stock is /500 points.
	
There are no known defects. 

Work was split evenly. We both outlined all of the functions and their responsibilities planning wise.
Luke was responsible for read_CSV method(), part of assess_CSV(), and main. Duncan was responsible for 
assess_stock() and assess_input(). 


No source code was used (besides line 150). The dataset used for CSV: https://datahub.io/core/s-and-p-500-companies-financials
