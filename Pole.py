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

    def showpole(self):
        t.pu()
        t.setpos(self.x, self.y)
        t.seth(0)
        t.pd()
        for i in range(2):
            t.fd(self.thickness)
            t.rt()
            t.fd(self.length)
            t.rt()
    #def pushdisk(self, disk):

    #def popdisk(self):

