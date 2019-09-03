from processing import *

class Button(object):

    def __init__(self,attr,imgs=[]):
        self.btn_x,self.btn_y,self.btn_w,self.btn_h = attr["btn_x"],attr["btn_y"],attr["btn_w"],attr["btn_h"]
        self.msg_x,self.msg_y,self.msg_w,self.msg_h = attr["msg_x"],attr["msg_y"],attr["msg_w"],attr["msg_h"]
        self.btn = loadImage(imgs[0])
        self.msg = loadImage(imgs[1])
        self.isReleased = False
        self.isOn = False
        self.btnToShow = self.msg

    def show(self,mousex,mousey):
        # print(self.isSmall)
        if mousex in range(self.btn_x, self.btn_x +self.btn_w) and \
                mousey in range(self.btn_y, self.btn_y + self.btn_h):
            image(self.btn, self.btn_x - int(self.btn_w / 4), self.btn_y - int(self.btn_w / 4),
                  int(1.3 * self.btn_w), int(1.3 * self.btn_h))
            image(self.msg, self.msg_x, self.msg_y,self.msg_w,self.msg_h)
        else:
            image(self.btn, self.btn_x, self.btn_y,self.btn_w, self.btn_h)

    def showBtn(self,mousex,mousey):
        if self.isOn == True:
            self.btnToShow = self.btn
        if self.isOn == False:
            self.btnToShow = self.msg

        if mousex in range(self.btn_x, self.btn_x +self.btn_w) and \
                mousey in range(self.btn_y, self.btn_y + self.btn_h):
            image(self.btnToShow, self.btn_x - int(self.btn_w / 4), self.btn_y - int(self.btn_w / 4),
                  int(1.3 * self.btn_w), int(1.3 * self.btn_h))
            return True
        else:
            image(self.btnToShow, self.btn_x, self.btn_y,self.btn_w, self.btn_h)
            return False
