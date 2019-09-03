from processing import *

class Sprite(object):

    def __init__(self,x,y,w,h,pic,
                 offset=8,isVib=False,moveList=[],arg=0,speed=2):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.isVib = isVib
        self.offset = offset
        # pdb.set_trace()
        self.sprite = loadImage(pic)
        image(self.sprite,self.x,self.y,self.w,self.h)
        self.corners = {"top_left":{"x":self.x+self.offset,"y":self.y+self.offset},
                        "bottom_right":{"x":self.x+self.w-self.offset,"y":self.y+self.h-self.offset},
                        "top_right":{"x":self.x+self.w-self.offset,"y":self.y+self.offset},
                        "bottom_left":{"x":self.x+self.offset,"y":self.y+self.h-self.offset}}
        self.counter = 0
        self.move_counter = 0
        self.speed = speed
        self.start_x,self.start_y = self.x,self.y
        self.move_list,self.arg = moveList,arg
        self.isMoving = False

    def show(self):
        if self.isVib:
            if frameCount % 20 == 0:
                if self.counter < 3:
                    self.y += 1
                    self.counter += 1
                elif self.counter < 6:
                    self.y -= 1
                    self.counter += 1
                else:
                    self.counter = 0
        self.__rectUpdate()
        image(self.sprite,self.x,self.y,self.w,self.h)

    def show_counter(self,frameCounter):
        if self.isVib:
            if frameCounter % 20 == 0:
                if self.counter < 3:
                    self.y += 1
                    self.counter += 1
                elif self.counter < 6:
                    self.y -= 1
                    self.counter += 1
                else:
                    self.counter = 0
        self.__rectUpdate()
        image(self.sprite,self.x,self.y,self.w,self.h)

    def show_rect(self):
        rect(self.corners["top_left"]["x"],self.corners["top_left"]["y"],
             self.w-2*self.offset,self.h-self.offset)

    def __rectUpdate(self,):
        self.corners = {"top_left":{"x":self.x+self.offset,"y":self.y+self.offset},
                        "bottom_right":{"x":self.x+self.w-self.offset,"y":self.y+self.h-self.offset},
                        "top_right":{"x":self.x+self.w-self.offset,"y":self.y+self.offset},
                        "bottom_left":{"x":self.x+self.offset,"y":self.y+self.h-self.offset}}

    def move(self,direction,distance):
        if direction == "left":
            if self.isMoving == False:
                self.x -= self.speed
                if abs(self.x - self.start_x) > distance:
                    self.isMoving = False
                    self.start_x = self.x
                    self.move_counter += 1
        elif direction == "right":
            if self.isMoving == False:
                self.x += self.speed
                if abs(self.x - self.start_x) > distance:
                    self.isMoving = False
                    self.start_x = self.x
                    self.move_counter += 1
        elif direction == "up":
            if self.isMoving == False:
                self.y -= self.speed
                if abs(self.y - self.start_y) > distance:
                    self.isMoving = False
                    self.start_y = self.y
                    self.move_counter += 1
        elif direction == "down":
            if self.isMoving == False:
                self.y += self.speed
                if abs(self.y - self.start_y) > distance:
                    self.isMoving = False
                    self.start_y = self.y
                    self.move_counter += 1
        pass

    def movePath(self):
        self.move(direction=self.move_list[self.move_counter],
                  distance=self.arg)
        # self.move_counter += 1
        if self.move_counter == len(self.move_list):
            self.move_counter = 0
        self.__rectUpdate()
        self.show()
        # self.show_rect()

    #---specifically for chests---#
    def open(self):
        pass
