import curses
import time
screen = curses.initscr()
dims = screen.getmaxyx() #should return max value of (y,x)

for i in range(dims[0]):
    screen.clear()
    screen.addstr(int(i), int(dims[1]/2 - 6) , 'Hello World!')
    screen.refresh()
    time.sleep(0.02)

for i in range(int(dims[1])):
    screen.clear()
    screen.addstr(int(dims[0]/2), int(i) , 'Hello World!')
    screen.refresh()
    time.sleep(0.02)
screen.getch()
curses.endwin()

