import curses

def make_win(stdscr, h,l, y,x, str):
   win = stdscr.subwin(h,l, y,x) # ???
   win.erase()
   win.box()
   win.addstr(2, 2, str)
   return win

def test(stdscr):
   curses.curs_set(0)
   stdscr.box()
   stdscr.addstr(2, 2, "windows everywhere")
   win1 = make_win(stdscr, 10,12, 5,5, "Window 1")
   win2 = make_win(stdscr, 10,12, 8,8, "Window 2")
   stdscr.refresh(); c = stdscr.getch()

if __name__ == '__main__':
   curses.wrapper(test)
