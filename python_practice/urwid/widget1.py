import urwid
#It is possible to create a widget that will behave as either a flow widget or
#box widget depending on what is required

class MultiPudding(urwid.Widget):
    _sizing = frozenset(['flow', 'box'])

    def rows(self, size, focus=False):
        return 1
    def render(self, size, focus=False):
        if len(size) == 1:
           (maxcol,) = size
           maxrow = 1
        else:
           (maxcol, maxrow) = size
           num_pudding = maxcol / len("Pudding")
           return urwid.TextCanvas(["Pudding" * num_pudding] * maxrow,maxcol=maxcol)
