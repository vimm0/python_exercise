import urwid

#This program initially displays the string Hello World,
#then it displays each key pressed, exiting when the user presses Q.
def show_or_exit(key):
    if key in ('q', 'Q'):
       raise urwid.ExitMainLoop()
    txt.set_text(repr(key))

txt = urwid.Text(u"Hello World")
fill = urwid.Filler(txt, 'top')
loop = urwid.MainLoop(fill, unhandled_input=show_or_exit)
loop.run()
