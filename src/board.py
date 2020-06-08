class Square:
    def __init__(self, blank=False, final_x=False, final_y=False, initial_x=False, intersection=False, centre_char=" "):
        if blank:
            if initial_x:
                if final_x:
                    self.lines = ["|        " for x in range(4)]
                    if final_y:
                        self.lines.insert(0,"+-------+")
                    elif intersection:
                        self.lines.insert(0,"+       ")
                else:
                    self.lines = ["|       " for x in range(4)]
                    if final_y:
                        self.lines.insert(0,"+-------")
            else:
                if final_x:
                    self.lines = ["         " for x in range(4)]
                    if final_y:
                        self.lines.insert(0,"+-------+")
                else:
                    self.lines = ["        " for x in range(4)]
                    if final_y:
                        self.lines.insert(0,"+-------")
        else:
            if final_x:
                self.lines = ["+-------+",
                            "|       |",
                            f"|   {centre_char}   |",
                            "|       |",
                            ]
                if final_y:
                    self.lines.append("+-------+")
            else:
                self.lines = ["+-------",
                            "|       ",
                            f"|   {centre_char}   ",
                            "|       ",
                            ]
                if final_y:
                    self.lines.append("+-------")