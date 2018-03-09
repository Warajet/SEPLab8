import turtle as t

class Disk():
    def __init__(self, nm, x, y, h, w, colour):
        self.name = nm
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.colour = colour

    def showdisk(self):
        t.pu()
        t.setpos(self.x,self.y)
        t.seth(0)
        t.pd()
        for i in range(2):
            t.fd(self.w)
            t.rt()
            t.fd(self.h)
            t.rt()

    def newpos(self, x, y):
        self.x = x
        self.y = y

    # def cleardisk(self):
