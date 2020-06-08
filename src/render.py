from time import sleep
import curses
import board
import sys

class Renderer:
    def __init__(self):
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
        return stdscr

    def dump(self, stdscr):
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
                        print(f"{e}: Your terminal can't render this ­— try maximising the window. We can't support monitors below 800x600")
                        sys.exit(1)

        stdscr.refresh()

"""
+-------+-------+-------+
|       |       |       |
|       |       |       |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   *   |       |   *   |
|       |       |       |
+-------+-------+-------+
        |       |        
        |       |        
        |       |        
        +-------+        
        |       |        
        |       |        
        |       |        
+-------+-------+-------+
|       |       |       |
|       |   *   |       |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|       |       |       |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|       |       |       |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   *   |       |   *   |
|       |       |       |
+-------+-------+-------+
"""