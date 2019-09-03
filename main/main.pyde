# 在线编辑器需要导入
# 离线编辑器不需要

from processing import *

from SpriteAnimated import AnimatedSprite
from SpriteAnimatedElf import AnimatedSpriteElf
from Sprite import Sprite
from Button import Button
from Obstacle import Obstacle
import math

alpha = 200
add_library("minim")
def setup():
    global scr_w,scr_h,frameR
    global bgimg,win_img,lose_img
    global obj_key,walls,kada,swamp,monsters, elf,obj_gate
    global btns,isGridOn,frameCounter
    global sounds,panel,attr_panel, minim

    #screen and fr init
    size(960,720)
    scr_w,scr_h = 960,720
    frameR = 30
    frameRate(frameR)
    isGridOn = False

    #auxiliaries:
    attr_panel = {"x":650 ,"y":630 ,"w": 300,"h":100 } # ori: 360x92

    attr_hint_btn = {"btn_x":720,"btn_y":655,"btn_w":60,"btn_h":60,
                 "msg_x":375,"msg_y":230,"msg_w":500,"msg_h":400}

    attr_grid_btn = {"btn_x":830,"btn_y":655,"btn_w":60,"btn_h":60,
                     "msg_x": 0, "msg_y": 0, "msg_w": 0, "msg_h": 0}
    #sprite attributes
    attr_kada = {"x":420,"y":315,"w":50,"h":80,"speed":3}
    attr_key = {"x":280,"y":300,"w":85,"h":85}
    attr_swamp = {"x":590,"y":175,"w":50,"h":45}
    # sprite elf
    attr_elf = {"x":420,"y":205,"w":40,"h":60,"speed":3}
    attr_gate = {"x":850,"y":600,"w":85,"h":85}
    #enemies
    attr_black_spider_1 =   {"x":500,"y":50,"w":60,"h":60,
                           "moves_list":["down","up"],"arg":150,"speed":2}
    # attr_black_spider_2 =   {"x":850,"y":600,"w":60,"h":60,
    #                        "moves_list":["left","right"],"arg":460,"speed":2}
    # attr_red_spider =       {"x":600,"y":640,"w":60,"h":60,
    #                         "moves_list":["left","right"],"arg":300,"speed":3}
    # attr_blue_monster_1 =   {"x":90,"y":81,"w":90,"h":90,
    #                        "moves_list":["down","up"],"arg":500,"speed":4}
    # attr_blue_monster_2 =   {"x":570,"y":373,"w":80,"h":90,
    #                        "moves_list":["down","up"],"arg":500}
    
    #walls' attr
    attr_wall_0 = {"x": 0, "y": 0, "w": 960, "h": 50}
    attr_wall_1 = {"x":0, "y":50, "w":50, "h":670}
    attr_wall_2 = {"x":50, "y":670, "w":350, "h":50}
#    attr_wall_3 = {"x":250, "y":600, "w":150, "h":20}
    attr_wall_4 = {"x":400, "y":670, "w":560, "h":50}
    attr_wall_5 = {"x":910, "y":50, "w":50, "h":540}
    
    
#    attr_wall_6 = {"x":130, "y":80, "w":20, "h":20}
    attr_wall_7 = {"x":195, "y":100, "w":200, "h":40}
    attr_wall_8 = {"x":350, "y":100, "w":50, "h":490}
    
#    attr_wall_9 = {"x":130, "y":550, "w":20, "h":20}
    attr_wall_10 = {"x":195, "y":550, "w":200, "h":40}

    attr_wall_11 = {"x":60, "y":260, "w":150, "h":20}
    attr_wall_12 = {"x":80, "y":245, "w":105, "h":15}
    attr_wall_13 = {"x":135, "y":230, "w":20, "h":15}
    
    attr_wall_14 = {"x":60, "y":370, "w":150, "h":20}
    attr_wall_15 = {"x":80, "y":390, "w":105, "h":15}
    attr_wall_16 = {"x":110, "y":405, "w":45, "h":15}
    
    attr_wall_17 = {"x":50, "y":280, "w":15, "h":90}
    attr_wall_18 = {"x":200, "y":280, "w":15, "h":90}
    
    attr_wall_19 = {"x":555, "y":75, "w":255, "h":85}
    attr_wall_20 = {"x":555, "y":160, "w":320, "h":80}
    attr_wall_21 = {"x":485, "y":240, "w":395, "h":180}
    attr_wall_22 = {"x":500, "y":420, "w":380, "h":20}
    attr_wall_23 = {"x":520, "y":440, "w":360, "h":20}  
    attr_wall_24 = {"x":540, "y":460, "w":340, "h":20}   
    attr_wall_25 = {"x":560, "y":480, "w":320, "h":40}
    attr_wall_26 = {"x":580, "y":520, "w":280, "h":35}

    #load hint
    panel = loadImage("/resources/panel.png")
    hint_btn = Button(attr=attr_hint_btn,
                      imgs=["/resources/q_mark.png", "/resources/hint_msg.png"])
    grid_btn = Button(attr=attr_grid_btn,
                      imgs=["/resources/grid_off.png", "/resources/grid_on.png"])
    btns = {"hint_btn": hint_btn, "grid_btn": grid_btn}

    #lose win/lose images:
    win_img = loadImage("/resources/win.png")
    lose_img = loadImage("/resources/lose.png")

    #load sprite
    kada = AnimatedSprite(x=attr_kada["x"], y=attr_kada["y"],
                          w=attr_kada["w"], h=attr_kada["h"],
                          pics_folder="/resources/kada_moves",
                          scr_w=scr_w, scr_h=scr_h, speed=attr_kada["speed"])
    obj_key = Sprite(x=attr_key["x"], y=attr_key["y"],
                        w=attr_key["w"], h=attr_key["h"],
                        pic="/resources/key.png",isVib=True)
    
    obj_gate = Sprite(x=attr_gate["x"], y=attr_gate["y"],
                        w=attr_gate["w"], h=attr_gate["h"],
                        pic="/resources/blue_monster.png",isVib=False)
    
    swamp = Obstacle(x=attr_swamp["x"], y=attr_swamp["y"],
                        w=attr_swamp["w"], h=attr_swamp["h"],num=-1)
    
    elf = AnimatedSpriteElf(x=attr_elf["x"], y=attr_elf["y"],
                          w=attr_elf["w"], h=attr_elf["h"],
                          pics_folder="/resources/elf_moves",
                          scr_w=scr_w, scr_h=scr_h, speed=attr_elf["speed"])
    

    #enemies:
    black_spider_1 = Sprite(x=attr_black_spider_1["x"], y=attr_black_spider_1["y"],
                        w=attr_black_spider_1["w"], h=attr_black_spider_1["h"],
                            pic="/resources/black_spider.png",
                            moveList=attr_black_spider_1["moves_list"],
                            arg=attr_black_spider_1["arg"],speed=attr_black_spider_1["speed"])
    # black_spider_2 = Sprite(x=attr_black_spider_2["x"], y=attr_black_spider_2["y"],
    #                     w=attr_black_spider_2["w"], h=attr_black_spider_2["h"],
    #                         pic="/resources/black_spider_2.png",
    #                         moveList=attr_black_spider_2["moves_list"],
    #                         arg=attr_black_spider_2["arg"],speed=attr_black_spider_2["speed"])
    # red_spider = Sprite(x=attr_red_spider["x"], y=attr_red_spider["y"],
    #                     w=attr_red_spider["w"], h=attr_red_spider["h"],
    #                     pic="/resources/red_spider.png",
    #                         moveList=attr_red_spider["moves_list"],
    #                         arg=attr_red_spider["arg"],speed=attr_red_spider["speed"])
    # blue_monster_1 = Sprite(x=attr_blue_monster_1["x"], y=attr_blue_monster_1["y"],
    #                     w=attr_blue_monster_1["w"], h=attr_blue_monster_1["h"],
    #                         pic="/resources/blue_monster.png",
    #                         moveList=attr_blue_monster_1["moves_list"],
    #                         arg=attr_blue_monster_1["arg"],speed=attr_blue_monster_1["speed"])
    # blue_monster_2 = Sprite(x=attr_blue_monster_2["x"], y=attr_blue_monster_2["y"],
    #                     w=attr_blue_monster_2["w"], h=attr_blue_monster_2["h"],
    #                         pic="/resources/blue_monster_2.png")
    monsters =  [black_spider_1]


    #walls' init
    wall_0 = Obstacle(x=attr_wall_0["x"], y=attr_wall_0["y"],
                        w=attr_wall_0["w"], h=attr_wall_0["h"],num=0)

    wall_1 = Obstacle(x=attr_wall_1["x"], y=attr_wall_1["y"],
                      w=attr_wall_1["w"], h=attr_wall_1["h"],num=1)

    wall_2 = Obstacle(x=attr_wall_2["x"], y=attr_wall_2["y"],
                      w=attr_wall_2["w"], h=attr_wall_2["h"],num=2)

    # wall_3 = Obstacle(x=attr_wall_3["x"], y=attr_wall_3["y"],
    #                   w=attr_wall_3["w"], h=attr_wall_3["h"],num=3)

    wall_4 = Obstacle(x=attr_wall_4["x"], y=attr_wall_4["y"],
                      w=attr_wall_4["w"], h=attr_wall_4["h"],num=4)

    wall_5 = Obstacle(x=attr_wall_5["x"], y=attr_wall_5["y"],
                      w=attr_wall_5["w"], h=attr_wall_5["h"],num=5)

    # wall_6 = Obstacle(x=attr_wall_6["x"], y=attr_wall_6["y"],
    #                   w=attr_wall_6["w"], h=attr_wall_6["h"],num=6)

    wall_7 = Obstacle(x=attr_wall_7["x"], y=attr_wall_7["y"],
                      w=attr_wall_7["w"], h=attr_wall_7["h"],num=7)

    wall_8 = Obstacle(x=attr_wall_8["x"], y=attr_wall_8["y"],
                      w=attr_wall_8["w"], h=attr_wall_8["h"],num=8)
    
    # wall_9 = Obstacle(x=attr_wall_9["x"], y=attr_wall_9["y"],
    #                   w=attr_wall_9["w"], h=attr_wall_9["h"],num=9)
        
    wall_10 = Obstacle(x=attr_wall_10["x"], y=attr_wall_10["y"],
                      w=attr_wall_10["w"], h=attr_wall_10["h"],num=10)
    
    wall_11 = Obstacle(x=attr_wall_11["x"], y=attr_wall_11["y"],
                      w=attr_wall_11["w"], h=attr_wall_11["h"],num=11)    
    
    
    wall_12 = Obstacle(x=attr_wall_12["x"], y=attr_wall_12["y"],
                      w=attr_wall_12["w"], h=attr_wall_12["h"],num=12)     
    
    wall_13 = Obstacle(x=attr_wall_13["x"], y=attr_wall_13["y"],
                      w=attr_wall_13["w"], h=attr_wall_13["h"],num=13) 
    
    wall_14 = Obstacle(x=attr_wall_14["x"], y=attr_wall_14["y"],
                      w=attr_wall_14["w"], h=attr_wall_14["h"],num=14)    
    
    
    wall_15 = Obstacle(x=attr_wall_15["x"], y=attr_wall_15["y"],
                      w=attr_wall_15["w"], h=attr_wall_15["h"],num=15)     
    
    wall_16 = Obstacle(x=attr_wall_16["x"], y=attr_wall_16["y"],
                      w=attr_wall_16["w"], h=attr_wall_16["h"],num=16) 
    wall_17 = Obstacle(x=attr_wall_17["x"], y=attr_wall_17["y"],
                      w=attr_wall_17["w"], h=attr_wall_17["h"],num=17)     
    
    wall_18 = Obstacle(x=attr_wall_18["x"], y=attr_wall_18["y"],
                      w=attr_wall_18["w"], h=attr_wall_18["h"],num=18) 
    
    wall_19 = Obstacle(x=attr_wall_19["x"], y=attr_wall_19["y"],
                      w=attr_wall_19["w"], h=attr_wall_19["h"],num=19)     
    
    wall_20 = Obstacle(x=attr_wall_20["x"], y=attr_wall_20["y"],
                      w=attr_wall_20["w"], h=attr_wall_20["h"],num=20) 
    wall_21 = Obstacle(x=attr_wall_21["x"], y=attr_wall_21["y"],
                      w=attr_wall_21["w"], h=attr_wall_21["h"],num=21) 
    wall_22 = Obstacle(x=attr_wall_22["x"], y=attr_wall_22["y"],
                      w=attr_wall_22["w"], h=attr_wall_22["h"],num=22) 
    wall_23 = Obstacle(x=attr_wall_23["x"], y=attr_wall_23["y"],
                      w=attr_wall_23["w"], h=attr_wall_23["h"],num=23) 
    wall_24 = Obstacle(x=attr_wall_24["x"], y=attr_wall_24["y"],
                      w=attr_wall_24["w"], h=attr_wall_24["h"],num=24) 
    wall_25 = Obstacle(x=attr_wall_25["x"], y=attr_wall_25["y"],
                      w=attr_wall_25["w"], h=attr_wall_25["h"],num=25)
    wall_26 = Obstacle(x=attr_wall_26["x"], y=attr_wall_26["y"],
                      w=attr_wall_26["w"], h=attr_wall_26["h"],num=26)

    walls = [wall_0,wall_1,wall_2,wall_4,wall_5,wall_7,wall_8,wall_10,
             wall_11,wall_12,wall_13,wall_14,wall_15,wall_16,wall_17,wall_18,wall_19,wall_20,
             wall_21,wall_22,wall_23,wall_24,wall_25,wall_26]

    bgimg = loadImage("/resources/bg.png")
    Chinese = createFont("LiSu", 35)
    textFont(Chinese)

    frameCounter = 0
    minim = Minim(this)
    hit_wall_sound = minim.loadFile("hit_wall.mp3")
    winning_sound = minim.loadFile("winning.mp3")
    losing_sound = minim.loadFile("losing.mp3")
    
    sounds = {"hit_wall":hit_wall_sound,
              "winning":winning_sound,
              "losing":losing_sound
              }
    
    starting_sound = minim.loadFile("starting.mp3")
    starting_sound.play()
    
    
    elf.goto(-60, 290)
    elf.goto(-420,290)
    elf.goto(-150,30)
    
    elf.goto(-420,-270)
    elf.goto(420,-270)
    
    kada.goto(-40, -260)
    kada.goto(420,-260)
    # $start0
    
    
    
    
    
    
    
    
    
    
    # $end0
    
def draw():
    global scr_w,scr_h,frameR
    global bgimg,win_img,lose_img
    global obj_key,walls,kada,swamp,monsters,elf,obj_gate
    global btns,isGridOn,frameCounter
    global sounds,panel,attr_panel


    #run multiple lines
    kada.runCode()
    elf.runCode()
    updateFrame(kada=kada,elf=elf, frameR=frameR, obj_key=obj_key,
                swamp=swamp, walls=walls, monsters=monsters,
                btns=btns,obj_gate = obj_gate,
                win_img=win_img,lose_img=lose_img)

    
    frameCounter += 1
#    pic=loadImage("/resources/blue_monster.png")
#    image(pic, 850, 600)
    pass

def showMouseXY(scr_w,scr_h,coord_type=0):# display the current cord of X and Y
    fill(0)
    point(mouseX,mouseY)
    if coord_type == 0: #origin at the center of the screen
        fill(255)
        textSize(15)
        text("x:"+str(mouseX-480),mouseX+15,mouseY)
        text("y:"+str(360-mouseY),mouseX+60,mouseY)
    else: # processing's default coord-sys
        fill(255)
        textSize(15)
        text("x:" + str(mouseX), mouseX+15, mouseY)
        text("y:" + str(mouseY), mouseX+60, mouseY)

# def move_elf(elf,frameR,walls,swamp,obj_key):
#     gameCollisionDetect(elf,walls,swamp,obj_key=obj_key,frameR=frameR)
#     elf.animationUpdate(frameR=frameR,frameCounter=frameCounter)
#     # kada.show()

#     #move kada w.r.t the degree parameter
#     if elf.isMoving:
#         delta_x,delta_y = 0,0
#         if elf.deg >= 0 and elf.deg < 90:
#             delta_x = elf.speed * math.cos(radians(elf.deg))
#             delta_y = (-1) * elf.speed * math.sin(radians(elf.deg))
#         if elf.deg >= 90 and elf.deg < 180:
#             delta_x = (-1) * elf.speed * math.cos(radians(180-elf.deg))
#             delta_y = (-1) * elf.speed * math.sin(radians(180-elf.deg))
#         if elf.deg >= 180 and elf.deg < 270:
#             delta_x = (-1) * elf.speed * math.cos(radians(elf.deg-180))
#             delta_y = elf.speed * math.sin(radians(elf.deg-180))
#         if elf.deg >= 270 and elf.deg < 360:
#             delta_x = elf.speed * math.cos(radians(360-elf.deg))
#             delta_y = elf.speed * math.sin(radians(360-elf.deg))
#         if elf.isBackward:
#             elf.x -= int(delta_x)
#             elf.y -= int(delta_y)
#         else:
#             elf.x += int(delta_x)
#             elf.y += int(delta_y)
#         distance = math.sqrt( math.pow((elf.x-elf.start_x),2) + math.pow((elf.y-elf.start_y),2))
#         if distance >= elf.stepSize:
#             elf.isMoving = False
#             elf.start_x = kada.x
#             elf.start_y = kada.y

def move_elf(kada,frameR,walls,swamp,obj_key):
    gameCollisionDetect(kada,walls,swamp,obj_key=obj_key,frameR=frameR)
    kada.animationUpdate(frameR=frameR,frameCounter=frameCounter)
    # kada.show()

    #move kada w.r.t the degree parameter
    if kada.isMoving:
        delta_x,delta_y = 0,0
        if kada.deg >= 0 and kada.deg < 90:
            delta_x = kada.speed * math.cos(radians(kada.deg))
            delta_y = (-1) * kada.speed * math.sin(radians(kada.deg))
        if kada.deg >= 90 and kada.deg < 180:
            delta_x = (-1) * kada.speed * math.cos(radians(180-kada.deg))
            delta_y = (-1) * kada.speed * math.sin(radians(180-kada.deg))
        if kada.deg >= 180 and kada.deg < 270:
            delta_x = (-1) * kada.speed * math.cos(radians(kada.deg-180))
            delta_y = kada.speed * math.sin(radians(kada.deg-180))
        if kada.deg >= 270 and kada.deg < 360:
            delta_x = kada.speed * math.cos(radians(360-kada.deg))
            delta_y = kada.speed * math.sin(radians(360-kada.deg))
        if kada.isBackward:
            kada.x -= int(delta_x)
            kada.y -= int(delta_y)
        else:
            kada.x += int(delta_x)
            kada.y += int(delta_y)
        distance = math.sqrt( math.pow((kada.x-kada.start_x),2) + math.pow((kada.y-kada.start_y),2))
        if distance >= kada.stepSize:
            kada.isMoving = False
            kada.start_x = kada.x
            kada.start_y = kada.y



def move_kada(kada,frameR,walls,swamp,obj_key):
    gameCollisionDetect(kada,walls,swamp,obj_key=obj_key,frameR=frameR)
    kada.animationUpdate(frameR=frameR,frameCounter=frameCounter)
    # kada.show()

    #move kada w.r.t the degree parameter
    if kada.isMoving:
        delta_x,delta_y = 0,0
        if kada.deg >= 0 and kada.deg < 90:
            delta_x = kada.speed * math.cos(radians(kada.deg))
            delta_y = (-1) * kada.speed * math.sin(radians(kada.deg))
        if kada.deg >= 90 and kada.deg < 180:
            delta_x = (-1) * kada.speed * math.cos(radians(180-kada.deg))
            delta_y = (-1) * kada.speed * math.sin(radians(180-kada.deg))
        if kada.deg >= 180 and kada.deg < 270:
            delta_x = (-1) * kada.speed * math.cos(radians(kada.deg-180))
            delta_y = kada.speed * math.sin(radians(kada.deg-180))
        if kada.deg >= 270 and kada.deg < 360:
            delta_x = kada.speed * math.cos(radians(360-kada.deg))
            delta_y = kada.speed * math.sin(radians(360-kada.deg))
        if kada.isBackward:
            kada.x -= int(delta_x)
            kada.y -= int(delta_y)
        else:
            kada.x += int(delta_x)
            kada.y += int(delta_y)
        distance = math.sqrt( math.pow((kada.x-kada.start_x),2) + math.pow((kada.y-kada.start_y),2))
        if distance >= kada.stepSize:
            kada.isMoving = False
            kada.start_x = kada.x
            kada.start_y = kada.y

def isCollided(kada,obs): # collision detection
    # Method: check if the corner touches or within each other.
    kada.rectUpdate()
    obs_corners = obs.corners
    res = []
    #check whether the edges are collided
    if (kada.area["top_left"]["x"] in range(obs_corners["top_left"]["x"],obs_corners["top_right"]["x"])) and \
            (kada.area["top_left"]["y"]in range(obs_corners["top_left"]["y"],obs_corners["bottom_left"]["y"])):
        res.append("top_left")
    if (kada.area["top_right"]["x"] in range(obs_corners["top_left"]["x"], obs_corners["top_right"]["x"])) and \
            (kada.area["top_right"]["y"] in range(obs_corners["top_left"]["y"], obs_corners["bottom_left"]["y"])):
        res.append("top_right")
    if (kada.area["bottom_left"]["x"] in range(obs_corners["top_left"]["x"], obs_corners["top_right"]["x"])) and \
            (kada.area["bottom_left"]["y"] in range(obs_corners["top_left"]["y"], obs_corners["bottom_left"]["y"])):
        res.append("bottom_left")
    if (kada.area["bottom_right"]["x"] in range(obs_corners["top_left"]["x"], obs_corners["top_right"]["x"])) and \
            (kada.area["bottom_right"]["y"] in range(obs_corners["top_left"]["y"], obs_corners["bottom_left"]["y"])):
        res.append("bottom_right")
    return res

def gameCollisionDetect(kada,walls,swamp,obj_key,frameR):
    offset = kada.w//8
    kada.show_rect()

    #interaction with walls
    for wall in walls:
        wall.show(alpha)
        res = isCollided(kada,wall)
        if len(res) != 0:
            # sounds["losing"] = minim.loadFile("hit_wall.mp3")
            sounds["hit_wall"].play()
            kada.isMoving = False
            if ("top_left" in res and "top_right" in res):
                kada.y += offset
            if ("bottom_left" in res and "bottom_left" in res):
                kada.y -= offset
            if ("top_right" in res and "bottom_right" in res):
                kada.x -= offset
            if ("top_left" in res or "bottom_left" in res):
                kada.x += offset

    # losing - monsters
    for monster in monsters:
        if isCollided(kada,monster):
            sounds["losing"].play()
            kada.lose()
            kada.isLose = True

    #losing - swamp
    swamp.show()
    isLose = isCollided(kada,swamp)
    if("top_left" in isLose) and ("bottom_left" in isLose) and \
            ("top_right" in isLose) and ("bottom_left" in isLose):
        kada.isLose = True
        kada.lose()

    #winning
    isWin = isCollided(kada,obj_gate)
    if len(isWin) > 0:
        pass
        kada.isWin = True
        
    isTouchkey =  isCollided(kada,obj_key)
    if len(isTouchkey) > 0:
        sounds["item_acquired"] = minim.loadFile("item_acquired.mp3")
        sounds["item_acquired"].play()
        kada.touchKey = True
        
    
#        kada.win()

    #screen edge
    if kada.x + kada.w > scr_w:
        kada.isMoving = False
        kada.x -= offset
    if kada.x < 0:
        kada.isMoving = False
        kada.x += offset
    if kada.y < 0:
        kada.isMoving = False
        kada.y += offset
    if kada.y + kada.w > scr_h:
        kada.isMoving = False
        kada.y -= offset

def updateFrame(kada,elf,obj_key,frameR,walls,swamp,monsters,
                btns,obj_gate,win_img,lose_img):
    global isOverGridBtn,isGridOn,frameCounter
    # if elf.touchKey:
    #     pass
    # else:
    #     obj_key.show_counter(frameCounter)
    if kada.isWin and elf.isWin and elf.touchKey:
        sounds["winning"].play()
        if kada.win_counter < 20:
            kada.win_counter += 1
            tint(100,10)
            image(bgimg, 0, 0, scr_w, scr_h)
            obj_key.show_counter(frameCounter)
            obj_gate.show_counter(frameCounter)
            kada.win_counter += 1
        else:
            noTint()
            image(win_img,scr_w//2-50,scr_h//2-150,200,200)
            fill(255)
            textSize(40)
            text(u"闯关成功！你拿到了钥匙！",scr_w//2-200,scr_h//2+125)
    elif kada.isLose or elf.isLose:
        if kada.lose_counter < 20:
            kada.lose_counter += 1
            tint(100,10)
            image(bgimg, 0, 0, scr_w, scr_h)
            kada.show()
            obj_key.show_counter(frameCounter)
            obj_gate.show_counter(frameCounter)
        else:
            noTint()
            image(lose_img,scr_w//2-50,scr_h//2-150,200,200)
            fill(255)
            textSize(40)
            text(u"胜败乃兵家常事，大侠请重新来过！", scr_w // 2-250, scr_h // 2+125)
    else:
        #--elements to show---
        image(bgimg,0,0,scr_w,scr_h)
        stroke(255,255,0)
        # panel  
        image(panel, attr_panel["x"], attr_panel["y"], attr_panel["w"], attr_panel["h"])

        # line(95,0,95,scr_h) # boarder-seperation

        #grid button
        isOverGridBtn = btns["grid_btn"].showBtn(mouseX,mouseY)
        if isGridOn:
            showGrid(scr_w=960,scr_h=720,isDash=True)

        #direction pointer
        # elf.direction(x=40,y=650)
        # textSize(20)
        # text(u"角度:"+str(kada.deg),15,610)

        #objective btn
        if not elf.touchKey:
            obj_key.show_counter(frameCounter)
        obj_gate.show_counter(frameCounter)

        #monsters
        for monster in monsters:
            monster.movePath()

        #showMouseXY
        showMouseXY(scr_w-100,scr_h-100,coord_type=0) # 0 for traditional coord; 1 for processing coord

        #move_kada
        move_kada(kada=kada,frameR=frameR,walls=walls,swamp=swamp,obj_key=obj_key)
        move_elf(kada=elf,frameR=frameR,walls=walls,swamp=swamp,obj_key=obj_key)
        #hint and objective btns
        btns["hint_btn"].show(mouseX,mouseY)
        # btns["obj_btn"].show(mouseX,mouseY)


def showGrid(scr_w,scr_h,isDash=False,interval=5):
    fill(0,500)
    strokeWeight(1)
    stroke(255)
    for x in range(2,scr_w//50+1):
        if isDash:
            y = 0
            while y < scr_h:
                line(50*x,y,50*x,y+interval)
                y += interval*2
        else:
            line(50*x,0,50*x,scr_h)
    for y in range(1,scr_h//50+1):
        if isDash:
            x = 5*scr_w//50 + 5
            while x < scr_w:
                line(x,50*y,x+interval,50*y)
                x += interval*2
        else:
            line(0,50*y,scr_w,50*y)
    pass

# **inner event func of processing***
# grid on/off event
def mouseReleased():
    global kada
    global btns, isGridOn, isOverGridBtn

    if isGridOn and isOverGridBtn:
        btns["grid_btn"].isOn = False
        isGridOn = False
    elif not isGridOn and isOverGridBtn:
        btns["grid_btn"].isOn = True
        isGridOn = True

# ----testing purpose only-----
def keyPressed():
    global kada,obj_key
    stepSize = 50
    if keyCode == RIGHT:
        kada.right(45)
    if keyCode == LEFT:
        kada.left(45)
    if keyCode == DOWN:
        kada.backward(stepSize)
    if keyCode == UP:
        kada.forward(stepSize)
        
    if keyCode == 68: # d
        elf.right(45)
    if keyCode == 65: # a
        elf.left(45)
    if keyCode == 83: # s
        elf.backward(stepSize)
    if keyCode == 87: # w
        elf.forward(stepSize)

# 在线编辑器需要run函数
# 才能正常执行Processing代码
# run()
