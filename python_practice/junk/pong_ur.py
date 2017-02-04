import urwid
import urwid.raw_display

#exit code
def exit(key):
    if key in ('q','Q'):
        raise urwid.ExitMainLoop()
#exit code

palette = [
    ('banner', 'black', 'light gray'),
    ('streak', 'black', 'brown'),
    ('bg', 'black', 'dark blue'),]

#txt = urwid.Text(('banner', u" TableTennis \n Score-Board "), align='center')
#map1 = urwid.AttrMap(txt, 'streak')
#fill = urwid.Filler(map1,'top')
#map2 = urwid.AttrMap(fill, 'bg')
bt = urwid.BigText(u"Sandesh Rana",urwid.Thin3x3Font() )
ht = urwid.Padding(bt, "center", width = 'clip')
#button = urwid.Button(u'count')
#div = urwid.Divider()
#pile = urwid.Pile([ht,div, button])
loop = urwid.MainLoop(ht, palette,unhandled_input= exit)
loop.run()
