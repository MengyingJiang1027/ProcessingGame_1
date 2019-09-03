from processing import *

class Obstacle(object):

    def __init__(self,x,y,w,h,num,offset=0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.num = num
        self.offset = offset
        self.corners = {"top_left":{"x":self.x+self.offset,"y":self.y+self.offset},
                        "bottom_right":{"x":self.x+self.w-self.offset,"y":self.y+self.h-self.offset},
                        "top_right":{"x":self.x+self.w-self.offset,"y":self.y+self.offset},
                        "bottom_left":{"x":self.x+self.offset,"y":self.y+self.h-self.offset}}
        
    def show(self,alpha=100):
        toFill = color(255,255,255,0)
        fill(toFill)
        stroke(255,255,255,alpha)
        strokeWeight(5)
        rect(self.x,self.y,self.w,self.h)
        fill(255)
        textSize(20)
        text(str(self.num),self.x+self.w//2,self.y+self.h//2)
