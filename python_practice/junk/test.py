import urwid
def render(self, size, focus=False):
               fixed_size(size) # complain if parameter is wrong
               a = None
               ai = ak = 0
               o = []
               rows = self.font.height
               attrib = self.attrib+[(None,len(self.text))]
               for ch in self.text:
                      if not ak:
                             a, ak = attrib[ai]
                             ai += 1
                      ak -= 1
                      width = self.font.char_width(ch)
                      if not width:
                             # ignore invalid characters
                             continue
                      c = self.font.render(ch)
                      if a is not None:
                             c = CompositeCanvas(c)
                             c.fill_attr(a)
                      o.append((c, None, False, width))
               if o:
                      canv = CanvasJoin(o)
               else:
                      canv = TextCanvas([""]*rows, maxcol=0,
                             check_width=False)
                      canv = CompositeCanvas(canv)
               canv.set_depends([])
               return canv


