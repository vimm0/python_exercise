import curses
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(1)


pad = curses.newpad(100, 100)
#  These loops fill the pad with letters; this is
# explained in the next section
for y in range(0, 100):
    for x in range(0, 100):
        try:
            pad.addch(y,x, ord('a') + (x*x+y*y) % 26)
        except curses.error:
            pass

#  Displays a section of the pad in the middle of the screen
pad.refresh(0,0, 5,5, 20,75)

pad = curses.newpad(120, 220)

for y in range(0, 100):
    for x in range(0, 100):
        try:
            pad.addch(y,x, ord('a') + (x*x+y*y) % 26)
        except curses.error:
            pass

#  Displays a section of the pad in the middle of the screen
#pad.refresh(100,100, 15,15, 20,75)

stdscr.addstr(0,0, "RED ALERT!", curses.color_pair(1))
