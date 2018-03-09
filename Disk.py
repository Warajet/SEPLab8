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
        t.fd(self.w/2)
        t.lt(90)
        t.fd(self.h)
        t.lt(90)
        t.fd(self.w)
        t.lt(90)
        t.fd(self.h)
        t.lt(90)
        t.fd(self.w/2)

    def newpos(self, x, y):
        self.x = x
        self.y = y

    def cleardisk(self):
        t.pu()
        t.setpos(self.x, self.y)
        t.seth(0)
        t.pd()
        t.pencolour("white")
        t.fd(self.w / 2)
        t.lt(90)
        t.fd(self.h)
        t.lt(90)
        t.fd(self.w)
        t.lt(90)
        t.fd(self.h)
        t.lt(90)
        t.fd(self.w / 2)
