from time import sleep
import sys
import os
import curses
from curses import wrapper
from yahoo_fin import stock_info as si


stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)



curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()



def write_stock_info(tickers):
	for ticker in tickers:
		data = si.get_quote_table(ticker)
		output = "\r"
		price = str(data["Quote Price"])
		output += price
		output += "\n I love ice cream"
		output += "\0x1B[1A"
		sys.stdout.write(output)
		sys.stdout.flush()


# main loop
def main(*tickers):
    "Write stock info for ticker symbol"
    for i in range(10):
    	write_stock_info(tickers)
    sys.stdout.write("\n")
 
if __name__ == '__main__':
    wrapper(main)