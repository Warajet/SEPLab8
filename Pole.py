import turtle as t
class Pole():
    def __init__(self, nm, x, y, th = 1, ln = 50, colour = "black"):
        self.name = nm
        self.stack = []
        self.toppos = 0
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
            t.rt(90)
            t.fd(self.length)
            t.rt(90)

    def pushdisk(self, disk):
        disk.newpos(self.x ,disk.h * self.toppos)
        disk.showdisk()
        self.stack.append(disk)
        self.toppos = self.toppos +  1

    def popdisk(self):
        self.toppos = self.toppos -  1
        self.stack[-1].cleardisk()
        return self.stack.pop()
