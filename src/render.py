from time import sleep
import os
import sys
import curses
import board
import menu

class Renderer:
    def __init__(self):
        self.screen = "menu"

        # Menu
        self.menu = menu.Menu(
            "The Royal Game of Ur",
            [
                "Play online",
                "Play over LAN",
                "Play against AI",
                "Rules",
                "Settings",
                "Credits",
                "Exit",
            ],
            "v0.0.0 (c) Fylek MMXX"
        )

        # Board
        self.board_squares = [[
                board.Square(),
                board.Square(centre_char="*"),
                board.Square(blank=True,final_y=True),
                board.Square(blank=True),
                board.Square(),
                board.Square(),
                board.Square(),
                board.Square(final_y=True,centre_char="*"),
            ],
            [
                board.Square(),
                board.Square(),
                board.Square(),
                board.Square(),
                board.Square(centre_char="*"),
                board.Square(),
                board.Square(),
                board.Square(final_y=True),
            ],
            [
                board.Square(final_x=True),
                board.Square(centre_char="*",final_x=True),
                board.Square(blank=True,final_x=True,final_y=True,initial_x=True),
                board.Square(blank=True,final_x=True,initial_x=True,intersection=True),
                board.Square(final_x=True),
                board.Square(final_x=True),
                board.Square(final_x=True),
                board.Square(centre_char="*",final_x=True,final_y=True),
            ],
        ]

    def start(self):
        stdscr = curses.initscr()
        stdscr.clear()
        curses.def_shell_mode()
        curses.start_color()
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
        rows, columns = os.popen('stty size', 'r').read().split()
        self.rows = int(rows)
        self.columns = int(columns)
        if int(self.rows) < 35 or int(self.columns) < 50:
            curses.intrflush(True)
            curses.reset_shell_mode()
            print("Your terminal can't render this ­— try maximising the window. If it is already maximised, try lowering the font size.")
            sys.exit(1)
        return stdscr

    def wait_for_input(self,win,acceptable=[]):
        win.nodelay(False)
        key = ""

        while True:
            key = win.getkey()
            if key in acceptable or len(acceptable) == 0:
                return key

    def handle_menu(self,stdscr):
        key = ""
        while key != "KEY_ENTER":
            key = curses.wrapper(self.wait_for_input,acceptable=["KEY_UP","KEY_DOWN","KEY_ENTER"])
            if key == "KEY_DOWN" or key == "S":
                self.menu.selected = (self.menu.selected + 1) % len(self.menu.menu_list)
                key = ""
            if key == "KEY_UP" or key == "W":
                self.menu.selected = (self.menu.selected - 1) % len(self.menu.menu_list)
                key = ""
            self.dump(stdscr)

        if self.menu.menu_list[self.menu.selected].lower() == "exit":
            print()
            sys.exit(0)

    def dump(self,stdscr):
        if self.screen == "menu":
            stdscr.addstr(0,int((self.columns/2)-(len(self.menu.header)/2)),self.menu.header,curses.A_BOLD | curses.color_pair(1))
            for i in range(len(self.menu.menu_list)):
                if i == self.menu.selected:
                    stdscr.addstr((i+1)*2,int((self.columns/2)-(len(self.menu.menu_list[i])/2)),self.menu.menu_list[i].upper(),curses.A_STANDOUT)
                else:
                    stdscr.addstr((i+1)*2,int((self.columns/2)-(len(self.menu.menu_list[i])/2)),self.menu.menu_list[i].upper())
            stdscr.addstr(((len(self.menu.menu_list)+1)*2),int((self.columns/2)-(len(self.menu.footer)/2)),self.menu.footer,curses.A_DIM)

        elif self.screen == "board":
            for column in range(len(self.board_squares)):
                for row in range(len(self.board_squares[column])):
                    for y in range(len(self.board_squares[column][row].lines)):
                        square = self.board_squares[column][row]
                        line = square.lines[y]
                        try:
                            if square.occupied and y == 2:
                                stdscr.addstr((row*4) + y,column*8,line[0])
                                stdscr.addstr((row*4) + y,column*8 + 1,line[1:])
                                stdscr.addstr((row*4) + y,column*8 + 1,line[1:],curses.color_pair(1))
                                stdscr.addstr((row*4) + y,column*8 + (len(line)-1),line[len(line)-1:])
                            else:
                                stdscr.addstr((row*4) + y,column*8,line)
                        except curses.error as e:
                            curses.intrflush(True)
                            curses.reset_shell_mode()
                            print(f"{e}: Your terminal can't render this ­— try maximising the window. If it is already maximised, try lowering the font size.")
                            sys.exit(1)
        stdscr.refresh()

if __name__ == "__main__":
    r = Renderer()
    stdscr = r.start()
    r.dump(stdscr)
    r.handle_menu(stdscr)