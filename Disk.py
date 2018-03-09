import turtle as t

class Disk():
    def __init__(self, nm, x, y, h, w, colour):
        self.name = nm
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.colour = colour

    # def showdisk(self):

    def newpos(self, x, y):
        self.x = x
        self.y = y

    # def cleardisk(self):
