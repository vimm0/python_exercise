import urwid
import urwid.raw_display
import urwid.web_display

def main():
    text_header = (u"hi!  "
        u"UP / DOWN / PAGE UP / PAGE DOWN scroll.  F8 exits.")
    Radio_Text = [u"Select ",('important', u"one"), ]
    Multiselect_Text = [u"Select ",('important', u"many"), ]
    MultiSelect_Options = [u"Wax", u"Wash", u"Buff", u"Clear Coat", u"Dry",
        u"Racing Stripe"]
    Radio_Options = [u"opt1", u"opt2", u"opt3" ]

    def button_press(button):
        frame.footer = urwid.AttrWrap(urwid.Text(
            [u"Pressed: ", button.get_label()]), 'header')

    radio_button_group = []

    AttrWraps_list = [urwid.AttrWrap(urwid.CheckBox(txt),'buttn','buttnf') for txt in MultiSelect_Options]

    blank = urwid.Divider()
    listbox_content = [
        blank,
        urwid.Padding(urwid.Text(Radio_Text), left=2, right=2,
            min_width=20),
        blank,

        urwid.Padding(urwid.GridFlow(
            [urwid.AttrWrap(urwid.RadioButton(radio_button_group,
                txt), 'buttn','buttnf')
                for txt in Radio_Options],
            23, 7, 1, 'left') ,
            left=3, right=3, min_width=20),
        blank,
        urwid.Padding(urwid.Text(Multiselect_Text), left=2, right=2,
            min_width=20),
        blank,
        urwid.Padding(urwid.GridFlow(
            [urwid.AttrWrap(urwid.CheckBox(txt),'buttn','buttnf')
                for txt in MultiSelect_Options
        ],
            10, 3, 1, 'left') ,
            left=4, right=3, min_width=10),
        blank,
        blank,
        ]

    header = urwid.AttrWrap(urwid.Text(text_header), 'header')
    listbox = urwid.ListBox(urwid.SimpleListWalker(listbox_content))
    frame = urwid.Frame(urwid.AttrWrap(listbox, 'body'), header=header)

    palette = [
        ('body','black','light gray', 'standout'),
        ('reverse','light gray','black'),
        ('header','white','dark red', 'bold'),
        ('important','dark blue','light gray',('standout','underline')),
        ('editfc','white', 'dark blue', 'bold'),
        ('editbx','light gray', 'dark blue'),
        ('editcp','black','light gray', 'standout'),
        ('bright','dark gray','light gray', ('bold','standout')),
        ('buttn','black','dark cyan'),
        ('buttnf','white','dark blue','bold'),
        ]


    # use appropriate Screen class
    if urwid.web_display.is_web_request():
        screen = urwid.web_display.Screen()
    else:
        screen = urwid.raw_display.Screen()

    def unhandled(key):
        if key == 'f8':
            raise urwid.ExitMainLoop()
        if key == 'f5':
            txt = urwid.Text(str( {x.get_label(): x.get_state() for x in AttrWraps_list} ))
            fill = urwid.Filler(txt, 'top')
            loop = urwid.MainLoop(fill)
            loop.run()

    urwid.MainLoop(frame, palette, screen,
        unhandled_input=unhandled).run()

def setup():
    urwid.web_display.set_preferences("Urwid Tour")
    # try to handle short web requests quickly
    if urwid.web_display.handle_short_request():
        return

    main()

if '__main__'==__name__ or urwid.web_display.is_web_request():
    setup()
