import urwid
txt = urwid.Text(u"Hello World, Sandesh Rana welcome to the terminal user\n"
              u"we agreed her to use this console until we grab the root \n"
                 "******Jai Nepal*******")
fill = urwid.Filler(txt, 'top')
loop = urwid.MainLoop(fill)
loop.run()
