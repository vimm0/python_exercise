#!/usr/bin/env python
# my_ncurses_with_color.py - very basic demonstration of ncurses with color
# plus a fancy border.
 
import curses
 
screen = curses.initscr()  # Initialize curses.
curses.start_color()       # Must call this before creating pairs.
 
# Create hardcoded color pairs (foreground/background) to use:
curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_WHITE)
curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
 
# Clear screen and draw custom border:
screen.clear()
screen.border(curses.ACS_VLINE, curses.ACS_VLINE,
              curses.ACS_DIAMOND, curses.ACS_DIAMOND)
# NOTE: 0 will be normal style border, here the order is:
# left, right, top, bottom
 
# NOTE: First two arguments of addstr are row and col position.
screen.addstr(1, 4, 'Ncurses with color, featuring:')
screen.addstr(2, 4, '  > Underlined text', curses.A_UNDERLINE)
screen.addstr(3, 4, '  > Blue on white', curses.color_pair(2))
screen.addstr(4, 4, '  > Bold, blinking and red', curses.A_BOLD |
              curses.A_BLINK | curses.color_pair(3))
screen.addstr('     ... press any key to exit')
 
screen.refresh()      # Redraw screen.
opt = screen.getch()  # Wait for user to enter character.
curses.endwin()       # End screen (ready to draw new one, but instead we exit)
