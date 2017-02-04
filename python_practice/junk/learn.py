import curses

stdscr = curses.initscr()
#Turn off auto echo (enable reading of keys prior to displaying)
#curses.noecho()

#React to keys instantly without buffered input relying on Enter Key
#curses.cbreak()

#enable special keys using curses processing
#stdscr,keypad(True)

begin_x = 20; begin_y = 7
height = 5; width = 40
win = curses.newwin(height, width, begin_y, begin_x)

#def exit_program():
  #reverse 'curses freindly terminal settings'
#  curses.nocbreak()
#  stdscr.keypad(False)
#  curses.echo()
#curses.endwin()
   
