class Square:
    def __init__(self, blank=False, final_x=False, final_y=False, initial_x=False, intersection=False, centre_char=" "):
        self.occupied = False
        self.colour = None
        self.blank = blank
        self.final_x = final_x
        self.final_y = final_y
        self.initial_x = initial_x
        self.intersection = intersection
        self.centre_char = centre_char
        if self.blank:
            if self.initial_x:
                if self.final_x:
                    self.lines = ["|        " for x in range(4)]
                    if self.final_y:
                        self.lines.insert(0,"+-------+")
                    elif intersection:
                        self.lines.insert(0,"+       ")
                else:
                    self.lines = ["|       " for x in range(4)]
                    if self.final_y:
                        self.lines.insert(0,"+-------")
            else:
                if self.final_x:
                    self.lines = ["         " for x in range(4)]
                    if self.final_y:
                        self.lines.insert(0,"+-------+")
                else:
                    self.lines = ["        " for x in range(4)]
                    if self.final_y:
                        self.lines.insert(0,"+-------")
        else:
            if self.final_x:
                self.lines = ["+-------+",
                            "|       |",
                            f"|   {self.centre_char}   |",
                            "|       |",
                            ]
                if self.final_y:
                    self.lines.append("+-------+")
            else:
                self.lines = ["+-------",
                            "|       ",
                            f"|   {self.centre_char}   ",
                            "|       ",
                            ]
                if self.final_y:
                    self.lines.append("+-------")
    
    def occupy(self, occupy=True):
        if occupy:
            self.occupied = True
            if not self.blank:
                if self.final_x:
                    self.lines[2] = f"|  ({self.centre_char})  |"
                else:
                    self.lines[2] = f"|  ({self.centre_char})  "
        else:
            self.occupied = False
            if not self.blank:
                if self.final_x:
                    self.lines[2] = f"|   {self.centre_char}  |"
                else:
                    self.lines[2] = f"|   {self.centre_char}   "

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