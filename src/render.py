from time import sleep
import curses
import board

stdscr = curses.initscr()
curses.start_color()
board_squares = [[
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

for column in range(len(board_squares)):
    for row in range(len(board_squares[column])):
        for y in range(len(board_squares[column][row].lines)):
            stdscr.addstr((row*4) + y,column*8,board_squares[column][row].lines[y])
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