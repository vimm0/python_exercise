
    def add_buttons(self, buttons):
        l = []
        for name, exitcode in buttons:
            b = urwid.Button( name, self.button_press )
            b.exitcode = exitcode
            b = urwid.AttrWrap( b, 'selectable','focus' )
            l.append( b )
        self.buttons = urwid.GridFlow(l, 10, 3, 1, 'center')
        self.frame.footer = urwid.Pile( [ urwid.Divider(),
            self.buttons ], focus_item = 1)

def button_press(self, button):
        raise DialogExit(button.exitcode)

 def mouse_event(self,size,event,button,col,row,focus):
        if event=='mouse release':
            self.state = True
            raise DialogExit, 0

def do_menu(text, height, width, menu_height, *items):
    def constr(tag, state ):
        return MenuItem(tag)
    d = ListDialogDisplay(text, height, width, constr, items, False)
    d.add_buttons([    ("OK", 0), ("Cancel", 1) ])
    return d


def do_yesno(text, height, width):
    d = DialogDisplay( text, height, width )
    d.add_buttons([    ("Yes", 0), ("No", 1) ])
    return d


class pong():
  def __init__(self,player_one,player_two):
    self.player_one = player_one
    self.player_two = player_two

  def btn_player_one():
    """This part has to show the recent score on the board of
    player one which is '0' for first case and other depends on
    the other condition"""
    print("player one count")
    count++
    """Highlight the servicing player"""
    divide_show()
    if player_one_count == 10 and player_two_count == 10:
       show_deuce_both()
       count_deuce()
    if player_one_count == 11:
       """Display player One wins"""

  def divide_show():
     if count%2 == 0:
        toggle_visibility()

        """change the highlight i.e if it is in the player one toggle
        to player two side"""

  def btn_player_two():
    """This part has to show the recent score on the board of player
    two which is '0' for first case and other depends on the other
    condition"""
    print("player two count")
    count++
    """Highlight the servicing player"""
    divide_show()
    if player_one_count == 10 and player_two_count == 10:
       show_deuce_both()
       count_deuce()
    if player_one_count == 11:
       """Display player One wins"""
#Deuce
#Deuce

#Advantage
#Advantage

  def toggle_visibility(): #visibility toggle
     if visible in player_one and not visible in player_two:
        """Highlight player two"""
     elif visible in player_two and not visible in player_one:
        """Highlight player one"""
  def player_one_win():
     """show game over and declare player one wins"""
  def player_two_win():
     """show game over and declare player two wins"""

#Advantage show
  def adv_player_one():
     if visible in player_one and not visible in player_two:
        show_advantage_one()
        """Highlight player two"""
     elif visible in player_two and not visible in player_one:
        show_advantage_one()
        """Highlight player one"""

   def adv_player_two():
     if visible in player_two and not visible in player_one:
        show_advantage_two()
        """Highlight player one"""
     elif visible in player_one and not visible in player_two:
        show_advantage_two()
        """Highlight player two"""
  def show_deuce_both():
    """show deuce on both sides"""
  def show_advantage_one():
    """highlight player one as advantage"""
  def show_advantage_two():
    """highlight player two as advantage"""
  def serve_status():
    """if player one is serving ***player one is serving*** """
    """if player two is serving ***player two is serving*** """
  def check_button():
    if player_one > player_two:
      """player one wins in the status"""
    elif player two > player one:
      """player two wins in the status"""
    else:
      """Game Draw"""
  def toss_button():
    if ran <=0.5:
     """show player one serving"""
    else:
     """show player two serving"""
  disable_toss_button

  def gameover():
    check_button_disable
    toss_button_disable
    both_button_disable








