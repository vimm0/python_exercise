#!/usr/bin/python

import curses

# -----------------------------------------------------------------------------
class curses_screen:
    def __enter__(self):
        self.stdscr = curses.initscr()
        curses.cbreak()
        curses.noecho()
        self.stdscr.keypad(1)
        return self.stdscr
    def __exit__(self,a,b,c):
        curses.nocbreak()
        self.stdscr.keypad(0)
        curses.echo()
        curses.endwin()

# -----------------------------------------------------------------------------
with curses_screen() as stdscr:
    pass # Do your stuff here...

