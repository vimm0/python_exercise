import urwid as u


class MainLoop(u.MainLoop):
    def unhandled_input(self, input):
        if input == 'q':
            raise u.ExitMainLoop()
        elif input == 'p':
            self.screen.stop()
            #run_pager('This is the pager!')
            run_pager(processedtxt)
            self.screen.start()
        else:
            self.txtwidget.set_text(input)
            self.draw_screen()
        return True

def main():
    #print "Running..."
    #run_pager(t)
    #print "Ran."
    #return

    s = u.raw_display.Screen()

    txtwidget = u.Text('Test!')
    widget = u.Filler(txtwidget)

    def handler(inpt):
        if inpt == 'q':
            raise u.ExitMainLoop()
        elif inpt == 'p':
            s.stop()
            #run_pager('This is the pager!')
            run_pager(processedtxt)
            s.start()
        else:
            txtwidget.set_text(inpt)
            s.draw_screen()
        return True

    loop.txtwidget = txtwidget


#bt = u.BigText(" Table Tennis ",  u.font.HalfBlock5x4Font())
#bt = u.Padding(bt, 'center', width='clip')
#bt = u.Filler(bt, 'top')
#div = u.Divider()
#dam = u.AttrMap(div,'dam')
##pile = u.Pile([bt,div,button])
#palette = [
#('dam','dark red','dark blue')
#]
loop = u.MainLoop( widget, screen = s)
loop.run()

if __name__ =='__main__':
   main()
#class Border(urwid.WidgetWrap):
#         def __init__(self, w):
#                 # Define the border characters
#                 tline = bline = urwid.Divider("B")
#                 lline = rline = urwid.SolidFill("B")
#                 tlcorner = urwid.Text("B")
#		 trcorner = blcorner = brcorner = tlcorner
#
#                 top = Columns([ ('fixed', 1, tlcorner),
#                         tline, ('fixed', 1, trcorner) ])
#                 middle = Columns( [('fixed', 1, lline),
#                         w, ('fixed', 1, rline)], box_columns = [0,2],
#                         focus_column = 1)
#                 bottom = Columns([ ('fixed', 1, blcorner),
#                         bline, ('fixed', 1, brcorner) ])
#                 pile = Pile([('flow',top),middle,('flow',bottom)],
#                         focus_item = 1)
#                 WidgetWrap.__init__(self, pile)
