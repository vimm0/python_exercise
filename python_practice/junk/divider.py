import urwid

def exit(key):
    if key in ('q','Q'):
        raise urwid.ExitMainLoop()

txt = urwid.Text(u"Hello World")
fill = urwid.Filler(txt, 'top')
loop = urwid.MainLoop(fill, unhandled_input = exit)
loop.run()

