import curses
import time
screen = curses.initscr()
dims = screen.getmaxyx() #should return max value of (y,x)
q = -1
x,y = 0,0
Vertical = 1
Horizontal = 1
while q != ord('q'):
    screen.clear()
    screen.addstr(int(y), int(x) , 'Hello World!')
    screen.refresh()
    q = screen.getch()
    if q == ord('w') and y > 0:
        y-=1
    elif q == ord('s') and y < dims[0] - 1:
        y+=1
    if q == ord('a') and x > 0:
        x-=1
    elif q == ord('d') and x < dims[1] -len('Hello World!') - 1:
        x+=1
screen.getch()
curses.endwin()

