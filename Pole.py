class Pole():
    def __init__(self, nm, x, y, st = [], tp = 0,  th = 1, ln = 50, colour = "black"):
        self.name = nm
        self.stack = st
        self.toppos = tp
        self.x = x
        self.y = y
        self.thickness = th
        self.length = ln
        self.colour = colour
    
    #def showpole(self):
