import curs_eg
import time
screen = curs_eg.initscr()
dims = screen.getmaxyx() #should return max value of (y,x)
# print(dims)
# def x_axis(dims):
for i in range(dims[0]):
    screen.clear()
    y = int(i)
    x = int(dims[1] / 2)
    screen.addstr(y, x, 'Hello World!')
    screen.refresh()
    time.sleep(0.02)
    # y_axis

# def y_axis(self):
#     for i in range(dims[1]):
#         screen.clear()
#         y = int(dims[0]/2)
#         x = int(i)
#         screen.addstr(y, x , 'Hello World!')
#         screen.refresh()
#         time.sleep(0.01)
#         x_axis
screen.getch()
curs_eg.endwin()

