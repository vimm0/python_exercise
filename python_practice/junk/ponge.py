import curses
import urwid

import urwid as u

def exit(key):
   if key in ('q','Q'):
     raise u.ExitMainLoop()

def make_win(stdscr, h,l, y,x, str):
   win = stdscr.subwin(h,l, y,x)
   win.erase()
   win.box()
   win.addstr(2, 2, str)
   return win

def test(stdscr):
   curses.curs_set(0)
   stdscr.box()
   stdscr.addstr(2, 90, "Table-Tennis", curses.A_BOLD)
   win1 = make_win(stdscr, 20,60, 5,5, "Window 1")
   win2 = make_win(stdscr, 20,80, 5,68, "Window 2")
   stdscr.refresh(); c = stdscr.getch()

if __name__ == '__main__':
   curses.wrapper(test)




