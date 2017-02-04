#import urwid.curses_display
import urwid as u


from urwid import MainLoop, SolidFill




caption = u.Text(('caption', 'Enter some words:'), align='center')
input = u.Edit(multiline=False)
# Will be set from the code
scratchpad = u.Text('')
button = u.Button('Push me')
button_wrap = u.Padding(u.AttrMap(button, 'button.normal', 'button.focus'),
                      align='center', width=15)
interior = u.Filler(u.Pile())

window = u.LineBox(interior)
single_color = [('basic', 'yellow', 'dark blue')]

topw = u.Overlay(window, background, 'center', 30, 'middle', 10)
main_loop = MainLoop(topw, palette=single_color)
main_loop.run()

#def callback(key):
#    raise ExitMainLoop()
#

#mainloop = MainLoop(u.AttrMap(SolidFill('#'),
#'basic'), palette=single_color).run()

#b = u.Button(u"cancel")
#b.render((15,), focus = True).text
#u.MainLoop(b).run()
#u.MainLoop(b)
