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

        self.credits = menu.Menu(
            "The Royal Game of Ur",
            [
                "By",
                "Jacob Fisher",
                "-- and --",
                "Grzegorz Ciołek",
                "",
                "A Fylek Game",
            ],
            "v0.0.0 (c) Fylek MMXX"
        )

        self.rules = menu.Menu(
            "The Royal Game of Ur",
            [
                "1) On each player's go, they will roll 4 binary dice and sum the total",
                "and then move one of their pips by that total",
                "2) A player must always move only one of their pips by the amount shown on",
                "the dice as long as it is possible — if not the turn is lost",
                "3) A player's pip cannot occupy a space already occupied by",
                "another pip of that same player",
                "4) If a player moves one of their pips to a space occupied by the other player,",
                "the other player's pip must return to the starting position,",
                "as long as it is not a rosette square",
                "5) If a player's pip is moved to a rossette space (denoted by an asterisk),",
                "it cannot be captured and the player rolls the dice again",
                "6) The game ends when a player has gotten all of their pips successfully",
                "round the board. The first player to do this is the winner",
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

    def exit(self,code=0,output=""):
        curses.intrflush(True)
        curses.reset_shell_mode()
        os.system('stty sane')
        if code == 0:
            sys.exit()
        elif code == 1:
            print(output)
            sys.exit(1)

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
            self.exit(1,"Your terminal can't render this ­— try maximising the window. If it is already maximised, try lowering the font size.")
        return stdscr

    def wait_for_input(self,win,acceptable=[]):
        win.nodelay(False)
        key = ""

        while True:
            key = win.getch()
            if key in acceptable or len(acceptable) == 0:
                return key

    def handle_menu(self,stdscr):
        while True:
            key = curses.wrapper(self.wait_for_input,acceptable=[curses.KEY_UP,ord("w"),curses.KEY_DOWN,ord("s"),curses.KEY_ENTER,ord("\r"),ord("\n")])
            if key == curses.KEY_DOWN or key == ord("s"):
                self.menu.selected = (self.menu.selected + 1) % len(self.menu.menu_list)
                key = ""
            if key == curses.KEY_UP or key == ord("w"):
                self.menu.selected = (self.menu.selected - 1) % len(self.menu.menu_list)
                key = ""
            if key == curses.KEY_ENTER or key == ord("\r") or key == ord("\n"):
                break
            self.dump(stdscr)

        current_menu_selection = self.menu.menu_list[self.menu.selected].lower()
        if current_menu_selection == "exit":
            self.exit()
        if current_menu_selection == "credits" or current_menu_selection == "rules":
            self.screen = current_menu_selection
            self.dump(stdscr)
            while True:
                key = curses.wrapper(self.wait_for_input,acceptable=[curses.KEY_ENTER,ord("\r"),ord("\n")])
                if key == curses.KEY_ENTER or key == ord("\r") or key == ord("\n"):
                    self.screen = "menu"
                    self.dump(stdscr)
                    break
        if current_menu_selection[:4] == "play":
            self.screen = "board"
            self.dump(stdscr)

    def dump(self,stdscr):
        stdscr.clear()
        if self.screen == "menu":
            stdscr.addstr(0,int((self.columns/2)-(len(self.menu.header)/2)),self.menu.header,curses.A_BOLD | curses.color_pair(1))
            for i in range(len(self.menu.menu_list)):
                if i == self.menu.selected:
                    stdscr.addstr((i+1)*2,int((self.columns/2)-(len(self.menu.menu_list[i])/2)),self.menu.menu_list[i].upper(),curses.A_STANDOUT)
                else:
                    stdscr.addstr((i+1)*2,int((self.columns/2)-(len(self.menu.menu_list[i])/2)),self.menu.menu_list[i].upper())
            stdscr.addstr(((len(self.menu.menu_list)+1)*2),int((self.columns/2)-(len(self.menu.footer)/2)),self.menu.footer,curses.A_DIM)

        elif self.screen == "credits":
            stdscr.addstr(0,int((self.columns/2)-(len(self.credits.header)/2)),self.credits.header,curses.A_BOLD | curses.color_pair(1))
            for i in range(len(self.credits.menu_list)):
                stdscr.addstr((i+1)*2,int((self.columns/2)-(len(self.credits.menu_list[i])/2)),self.credits.menu_list[i])
            stdscr.addstr(((len(self.credits.menu_list)+1)*2),int((self.columns/2)-(len(self.credits.footer)/2)),self.credits.footer,curses.A_DIM)

        elif self.screen == "rules":
            offset = 0
            stdscr.addstr(0,int((self.columns/2)-(len(self.rules.header)/2)),self.rules.header,curses.A_BOLD | curses.color_pair(1))
            for i in range(len(self.rules.menu_list)):
                if self.rules.menu_list[i][1] == ")":
                    offset += 1
                stdscr.addstr((i+3+offset),int((self.columns/2)-(len(self.rules.menu_list[i])/2)),self.rules.menu_list[i])
            stdscr.addstr(len(self.rules.menu_list)+6+offset,int((self.columns/2)-(len(self.rules.footer)/2)),self.rules.footer,curses.A_DIM)

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
                            self.exit(1,f"{e}: Your terminal can't render this ­— try maximising the window. If it is already maximised, try lowering the font size.")
        stdscr.refresh()

if __name__ == "__main__":
    try:
        r = Renderer()
        stdscr = r.start()
        r.dump(stdscr)
        while r.screen == "menu":
            r.handle_menu(stdscr)
        r.exit()
    except Exception as e:
        # Exit safely
        print(e)
        r.exit()