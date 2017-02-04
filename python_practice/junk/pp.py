import urwid as u
from urwid import SolidFill

def exit(key):
    if key in ('q','Q'):
        raise u.ExitMainLoop
bt = u.BigText("Table Tennis", u.font.HalfBlock5x4Font())
#bt = u.Padding(bt,'center', width='clip')
#bt = u.Filler(bt,'top')

loop = u.MainLoop(SolidFill('*'),unhandled_input=exit)
loop.run()
##palette = [
#    ('title','dark cnyan','dark red'),
#    ('dam','yellow','light red'),
#    ('bg','light cyan','black')]
#
#placeholder = u.SolidFill()
#loop = u.MainLoop(placeholder,palette,unhandled_input=exit)
#bt = u.BigText("Table-Tennis", u.font.HalfBlock5x4Font())
#bt = u.padding(bt,'center',width = 'clip')
#bt = u.Filler(bt, 'top')
#loop.widget.original_widget = u.Filler(u.Pile([]))
#
#div = u.Divider()
#damn = u.Attr(div,'dam')
#pile = loop.widget.base_widget
#for item in [placeholder,damn,bt]:
#    pile.contents.append((item.pile.options()))
#loop.run()



#bt = u.BigText(" HelloWorld  v2.0 ",  u.font.HalfBlock5x4Font())
#bt = u.Padding(bt, 'left', width='clip')
#bt = u.Filler(bt, 'bottom')
#
#loop = u.MainLoop(bt,unhandled_input=exit)
#loop.run()

