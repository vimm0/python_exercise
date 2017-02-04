import urwid

header = urwid.Text("Your header stuff goes here")
user_input = urwid.Edit("Type things here ->","")
status_bar = urwid.Text("Everything is just great")
footer = urwid.Pile( [user_input, status_bar], focus_item=0 )
content_list = [urwid.Text("content goes here")]
content = urwid.ListBox( content_list )
frame = urwid.Frame( content, header, footer, focus_part='footer' )

