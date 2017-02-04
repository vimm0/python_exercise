
import curses
screen = curses.initscr()  # Initialize curses.

# Clear screen and draw default border:
screen.clear()
screen.border(0)
screen.addstr(10, 30, 'Hello world!')  # Row 10, row 30

begin_x = 20; begin_y = 7
height = 5; width = 40
win = curses.newwin(height, width, begin_y, begin_x)

screen.refresh()      # Redraw screen.
opt = screen.getch()  # Wait for user to enter character.
curses.endwin()       # End screen (ready to draw new one, but instead we exit)

# If you wanted a second screen you'd start with screen.clear and repeat here.
