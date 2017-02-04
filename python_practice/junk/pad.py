#!/usr/bin/env python
# ncurses_hello_world.py - minimal ncurses example with default border.
import curses
screen = curses.initscr()  # Initialize curses.
screen.clear()
screen.border(0)
screen.addstr(10, 30, 'Hello world!')  # Row 10, row 30
opt = screen.getch()  # Wait for user to enter character.
curses.endwin()       # End screen (ready to draw new one, but instead we exit)
# If you wanted a second screen you'd start with screen.clear and repeat here.
