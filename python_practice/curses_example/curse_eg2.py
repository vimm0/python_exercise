import curses
from curses.textpad import Textbox, rectangle

class Screen(object):
    def __init__(self, stdscr):
        curses.use_default_colors()
        self.maptext = ''
        self.status = ''
        self.mesg = ''
        self.mesg_len = 0
        self.too_small = False
        self.windows = [stdscr]

    def clear(self):
        '''Clears screen'''
        self.get_stdscr().clear()

    def get_stdscr(self):
        '''Returns root windows'''
        return self.windows[0]

    def update(self, status, mesg):
        '''Updates self using given text'''
        self.status = status
        self.mesg = mesg
        m = mesg.split('\n')
        self.mesg_len = len(m)

    def update_map(self, to_show, scope):
        '''Maps universe, updates internal map string'''
        self.maptext = to_show.show(scope)

    def refresh(self):
        '''noutrefreshes all, then doupdates root'''
        for win in self.windows:
            win.noutrefresh()
        curses.doupdate()

    def draw_all(self, player=True):
        '''Draws screen onto terminal'''
        try:
            self.too_small = False
            self.get_stdscr().erase()
            self.get_stdscr().addstr(self.maptext)
            self.get_stdscr().addstr(self.mesg)
        except curses.error:
            self.too_small = True
            self.ask_for_resize()

    def draw_override(self,string):
        '''Overrides everything and draws string right now'''
        try:
            self.get_stdscr().erase()
            self.get_stdscr().addstr(string)
        except curses.error:
            self.too_small = True
            self.ask_for_resize()

    def ask_for_resize(self):
        '''Asks user to make window bigger'''
        self.get_stdscr().clear()
        self.get_stdscr().addstr(0,0,'Please make the terminal bigger')

    def draw_side(self):
        '''Makes text box, fills it with status output, draws it'''
        try:
            if not self.too_small:
                sidewin = self.get_stdscr().subwin(14, 41, 2, 18)
                sidewin.addstr(0, 0, self.status)
        except curses.error:
            self.ask_for_resize()

    def get_input(self):
        '''Makes a text box and gets input'''
        try:
            curses.curs_set(1)
            editwin = curses.newwin(1, 58, 18 + self.mesg_len, 1)
            editwin.noutrefresh()
            rectangle(self.get_stdscr(), 17 + self.mesg_len, 0, 19 + self.mesg_len, 59)
            box = Textbox(editwin)
            box.edit()
            curses.curs_set(0)
            return box.gather()
        except curses.error:
            self.ask_for_resize()

    def get_key(self):
        '''Gets single keypress'''
        try:
            return self.get_stdscr().getch()
        except (EOFError,KeyboardInterrupt):
            return ord('e')
