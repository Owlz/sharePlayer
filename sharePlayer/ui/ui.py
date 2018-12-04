import logging
logger = logging.getLogger("sharePlayer:UI")

import urwid

url = '(c) https://github.com/bannsec/sharePlayer'

banner = """  ___ / /  ___ ________ / _ \/ /__ ___ _____ ____
 (_-</ _ \/ _ `/ __/ -_) ___/ / _ `/ // / -_) __/
 /___/_//_/\_,_/_/  \__/_/  /_/\_,_/\_, /\__/_/   
                                   /___/          {0}""".format(url)

class UI(object):

    def __init__(self):

        self.full_draw()

    def full_draw(self):
        """Fully recreate and re-draw the screen."""

        #self.frame_header = urwid.Padding(urwid.Text(banner, align='left'), align='center')
        self.frame_header = urwid.Text(banner, align='left')
        self.frame_footer = None

        #self.frame_body = urwid.LineBox(urwid.Filler(urwid.Text("test", wrap="space")), title='Main')
        #self.menu_box = urwid.LineBox( urwid.Text('blerg', align='left'), title='Menu')

        self.menu_widget = urwid.Text('blerg', align='left')
        self.menu_box = urwid.LineBox(urwid.Filler(urwid.Padding(self.menu_widget,width=self.menu_widget.pack()[0]), valign='top'), title="Menu")
        #self.menu_box = urwid.LineBox(urwid.Filler(urwid.Padding(urwid.Text('blerg', align='left'), width=20)), menu='Menu')

        self.chat_widget = urwid.Text('blerg2', align='left')
        self.chat_box =  urwid.LineBox(urwid.Filler(urwid.Padding(self.chat_widget, width='pack'), valign='top'), title="Chat")
        self.input_widget = urwid.Edit(caption='> ')
        self.input_box = urwid.LineBox(urwid.Filler(self.input_widget, valign='bottom', height='pack'))

        self.middle_box = urwid.Pile([self.chat_box, (3, self.input_box)])

        # The far right box, containing whose logged in, and other status sub-boxes
        self.right_box = urwid.LineBox(urwid.Filler(urwid.Padding(urwid.Text('rightbox', align='left'),width='pack'), valign='top'), title="Right")
        
        self.frame_body = urwid.Columns([(self.menu_widget.pack()[0] + 5, self.menu_box), self.middle_box, (40, self.right_box)], dividechars=0)

        self.frame = urwid.Frame(body=self.frame_body, header=self.frame_header, footer=self.frame_footer) #, focus_part='body')
        self.loop = urwid.MainLoop(self.frame, unhandled_input=self._unhandled_input)

        self.loop.run()

    def run(self):
        self.loop.run()

    def _unhandled_input(self, key):
        if key in ('q', 'Q'):
            raise urwid.ExitMainLoop()

        elif key == 'f1':
            import IPython
            IPython.embed()
            self.full_draw()
            #self.search_prompt()

    def search_prompt(self):
        popup = urwid.LineBox(urwid.Filler(urwid.Padding(urwid.Text("blerg"))), title='hello')

        self.loop.widget = urwid.Overlay(
            popup, self.loop.widget,
            align=("relative", 50),
            valign=("relative",  50),
            width=("relative", 40), height=6) 