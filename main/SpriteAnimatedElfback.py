from processing import *
import math

class AnimatedSpriteElf(object):

    def __init__(self, x, y, w, h, pics_folder, scr_w, scr_h, speed=3):
        self.scr_w, self.scr_h = scr_w, scr_h
        self.x, self.y, self.w, self.h = x, y, w, h
        self.speed, self.rot_angle = speed, 0
        # sprite's states
        self.isMovingRight, self.isMovingLeft, self.isMovingUp, self.isMovingDown = False, False, False, False
        self.isFlying = True
        self.isFacingRight, self.isFacingLeft,self.isFacingUp,self.isFacingDown = True, False, False,False
        self.isMoving = False
        self.isUp, self.isDown, self.isFall, self.isHit = False, True, False, False
        self.isEval = False

        self.start_x, self.start_y = x, y
        self.trail_x, self.trail_y, self.trail_deg = x, y, 0
        self.speed = speed
        self.commands = []
        self.args = []
        
        # touchkey
        self.touchKey = False

        #important: the actual location of the sprite
        self.area = {"top_left":{"x": self.x + 14,          "y": self.y + self.h - 10},
                     "top_right":{"x": self.x + self.w - 14, "y": self.y + self.h - 10},
                     "bottom_left":{"x": self.x + 14,          "y": self.y + self.h},
                     "bottom_right":{"x": self.x + self.w - 14, "y": self.y + self.h}}

        # Final outcomes
        self.isWin, self.isLose = False, False

        #animation pics init
        kadaR1 = loadImage(pics_folder + "/kadaR1.png")
        kadaR2 = loadImage(pics_folder + "/kadaR2.png")
        kadaR3 = loadImage(pics_folder + "/kadaR3.png")
        kadaR4 = loadImage(pics_folder + "/kadaR4.png")
        # kadaR5 = loadImage(pics_folder + "/kada_R5.png")
        # kadaR6 = loadImage(pics_folder + "/kada_R6.png")

        kadaL1 = loadImage(pics_folder + "/kadaL1.png")
        kadaL2 = loadImage(pics_folder + "/kadaL2.png")
        kadaL3 = loadImage(pics_folder + "/kadaL3.png")
        kadaL4 = loadImage(pics_folder + "/kadaL4.png")
        # kadaL5 = loadImage(pics_folder + "/walking/kada_L5.png")
        # kadaL6 = loadImage(pics_folder + "/walking/kada_L6.png")

        kadaU1 = loadImage(pics_folder + "/kadaU1.png")
        kadaU2 = loadImage(pics_folder + "/kadaU2.png")
        kadaU3 = loadImage(pics_folder + "/kadaU3.png")
        kadaU4 = loadImage(pics_folder + "/kadaU4.png")

        kadaD1 = loadImage(pics_folder + "/kadaD1.png")
        kadaD2 = loadImage(pics_folder + "/kadaD2.png")
        kadaD3 = loadImage(pics_folder + "/kadaD3.png")
        kadaD4 = loadImage(pics_folder + "/kadaD4.png")

        kada_U_lose1 = loadImage(pics_folder + "/losing/kada_U_lose1.png")
        kada_U_lose2 = loadImage(pics_folder + "/losing/kada_U_lose2.png")
        kada_U_lose3 = loadImage(pics_folder + "/losing/kada_U_lose3.png")
        kada_U_lose4 = loadImage(pics_folder + "/losing/kada_U_lose4.png")

        kada_D_lose1 = loadImage(pics_folder + "/losing/kada_D_lose1.png")
        kada_D_lose2 = loadImage(pics_folder + "/losing/kada_D_lose2.png")
        kada_D_lose3 = loadImage(pics_folder + "/losing/kada_D_lose3.png")
        kada_D_lose4 = loadImage(pics_folder + "/losing/kada_D_lose4.png")

        kada_R_lose1 = loadImage(pics_folder + "/losing/kada_R_lose1.png")
        kada_R_lose2 = loadImage(pics_folder + "/losing/kada_R_lose2.png")
        kada_R_lose3 = loadImage(pics_folder + "/losing/kada_R_lose3.png")
        kada_R_lose4 = loadImage(pics_folder + "/losing/kada_R_lose4.png")

        kada_L_lose1 = loadImage(pics_folder + "/losing/kada_L_lose1.png")
        kada_L_lose2 = loadImage(pics_folder + "/losing/kada_L_lose2.png")
        kada_L_lose3 = loadImage(pics_folder + "/losing/kada_L_lose3.png")
        kada_L_lose4 = loadImage(pics_folder + "/losing/kada_L_lose4.png")

        self.kada_R = [kadaR1, kadaR2, kadaR3, kadaR4]
        self.kada_L = [kadaL1, kadaL2, kadaL3, kadaL4]
        self.kada_U = [kadaU1, kadaU2, kadaU3, kadaU4]
        self.kada_D = [kadaD1, kadaD2, kadaD3, kadaD4]
        # self.kada_PU = {"R":kada_pu_R,"L":kada_pu_L}

        self.kada_U_lose = [kada_U_lose1, kada_U_lose2, kada_U_lose3, kada_U_lose4]
        self.kada_D_lose = [kada_D_lose1, kada_D_lose2, kada_D_lose3, kada_D_lose4]
        self.kada_L_lose = [kada_L_lose1, kada_L_lose2, kada_L_lose3, kada_L_lose4]
        self.kada_R_lose = [kada_R_lose1, kada_R_lose2, kada_R_lose3, kada_R_lose4]

        self.count = 0
        self.stepSize = 50
        self.lose_counter,self.win_counter = 0,0
        self.curr_imgs = self.kada_R
        image(self.curr_imgs[self.count], self.x, self.y, self.w, self.h)

        self.isFlying = False
        self.isMovingLeft, self.isMovingRight = False, False
        self.isMovingUp, self.isMovingDown = False, False
        self.isFacingLeft, self.isFacingRight = False, True
        self.isFacingUp, self.isFacingDown = False, False
        self.fly_counter = 0
        self.deg = 0
        self.isBackward = False

    def runCode(self):
        if self.isMoving == False:
            if len(self.commands) > 0:
                command, arg = self.commands.pop(0), self.args.pop(0)
                if command == "F":
                    self.__forwardT(arg)
                if command == "B":
                    self.__backwardT(arg)
                if command == "U":
                    self.__penupT()
                if command == "D":
                    self.__pendownT()
                if command == "L":
                    self.__leftT(arg)
                if command == "R":
                    self.__rightT(arg)
                    
    def goto(self,gx,gy):
        gox = gx + 480.0
        goy = 360 - gy
        #print(self.trail_x,self.trail_y,self.trail_deg,gox,goy)
        if gox == self.trail_x and goy == self.trail_y:return
        godeg = math.degrees(math.atan((goy-self.trail_y)/(gox-self.trail_x)))
        godit = math.sqrt((goy-self.trail_y)*(goy-self.trail_y)+(gox-self.trail_x)*(gox-self.trail_x))
        
        print(self.trail_x,self.trail_y,self.trail_deg,gox,goy,godeg,godit)
        
        if godeg >=0:
            self.left(godeg)
        else:
            self.right(-godeg)
        print(self.commands)
        print(self.args)
        self.forward(godit)

    def forward(self, stepSize):
        self.commands.append("F")
        self.args.append(stepSize)

    def backward(self, stepSize):
        self.commands.append("B")
        self.args.append(stepSize)

    def penup(self):
        self.commands.append("U")
        self.args.append("")

    def pendown(self):
        self.commands.append("D")
        self.args.append("")

    def left(self,deg):
        self.commands.append("L")
        self.args.append(deg)

    def right(self,deg):
        self.commands.append("R")
        self.args.append(deg)

    def __forwardT(self, stepSize):
        if self.isMoving == False:
            self.isMoving = True
            self.stepSize = stepSize
            self.count = 0
            self.isBackward = False
            if self.deg >= 0 and self.deg < 90:
                self.isMovingLeft, self.isMovingRight = False, True
                self.isMovingUp, self.isMovingDown = True, False
            if self.deg >= 90 and self.deg < 180:
                self.isMovingLeft, self.isMovingRight = True, False
                self.isMovingUp, self.isMovingDown = True, False
            if self.deg >= 180 and self.deg < 270:
                self.isMovingLeft, self.isMovingRight = True, False
                self.isMovingUp, self.isMovingDown = False, True
            if self.deg >= 270 and self.deg < 360:
                self.isMovingLeft, self.isMovingRight = False, True
                self.isMovingUp, self.isMovingDown = False, True

            self.start_x = self.x
        pass

    def __backwardT(self, stepSize):
        if self.isMoving == False:
            self.isMoving = True
            self.stepSize = stepSize
            self.isBackward = True
            self.count = 0
            if self.deg >= 0 and self.deg < 90:
                self.isMovingLeft, self.isMovingRight = True, False
                self.isMovingUp, self.isMovingDown = False, True
            if self.deg >= 90 and self.deg < 180:
                self.isMovingLeft, self.isMovingRight = False, True
                self.isMovingUp, self.isMovingDown = False, True
            if self.deg >= 180 and self.deg < 270:
                self.isMovingLeft, self.isMovingRight = False, True
                self.isMovingUp, self.isMovingDown = True, False
            if self.deg >= 270 and self.deg < 360:
                self.isMovingLeft, self.isMovingRight = True, False
                self.isMovingUp, self.isMovingDown = True, False

            self.start_x = self.x

    def __penupT(self):
        self.count = 0
        self.isFlying = True

    def __pendownT(self):
        self.count = 0
        self.isFlying = False

    def __leftT(self,deg):
        if self.isMoving == False:
            self.count = 0
            self.deg += deg
            if self.deg == 360:
                self.deg = 0
            if self.deg > 360:
                self.deg %= 360

            if self.deg > 315 and self.deg <= 360 or self.deg <= 45:
                self.isFacingUp, self.isFacingDown = False, False
                self.isFacingLeft,self.isFacingRight = False,True
            elif self.deg > 45 and self.deg <= 135:
                self.isFacingUp, self.isFacingDown = True, False
                self.isFacingLeft,self.isFacingRight = False,False
            elif self.deg > 135 and self.deg <= 225:
                self.isFacingUp, self.isFacingDown = False, False
                self.isFacingLeft,self.isFacingRight = True,False
            elif self.deg > 225 and self.deg <= 315:
                self.isFacingUp, self.isFacingDown = False, True
                self.isFacingLeft,self.isFacingRight = False,False
            else:
                self.isFacingUp, self.isFacingDown = False, False
                self.isFacingLeft, self.isFacingRight = False, True
            pass

    def __rightT(self,deg):
        if self.isMoving == False:
            self.count = 0
            self.deg -= deg
            if self.deg < 0:
                self.deg += 360
            if self.deg > 315 and self.deg <= 360 or self.deg <= 45:
                self.isFacingUp, self.isFacingDown = False, False
                self.isFacingLeft,self.isFacingRight = False,True
            elif self.deg > 45 and self.deg <= 135:
                self.isFacingUp, self.isFacingDown = True, False
                self.isFacingLeft,self.isFacingRight = False,False
            elif self.deg > 135 and self.deg <= 225:
                self.isFacingUp, self.isFacingDown = False, False
                self.isFacingLeft,self.isFacingRight = True,False
            elif self.deg > 225 and self.deg <= 315:
                self.isFacingUp, self.isFacingDown = False, True
                self.isFacingLeft,self.isFacingRight = False,False
            else:
                self.isFacingUp, self.isFacingDown = False, False
                self.isFacingLeft, self.isFacingRight = False, True

    def moveUp(self,stepSize):
        if self.isMoving == False:
            self.count = 0
            self.stepSize = stepSize

            self.isMovingLeft,self.isMovingRight = False,False
            self.isMovingUp,isMovingDown = True,False
            self.isFacingLeft, self.isFacingRight = False, False
            self.isFacingUp, self.isFacingDown = True, False

            self.isMoving = True

    def moveDown(self,stepSize):
        if self.isMoving == False:
            self.count = 0
            self.stepSize = stepSize

            self.isMovingLeft, self.isMovingRight = False, False
            self.isMovingUp, self.isMovingDown = False, True
            self.isFacingLeft, self.isFacingRight = False, False
            self.isFacingUp, self.isFacingDown = False, True

            self.isMoving  = True
        pass

    def moveLeft(self,stepSize):
        if self.isMoving == False:
            self.count = 0
            self.stepSize = stepSize

            self.isMovingLeft, self.isMovingRight = True, False
            self.isMovingUp, self.isMovingDown = False, False
            self.isFacingLeft, self.isFacingRight = True, False
            self.isFacingUp, self.isFacingDown = False, False

            self.isMoving = True
            pass

    def moveRight(self,stepSize):
        if self.isMoving == False:
            self.count = 0
            self.stepSize = stepSize

            self.isMovingLeft, self.isMovingRight = False, True
            self.isMovingUp, self.isMovingDown = False, False
            self.isFacingLeft, self.isFacingRight = False, True
            self.isFacingUp, self.isFacingDown = False, False

            self.isMoving = True

    def animationUpdate(self,frameR,frameCounter):

        if self.isFacingLeft:
            if self.isLose:
                self.curr_imgs = self.kada_L_lose
            else:
                if self.isFlying:
                    self.viberation()
                    self.curr_imgs = [self.kada_PU["L"]]
                else:
                    self.curr_imgs = self.kada_L
                    image(self.curr_imgs[self.count], self.x, self.y, self.w, self.h)

        elif self.isFacingRight:
            if self.isLose:
                self.curr_imgs = self.kada_R_lose
            else:
                if self.isFlying:
                    self.viberation()
                    self.curr_imgs = [self.kada_PU["R"]]
                else:
                    self.curr_imgs = self.kada_R
                    image(self.curr_imgs[self.count], self.x, self.y, self.w, self.h)

        elif self.isFacingUp:
            if self.isLose:
                self.curr_imgs = self.kada_U_lose
            else:
                self.curr_imgs = self.kada_U
                image(self.curr_imgs[self.count], self.x, self.y, self.w, self.h)

        elif self.isFacingDown:
            if self.isLose:
                self.curr_imgs = self.kada_D_lose
            else:
                self.curr_imgs = self.kada_D
                image(self.curr_imgs[self.count], self.x, self.y, self.w, self.h)

        if frameCounter % (frameR // 10) == 0:
            if self.isMoving:
                self.count += 1
                if self.count >= len(self.curr_imgs):
                    self.count = 0
            if self.isLose:
                if self.lose_counter < 4:
                    self.count += 1
                    if self.count >= len(self.curr_imgs):
                        self.count = 0
                    self.lose_counter += 1

    def show(self):
        if self.isLose:
            image(self.curr_imgs[self.count], self.x, self.y+10*self.lose_counter,
                  self.w, self.h-14*self.lose_counter)
        else:
            image(self.curr_imgs[self.count],self.x,self.y,
                  self.w, self.h)

    def show_rect(self):
        rect(self.area["top_left"]["x"], self.area["top_left"]["y"],
             self.w - 28, 5)

    def rectUpdate(self):
        self.area = {"top_left": {"x": self.x + 14, "y": self.y + self.h - 10},
                     "top_right": {"x": self.x + self.w - 14, "y": self.y + self.h - 10},
                     "bottom_left": {"x": self.x + 14, "y": self.y + self.h - 5 },
                     "bottom_right": {"x": self.x + self.w - 14, "y": self.y + self.h - 5}}

    def lose(self):
        self.isLose,self.isWin = True,False
        self.isMoving = False
        self.commands = []
        if self.lose_counter == 0:
            self.count = 0
            self.lose_counter += 1
        if self.lose_counter >= 4:
            text("You lost!", self.x, self.y)

    def win(self,frameCounter):
        self.isLose,self.isWin = False,True
        self.isMoving = False
        self.commands = []
        if frameCounter % 4 == 0 and self.win_counter < 12:
            tint(0,1)
            self.show()
            tint(0,0)
            self.win_counter += 1
        if self.win_counter >= 12:
            text("you win!", self.x, self.y)

    def viberation(self):
        if self.fly_counter < 2:
            self.y += 1
            self.fly_counter += 1
        elif self.fly_counter < 4:
            self.y -= 1
            self.fly_counter += 1
        else:
            self.fly_counter = 0

    def direction(self,x,y):
        strokeWeight(3)
        stroke(255,255,0)
        length = 30
        line(
            x+length*math.cos(radians(self.deg)),y-length*math.sin(radians(self.deg)),
            x-length*math.cos(radians(self.deg)),y+length*math.sin(radians(self.deg))
             )
        ellipse(x-length*math.cos(radians(self.deg)),y+length*math.sin(radians(self.deg)),
                10,10)
        textSize(15)
        fill(255,255,0)
        # text("Angle:"+str(self.deg),15,610)
