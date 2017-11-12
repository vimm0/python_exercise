import curses
screen = curses.initscr()

dims = screen.getmaxyx() #should return max value of (y,x)
screen.addstr(int(dims[0]/2), int(dims[1]/2 - 6) , 'Hello World!')
screen.refresh()
screen.getch()
curses.endwin()

