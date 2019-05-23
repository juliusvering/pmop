from time import sleep
import sys
from yahoo_fin import stock_info as si
import os



def write_stock_info(tickers: str[]):

	data = si.get_quote_table(ticker)
	output = "\r"
	price = str(data["Quote Price"])
	output += price
	output += "\n I love ice cream" + str(num)
	output += "\033[1A"
	sys.stdout.write(output)
	sys.stdout.flush()


# main loop
def main(ticker):
    "Write stock info for ticker symbol"
    for i in range(10):
    	write_stock_info([], i)
    sys.stdout.write("\n")
 
if __name__ == '__main__':
    import plac; plac.call(main)