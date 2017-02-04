import urwid as u
"""This game makes an assumption if a player is capable of making first count
then, he is serving first"""

def exit(key):
    if key in ('q','Q'):
        raise u.ExitMainLoop
    else:
        bt.set_text(repr(key))

# Frame
#w = urwid.AttrWrap(w, 'body')
#hdr = urwid.Text("Urwid BigText example program - F8 exits.")
#hdr = urwid.AttrWrap(hdr, 'header')
#w = urwid.Frame(header=hdr, body=w)

# Exit message
#exit = urwid.BigText(('exit'," Quit? "), exit_font)
#exit = urwid.Overlay(exit, w, 'center', None, 'middle', None)

bt = u.BigText("Table Tennis",  u.font.HalfBlock5x4Font())
bt = u.Padding(bt, 'center', width='clip')
bt = u.Filler(bt, 'top')
#ht = u.AttrWrap(u.Divider("=", 1), 'bright')
#ht = u.Filler(ht, 'relative')

#palette = [
#('dam','dark red','dark blue')
#]
loop = u.MainLoop(bt,unhandled_input = exit)
loop.run()

