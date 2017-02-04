
import curses
from math import *

screen = curses.initscr()
curses.noecho()
curses.cbreak()
curses.start_color()
screen.keypad( 1 )
curses.init_pair(1,curses.COLOR_BLACK, curses.COLOR_CYAN)
highlightText = curses.color_pair( 1 )
normalText = curses.A_NORMAL
screen.border( 0 )
curses.curs_set( 0 )
columns = 5
string = "Lorem ipsum dolor sit amet consectetuer metus nec eu C urabitur eleifen."
screen.addstr(1,1,string)
screen.addstr(20,1,"Press ESC to EXIT")
screen.refresh()
rows = int(ceil(len(string)/columns))
box = curses.newwin(rows + 2, columns + 2, 3, 1)
box.box()
for row in range(1,rows+1):
    box.addstr(row,1,string[(row*columns)-columns:(row*columns)])
    box.refresh()

x = screen.getch()
while x != 27:
    x = screen.getch()
curses.endwin()
exit()
