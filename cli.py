from time import sleep
import time
import sys
import os
import curses
from curses import wrapper
from yahoo_fin import stock_info as si

MARGIN_TOP = 2
MARGIN_LEFT = 2

def main(stdscr):
	# Clear screen
	curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
	curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
	curses.halfdelay(2)
	curses.resize_term(60, 200)
	while True:
		stdscr.clear()
		write_header(stdscr)
		write_stock_info(stdscr,["aapl", "msft", "googl", "amzn", "fb", "brk-a", "brk-b", "baba"])
		stdscr.refresh()
		process_input(stdscr.getch())

	stdscr.getkey()


def process_input(input):
	if input == 113: # letter q
		sys.exit()


def write_header(stdscr):
	stdscr.addstr(MARGIN_TOP, MARGIN_LEFT, "Ticker", curses.A_BOLD)
	stdscr.addstr(MARGIN_TOP, MARGIN_LEFT + 10, "Quote Price", curses.A_BOLD)
	stdscr.addstr(MARGIN_TOP, MARGIN_LEFT + 32, "Open", curses.A_BOLD)
	stdscr.addstr(MARGIN_TOP, MARGIN_LEFT + 42, "y Close", curses.A_BOLD)
	stdscr.addstr(MARGIN_TOP, MARGIN_LEFT + 52, "Ask", curses.A_BOLD)
	stdscr.addstr(MARGIN_TOP, MARGIN_LEFT + 66, "Bid", curses.A_BOLD)
	stdscr.addstr(MARGIN_TOP, MARGIN_LEFT + 80, "MCap", curses.A_BOLD)
	stdscr.addstr(MARGIN_TOP, MARGIN_LEFT + 92, "Vol", curses.A_BOLD)
	stdscr.addstr(MARGIN_TOP, MARGIN_LEFT + 105, "Avg Vol", curses.A_BOLD)
	stdscr.addstr(MARGIN_TOP, MARGIN_LEFT + 118, "Beta", curses.A_BOLD)
	stdscr.addstr(MARGIN_TOP, MARGIN_LEFT + 128, "PE", curses.A_BOLD)
	stdscr.addstr(MARGIN_TOP, MARGIN_LEFT + 138, "EPS", curses.A_BOLD)



def write_stock_info(stdscr,tickers):
	y_offset = 1
	for ticker in tickers:
		data = si.get_quote_table(ticker)
		price = data["Quote Price"]
		open_ = data["Open"]
		color = 2 if price > open_ else 1
		stdscr.addstr(MARGIN_TOP + y_offset, MARGIN_LEFT, str(ticker), curses.color_pair(color)|curses.A_BOLD)
		stdscr.addstr(MARGIN_TOP + y_offset, MARGIN_LEFT + 10, str(price), curses.color_pair(color)|curses.A_BOLD)
		stdscr.addstr(MARGIN_TOP + y_offset, MARGIN_LEFT + 32, str(open_), curses.color_pair(color)|curses.A_BOLD)
		stdscr.addstr(MARGIN_TOP + y_offset, MARGIN_LEFT + 42, str(data["Previous Close"]), curses.color_pair(color)|curses.A_BOLD)
		stdscr.addstr(MARGIN_TOP + y_offset, MARGIN_LEFT + 52, str(data["Ask"]), curses.color_pair(color)|curses.A_BOLD)
		stdscr.addstr(MARGIN_TOP + y_offset, MARGIN_LEFT + 66, str(data["Bid"]), curses.color_pair(color)|curses.A_BOLD)
		stdscr.addstr(MARGIN_TOP + y_offset, MARGIN_LEFT + 80, str(data["Market Cap"]), curses.color_pair(color)|curses.A_BOLD)
		stdscr.addstr(MARGIN_TOP + y_offset, MARGIN_LEFT + 92, str(data["Volume"]), curses.color_pair(color)|curses.A_BOLD)
		stdscr.addstr(MARGIN_TOP + y_offset, MARGIN_LEFT + 105, str(data["Avg. Volume"]), curses.color_pair(color)|curses.A_BOLD)
		stdscr.addstr(MARGIN_TOP + y_offset, MARGIN_LEFT + 118, str(data["Beta (3Y Monthly)"]), curses.color_pair(color)|curses.A_BOLD)
		stdscr.addstr(MARGIN_TOP + y_offset, MARGIN_LEFT + 128, str(data["PE Ratio (TTM)"]), curses.color_pair(color)|curses.A_BOLD)
		stdscr.addstr(MARGIN_TOP + y_offset, MARGIN_LEFT + 138, str(data["EPS (TTM)"]), curses.color_pair(color)|curses.A_BOLD)
		y_offset += 1
 
if __name__ == '__main__':
    wrapper(main)