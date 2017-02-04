#!/usr/bin/env python
# ncurses_hello_world.py - minimal ncurses example with default border.
 
import curses
screen = curses.initscr()  # Initialize curses.
curses.start_color();
curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
# Clear screen and draw default border:
curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
screen.clear()

screen.border(curses.ACS_DIAMOND,curses.ACS_DIAMOND,curses.ACS_DIAMOND,curses.ACS_DIAMOND)
screen.addstr(2, 8,"Pretty text", curses.color_pair(1))
screen.addstr(1, 1, "Current mode: Typing mode",
              curses.A_DIM) # Row 10, row 30
screen.addstr(3, 4, '  > Blue on white', curses.color_pair(1))
screen.addstr(4, 4, '  > Bold, blinking and red', curses.A_BOLD |
              curses.A_BLINK | curses.color_pair(3))

screen.refresh()      # Redraw screen.

while True:
    c = screen.getch()
    if c == ord('p'):
        PrintDocument()
    elif c == ord('q'):
        break  # Exit the while loop
    elif c == curses.KEY_HOME:
        x = y = 0
        # opt = screen.getch()  # Wait for user to enter character.
curses.endwin()       # End screen (ready to draw new one, but instead we exit)
 
# If you wanted a second screen you'd start with screen.clear and repeat here.