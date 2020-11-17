import pygame, sys
from pygame.locals import *
import random
import time
import os


# 存档点
class S_place(pygame.sprite.Sprite):
    i = 1
    init_location = 0
    type_sprite = 4  # 存档
    wh = 0, 0

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./save.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (80, 40))
        self.rect = self.image.get_rect()
        self.wh = self.image.get_size()
        player.group_prop.add(self)

    def update(self):

        if self.i:
            self.init_location = self.rect[0]
            self.i = self.i - 1
        else:
            self.rect.left = self.init_location + background.rect[0]


# 存档
def Save():
    if player.Check_p > Load():
        txt1 = open("./存档.txt", "w")
        txt1.write(str(player.Check_p0 + 1))
        txt1.close()
        print('存档成功')


# 读档
def Load():
    book_b0 = open("./存档.txt", 'r', encoding='gbk')
    book_b0 = book_b0.read()
    # player.Check_p=int(book_b0)
    return int(book_b0)


# 开始按键
class Button_save(pygame.sprite.Sprite):
    wh = 0, 0

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./game_start_up.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 20))

        self.rect = self.image.get_rect()
        self.wh = self.image.get_size()
        self.rect.left = 0
        self.rect.top = 20

    def update(self):
        if player.star == 2:
            self.image = pygame.image.load("./game_start_up.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (60, 20))
        if player.star == 2.5:
            self.image = pygame.image.load("./game_start_down.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (60, 20))


# 清空精灵组
def kill_s(content):
    for s in content:
        s.kill()


# 状态机
def blit_game():
    # 绘制游戏运行时候
    if player.star == 0 or player.star == 0.5:
        screen.blit(background.image, background.rect)
        screen.blit(button.image, button.rect)
    elif player.star == 2 or player.star == 2.5:
        screen.blit(background.image, background.rect)
        background.update()
        player.group_npc.update()
        player.group_npc.draw(screen)
        player.group_prop.draw(screen)
        player.group_prop.update()
        player.group_brick.draw(screen)
        player.group_brick.update()
        player.group_bullet.update()
        player.group_bullet.draw(screen)
        player.group_player.update()
        player.group_player.draw(screen)
        screen.blit(drawText("关卡：01" + '     ' + "弹夹：" + str(player.clip) + '     ' + "金币：" + str(player.gold_coin)),
                    (0, 0))

        screen.blit(button_save.image, button_save.rect)
    elif player.star == 1 or player.star == 1.5:
        screen.blit(background.image, background.rect)

        player.group_c_point.draw(screen)
        player.group_c_point.update()


# 关卡按键
class Checkpoint(pygame.sprite.Sprite):
    wh = 0, 0
    C_point = 0

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./Checkpoint.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.wh = self.image.get_size()
        self.rect.left = 240
        self.rect.top = 300

    def update(self):
        pygame.font.init()
        f = pygame.font.Font("站酷庆科黄油体.ttf", 40)
        f_rect = f.render(str(self.C_point), True,
                          pygame.Color(255, 255, 255))  # font.render(content,True,pygame.Color(255,255,255))
        f_position = self.rect.x + 10, self.rect.y - 5
        screen.blit(f_rect, f_position)

    def update0(self):
        if player.star == 1:
            self.image = pygame.image.load("./Checkpoint.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (40, 40))
        if player.star == 1.5:
            self.image = pygame.image.load("./Checkpoint0.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (40, 40))
        # 开始按键


class Button(pygame.sprite.Sprite):
    wh = 0, 0

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./game_start_up.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (120, 40))

        self.rect = self.image.get_rect()
        self.wh = self.image.get_size()
        self.rect.left = 240
        self.rect.top = 300

    def update(self):
        if player.star == 0:
            self.image = pygame.image.load("./game_start_up.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (120, 40))
        if player.star == 0.5:
            self.image = pygame.image.load("./game_start_down.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (120, 40))


# 掉落砖头
class Trap_brick1(pygame.sprite.Sprite):
    i = 1
    init_location = 0
    type_sprite = 2
    wh = 0, 0
    drop = 0
    speed = 0

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./Trap_brick_drop.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (80, 40))
        self.rect = self.image.get_rect()
        self.wh = self.image.get_size()
        player.group_brick.add(self)

    def update(self):

        if self.i:
            self.init_location = self.rect[0]
            self.i = self.i - 1

        else:
            self.rect.left = self.init_location + background.rect[0]
        if 0 < self.rect.right - player.rect.left < player.rect[2] + self.rect[
            2] or 0 < player.rect.right - self.rect.left < player.rect[2] + self.rect[2]:
            self.drop = 1
        if self.drop == 1:
            self.rect.bottom = self.rect.bottom + self.speed
            self.speed = self.speed + 1.2
        if self.rect.bottom > background.sur[1] + 10:
            self.kill()


# 倒刺砖头
class Trap_brick0(pygame.sprite.Sprite):
    i = 1
    init_location = 0
    type_sprite = 2
    wh = 0, 0

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./Trap_brick.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (120, 40))
        self.rect = self.image.get_rect()
        self.wh = self.image.get_size()
        player.group_brick.add(self)

    def update(self):

        if self.i:
            self.init_location = self.rect[0]
            self.i = self.i - 1
        else:
            self.rect.left = self.init_location + background.rect[0]


# 移动砖头
class Move_brick(pygame.sprite.Sprite):
    i = 1
    init_location = 0
    type_sprite = 0
    wh = 0, 0
    speed = 1
    cnt = 0
    old_background = 0

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./block.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (120, 40))
        self.rect = self.image.get_rect()
        self.wh = self.image.get_size()
        player.group_brick.add(self)

    def update(self):

        if self.i:  # 第一次
            self.init_location = self.rect[0]
            self.i = self.i - 1
        if self.old_background != background.rect.left:  # 屏幕有移动
            self.rect.left = self.rect.left + background.rect.left - self.old_background
            self.init_location = self.init_location + background.rect.left - self.old_background
            self.old_background = background.rect.left

        self.rect.left = self.rect.left + self.speed

        if self.rect.left == self.init_location - 20 or self.rect.left == self.init_location + 20:
            self.speed = -self.speed


# 怪物
'''
class Npc(pygame.sprite.Sprite):#Sprite是sprite模块的精灵类，内有很多有用的方法。
    # super(FooChild,self) 首先找到 FooChild 的父类（就是类 FooParent），然后把类 FooChild 的对象转换为类 FooParent 的对象
    old_rect=0
    type_sprite=0
    i=1
    bottom1=448
    init_location=0
    speed=[5,0]#第一个元素是左右移动速度，第二个元素是跳跃速度（只做初始化）
    limit=0
    n=0
    list_key=0
    a=1
    wh=0,0
    #初始化
    def __init__(self):
        #继承父类pygame.sprite.Sprite的__init__()方法
        super().__init__()
        # load函数，返回一个 Surface 对象("./images/background.png")
        self.image = pygame.image.load('./sprite/1.png').convert_alpha() 
        #width,height = self.image.get_size()
        self.wh = self.image.get_size()
        #调整角色大小（变为原来的1/2）
        self.image = pygame.transform.scale(self.image, (self.wh[0]//10,self.wh[1]//10))
        #位置
        self.rect = self.image.get_rect()
        self.rect.bottom=background.sur[0]
        if self.rect.bottom <background.sur[1]:
            self.list_key=1
        self.speed[1]=self.speed[1]+1
    # 随着方向键运动
    def update(self):
        self.jump()
        if background.rect.left-self.old_rect!=0:
            self.rect.left=self.rect.left+(background.rect.left-self.old_rect)
            
            self.old_rect=background.rect.left
        if self.list_key==1:
             self.rect.move_ip(0,-self.speed[1])
        
        
       # 限定player在屏幕中
        
        if self.rect.bottom >=background.sur[1]:
            self.rect.bottom =background.sur[1]
        if player.rect.right<self.rect.left:
            self.rect.move_ip(-self.a,0)
        if player.rect.left>self.rect.right:
            self.rect.move_ip(self.a,0)
        #动图
        self.image = pygame.image.load('./sprite/'+str(self.n+1)+'.png').convert_alpha()
        self.n=self.n+1
        if self.n>7:#n张图片，n-1
            self.n=0
        self.image = pygame.transform.scale(self.image, (self.wh[0]//10,self.wh[1]//10))    
        if random.randint(-50,1)>0:
            self.fire()
    def fire(self):
        # 1. 创建子弹
        #self.rect.bottom=50
        bullet = Bullet()
        # 2. 设置子弹的位置
        bullet.rect.bottom = self.rect.top
        bullet.rect.right = self.rect.right
        # 3. 将子弹添加到子弹组
        player.group_bullet.add(bullet) 
    def jump(self):
        if  self.rect.bottom<=self.bottom1-10:
            self.list_key=1
            if self.speed[1]<=-9:
                pass
            else:
                self.speed[1]=self.speed[1]-1
        else:
            self.list_key=0
            self.rect.bottom=self.bottom1
            '''


# 怪物
class Npc(pygame.sprite.Sprite):  # Sprite是sprite模块的精灵类，内有很多有用的方法。
    # super(FooChild,self) 首先找到 FooChild 的父类（就是类 FooParent），然后把类 FooChild 的对象转换为类 FooParent 的对象
    old_rect = 0
    type_sprite = 0
    i = 1
    bottom1 = 448
    init_location = 0
    speed = [5, 0]  # 第一个元素是左右移动速度，第二个元素是跳跃速度（只做初始化）
    limit = 0
    n = 0
    list_key = 0
    a = 1
    wh = 0, 0

    # 初始化
    def __init__(self):
        # 继承父类pygame.sprite.Sprite的__init__()方法
        super().__init__()
        # load函数，返回一个 Surface 对象("./images/background.png")
        self.image = pygame.image.load('./sprite/1.png').convert_alpha()
        # width,height = self.image.get_size()
        self.wh = self.image.get_size()
        # 调整角色大小（变为原来的1/2）
        self.image = pygame.transform.scale(self.image, (self.wh[0] // 10, self.wh[1] // 10))
        # 位置
        self.rect = self.image.get_rect()
        self.rect.bottom = background.sur[0]
        if self.rect.bottom < background.sur[1]:
            self.list_key = 1
        self.speed[1] = self.speed[1] + 1

    # 随着方向键运动
    def update(self):

        # 动图
        self.image = pygame.image.load('./sprite/' + str(self.n + 1) + '.png').convert_alpha()
        self.n = self.n + 1
        if self.n > 7:  # n张图片，n-1
            self.n = 0
        self.image = pygame.transform.scale(self.image, (self.wh[0] // 10, self.wh[1] // 10))
        if random.randint(-50, 1) > 0:
            self.fire()

    def fire(self):
        # 1. 创建子弹
        # self.rect.bottom=50
        bullet = Bullet()
        # 2. 设置子弹的位置
        bullet.rect.bottom = self.rect.top
        bullet.rect.right = self.rect.right
        # 3. 将子弹添加到子弹组
        player.group_bullet.add(bullet)
    # 子弹


class Bullet(pygame.sprite.Sprite):
    """子弹精灵"""
    k_a1 = 0
    k_a2 = 0
    wh = 0, 0
    i = -1
    init_location = 0
    old_background = 0

    def __init__(self):
        super().__init__()

        # 调用父类方法，设置子弹图片，设置初始速度

        self.image = pygame.image.load("./bullet.png").convert_alpha()

        self.wh = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (self.wh[0] // 3, self.wh[1] // 3))
        self.rect = self.image.get_rect()
        self.k_a1 = k_a[1]
        self.k_a2 = k_a[2]
        old_background = background.rect.left

    def update(self):

        if self.old_background != background.rect.left:  # 屏幕有移动
            # self.rect.left=self.rect.left+(background.rect.left-self.old_background)

            old_background = background.rect.left

        # 调用父类方法，让子弹沿垂直方向飞行
        if self.k_a2 != 0:
            self.rect.move_ip(0, self.k_a2 * 10)
        else:
            self.rect.move_ip(self.k_a1 * 10, 0)
        # 判断子弹是否飞出屏幕
        if self.rect.left < 0 or self.rect.right > background.sur[0]:
            pass


# 弹药箱
class Clip_add(pygame.sprite.Sprite):
    i = 1
    init_location = 0
    wh = 0, 0
    type_sprite = 0

    def __init__(self):
        super().__init__()

        # 调用父类方法，设置子弹图片，设置初始速度

        self.image = pygame.image.load("./clipadd.png").convert_alpha()

        # self.image = pygame.image.load("./clipadd.png").convert_alpha()
        self.wh = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (self.wh[0] // 3, self.wh[1] // 3))
        self.wh = self.image.get_size()
        self.rect = self.image.get_rect()
        player.group_prop.add(self)

    def update(self):
        if self.i:
            self.init_location = self.rect[0]
            self.i = self.i - 1
        else:
            self.rect.left = self.init_location + background.rect[0]

    def get(self):
        player.clip = player.clip + 5
        self.kill()


# 金币
class Gold_coin(pygame.sprite.Sprite):
    """子弹精灵"""
    type_sprite = 0
    i = 1
    init_location = 0
    wh = 0, 0

    def __init__(self):
        super().__init__()

        # 调用父类方法，设置子弹图片，设置初始速度

        self.image = pygame.image.load("./gold coin.png").convert_alpha()
        # self.image = pygame.image.load("./clipadd.png").convert_alpha()
        self.wh = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (self.wh[0], self.wh[1]))
        self.rect = self.image.get_rect()
        player.group_prop.add(self)

    def update(self):
        if self.i:
            self.init_location = self.rect[0]
            self.i = self.i - 1
        else:
            self.rect.left = self.init_location + background.rect[0]

    def get(self):
        player.gold_coin = player.gold_coin + 1
        self.kill()


# 砖头
class Brick(pygame.sprite.Sprite):
    i = 1
    init_location = 0
    type_sprite = 0
    wh = 0, 0

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./block.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (120, 40))
        self.rect = self.image.get_rect()
        self.wh = self.image.get_size()
        player.group_brick.add(self)

    def update(self):

        if self.i:
            self.init_location = self.rect[0]
            self.i = self.i - 1
        else:
            self.rect.left = self.init_location + background.rect[0]


# 水管
class Pipe(pygame.sprite.Sprite):
    init_location = 0
    type_sprite = 0
    wh = 0, 0

    def __init__(self):

        super().__init__()
        self.image = pygame.image.load("./pipe.png").convert_alpha()
        self.wh = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (self.wh[0] * 2, self.wh[1] * 2))
        self.rect = self.image.get_rect()
        self.wh = self.image.get_size()
        self.overlord_flower = self.Overlord_flower()
        player.group_npc.add(self.overlord_flower)
        player.group_brick.add(self)

    def update(self):
        if self.overlord_flower.i:
            self.overlord_flower.rect.bottom = self.rect.bottom - 10
            self.overlord_flower.rect.left = self.rect.right - self.wh[0] / 2 - self.overlord_flower.wh[0] / 2
            self.overlord_flower.i = self.overlord_flower.i - 1
            self.init_location = self.rect[0]
            self.overlord_flower.init_location = self.overlord_flower.rect[0]
        else:
            self.overlord_flower.rect.left = self.overlord_flower.init_location + background.rect[0]
            self.rect.left = self.init_location + background.rect[0]
            if self.overlord_flower.rect.bottom == self.rect.top:
                self.overlord_flower.speed = 0
                self.overlord_flower.cnt = self.overlord_flower.cnt + 1
                if self.overlord_flower.cnt == 50:
                    self.overlord_flower.rect.bottom = self.overlord_flower.rect.bottom + 1
                    self.overlord_flower.cnt = 0
                    self.overlord_flower.speed = 1
            if self.overlord_flower.rect.bottom == self.rect.top or self.overlord_flower.rect.bottom == self.rect.bottom - 10:
                self.overlord_flower.speed = -self.overlord_flower.speed
            self.overlord_flower.rect.move_ip(0, self.overlord_flower.speed)

    class Overlord_flower(pygame.sprite.Sprite):
        init_location = 0
        cnt = 0
        type_sprite = 1
        i = 1
        wh = 0, 0
        speed = 1

        def __init__(self):
            super().__init__()
            self.image = pygame.image.load("./Overlord_flower.png").convert_alpha()
            self.wh = self.image.get_size()
            self.image = pygame.transform.scale(self.image, (self.wh[0] * 3 // 2, self.wh[1] * 3 // 2))
            self.rect = self.image.get_rect()
            self.wh = self.image.get_size()
        # 问号箱


class Box(pygame.sprite.Sprite):
    hit = 0
    suprise_speed = 1
    i = 1
    what = random.randint(0, 1)
    suprise_location = 0
    init_location = 0
    type_sprite = 3
    wh = 0, 0

    def __init__(self):

        super().__init__()

        self.image = pygame.image.load("./box.png").convert_alpha()
        self.wh = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.wh = self.image.get_size()
        if self.what == 0:
            self.suprise = Clip_add()
        elif self.what == 1:
            self.suprise = Gold_coin()
        player.group_brick.add(self)
        player.group_prop.add(self.suprise)

    def update(self):

        if self.i:
            self.suprise.rect.bottom = self.rect.bottom - 10
            self.suprise.rect.left = self.rect.right - self.wh[0] // 2 - self.suprise.wh[0] // 2
            self.i = self.i - 1
            self.init_location = self.rect[0]
            self.suprise_location = self.suprise.rect[0]

        else:
            self.suprise.rect.left = self.suprise_location + background.rect[0]
            self.rect.left = self.init_location + background.rect[0]
            if self.suprise.rect.bottom == self.rect.top:
                self.suprise_speed = 0
            elif self.hit:
                self.suprise.rect.move_ip(0, -self.suprise_speed)


# 背景
class Background(pygame.sprite.Sprite):  # Sprite是sprite模块的精灵类，内有很多有用的方法。
    # super(FooChild,self) 首先找到 FooChild 的父类（就是类 FooParent），然后把类 FooChild 的对象转换为类 FooParent 的对象
    speed = [5, 20]  # 第一个元素是左右移动速度，第二个元素是跳跃速度（只做初始化）
    list_key = [0, 0]
    sur = [0, 0]
    who_move = [0, 0]

    # 初始化
    def __init__(self):
        # 继承父类pygame.sprite.Sprite的__init__()方法
        super().__init__()
        self.image = pygame.image.load("backgruond.png")
        self.sur = self.image.get_size()
        # 调整角色大小（变为原来的1/2）
        self.image = pygame.transform.scale(self.image, (self.sur[0] * 2, self.sur[1] * 2))
        # 位置

        self.rect = self.image.get_rect()
        self.sur = self.image.get_size()

    # 随着方向键运动
    def update(self):
        if self.list_key[1] == 1:
            self.rect.move_ip(-self.speed[0], 0)

        elif self.list_key[0] == 1:
            self.rect.move_ip(self.speed[0], 0)

        # 限定player在屏幕中
        if self.rect.left > 0:
            self.rect.left = 0
        elif self.rect.right <= self.sur[0]:
            self.rect.right = self.sur[0]


# 文字
def drawText(content):
    pygame.font.init()
    font = pygame.font.Font("站酷庆科黄油体.ttf", 15)
    text_sf = font.render(content, True, pygame.Color(255, 255, 255))
    return text_sf


# 初始化地图
def Mam_init(n0):
    brick_left = 0
    x = 1
    list_map = []
    # n0=0#选关
    # n0= input('选关')
    n0 = int(n0)

    # 障碍物类型，高，相对位置（与上一个障碍物的距离），绝对位置(绝对位置为0则看相对位置否则看绝对位置)
    #       0：烟囱     1：砖块     2：补给箱     3：问号箱     4：金币
    if n0 == 0:
        list_map = [
            [1, 0, 0],
            [1, 0, 400],  # [1,0,400]
            [1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0],
            [1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0],
            [1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0],
            [1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0],
            [-1, 0, 0],
            [0, 220, 250], [5, 220, 231],
            [6, 420, 260], [6, 420, 380], [2, 350, 380], [7, 420, 500], [7, 420, 580],
            [7, 420, 660], [8, 40, 600],
        ]

    elif n0 == 1:
        list_map = [
            [1, 0, 0],
            [1, 0, 0],
            [1, 0, 0],  # [1,0,400]
            [1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0],
            [1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0],
            [1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0],
            [1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0],
            [-1, 0, 0],
            [0, 220, 250], [5, 220, 231],
            [6, 420, 260], [6, 420, 380], [2, 350, 380], [7, 420, 500], [7, 420, 580],
            [7, 420, 660], [8, 40, 600],
        ]

    for i in list_map:
        if i[2] == -1:
            brick_left = 0
        else:

            if i[0] == 2:
                brick = Clip_add()
            elif i[0] == 1:
                brick = Brick()
            elif i[0] == 0:
                brick = Pipe()
            elif i[0] == 3:
                brick = Box()
            elif i[0] == 4:
                brick = Gold_coin()
            elif i[0] == 5:
                brick = Move_brick()
            elif i[0] == 6:
                brick = Trap_brick0()
            elif i[0] == 7:
                brick = Trap_brick1()
            elif i[0] == 8:
                brick = S_place()
            elif i[0] == -1:
                x = 0

            brick.rect.bottom = background.sur[1] - i[1]
            if x:
                brick.rect.left = brick_left + i[2]
                brick_left = brick.rect.left + brick.wh[0]
            else:
                brick.rect.bottom = background.sur[1] - i[1]
                brick.rect.left = i[2]
            # 玩家


class Player(pygame.sprite.Sprite):  # Sprite是sprite模块的精灵类，内有很多有用的方法。
    # super(FooChild,self) 首先找到 FooChild 的父类（就是类 FooParent），然后把类 FooChild 的对象转换为类 FooParent 的对象
    Check_p0 = 0  # 正在进行的关卡
    Check_p = 0  # 已经通关的关卡
    star = 0  # 游戏状态#未开始；选关；开始；结束
    speed = [5, 15]  # 第一个元素是左右移动速度，第二个元素是跳跃速度（只做初始化）
    clip = 2000000000000  # 弹夹
    gold_coin = 0  # 金币
    tf_jump = 0  # 值为1的时候在跳跃
    limit = 0  # 限制跳跃次数
    n = 0  # 动态参数
    list_state = [0, 9, 29]
    bottom1 = 100000  # 可落地的坐标
    left1 = [100000, -1]  # 可撞击坐标
    wh = 0, 0  # 角色的长宽
    # 精灵组
    group_c_point = pygame.sprite.Group()
    group_brick = pygame.sprite.Group()
    group_bullet = pygame.sprite.Group()
    group_player = pygame.sprite.Group()
    group_npc = pygame.sprite.Group()
    group_prop = pygame.sprite.Group()
    # group_overlord_flower = pygame.sprite.Group()
    list_key = [0, 0, 0]

    # 初始化
    def __init__(self):
        # 继承父类
        super().__init__()
        # 取图片
        self.image = pygame.image.load('./sprite1/1.png').convert_alpha()
        # 取得图片的尺寸
        self.wh = self.image.get_size()
        # 调整角色大小（变为原来的1/2）
        self.image = pygame.transform.scale(self.image, (self.wh[0] // 4, self.wh[1] // 4))
        # 位置
        self.rect = self.image.get_rect()
        # 把player加入组
        self.group_player.add(self)
        self.Check_p = Load()

    def fire(self):
        # 1. 创建子弹
        bullet = Bullet()
        # 2. 设置子弹的位置
        bullet.rect.bottom = self.rect.centery
        bullet.rect.centerx = self.rect.x + 10
        # 3. 将子弹添加到子弹组
        self.group_bullet.add(bullet)

    def update(self):
        if self.rect.bottom > background.sur[1] + 500:
            self.kill()
        if player.left1[0] == 0 and player.left1[1] == 0 and key[K_LEFT]:
            player.speed[0] = 5
            background.speed[0] = 5
        elif player.left1[0] == 0 and player.left1[1] == 1 and key[K_RIGHT]:
            player.speed[0] = 5
            background.speed[0] = 5
        elif player.left1[0] < player.speed[0]:
            player.speed[0] = player.left1[0]
            background.speed[0] = player.left1[0]
        if self.rect.bottom < self.bottom1:
            self.tf_jump = 1
            self.list_key[0] = 1

        if self.list_key[0] == 1 and self.list_key[1] == 0 and self.list_key[2] == 0 and self.tf_jump:
            self.rect.move_ip(0, -self.speed[1])
        elif self.list_key[2] == 1 and self.list_key[0] == 0:
            self.rect.move_ip(self.speed[0], 0)
        elif self.list_key[1] == 1 and self.list_key[0] == 0:
            self.rect.move_ip(-self.speed[0], 0)
        elif self.list_key[1] == 1 and self.list_key[0] == 1 and self.tf_jump:
            self.rect.move_ip(-self.speed[0], -self.speed[1])
        elif self.list_key[2] == 1 and self.list_key[0] == 1 and self.tf_jump:
            self.rect.move_ip(self.speed[0], -self.speed[1])

        # 边界的关系

        if self.rect.left < 0:
            self.rect.left = 0

        elif self.rect.right > background.sur[0]:
            self.rect.right = background.sur[0]
            # 可落地的坐标

    def jump(self):
        self.list_key[0] = 1
        if self.bottom1 == self.rect.bottom:
            pass


        elif self.bottom1 - self.rect.bottom < abs(self.speed[1]):
            self.speed[1] = -self.bottom1 + self.rect.bottom

        else:
            self.speed[1] = self.speed[1] - 1


# 碰撞检测
def Collide():
    # 英雄和砖块碰撞
    player.left1[0] = 100000
    player.left1[1] = -1
    player.bottom1 = 100000
    for brick1 in player.group_brick:

        if brick1.rect.top >= player.rect.bottom and 0 < player.rect.right - brick1.rect.left < player.rect[2] + \
                brick1.rect[2] and brick1.rect.top <= player.bottom1:
            player.bottom1 = brick1.rect.top
        if 0 < brick1.rect.bottom - player.rect.top < player.rect[3] + brick1.rect[3]:
            if abs(player.rect.right - brick1.rect.left) < abs(player.rect.left - brick1.rect.right) and abs(
                    player.rect.right - brick1.rect.left) < player.left1[0]:
                player.left1[0] = abs(player.rect.right - brick1.rect.left)
                player.left1[1] = 0
            elif abs(player.rect.left - brick1.rect.right) < abs(player.rect.right - brick1.rect.left) and abs(
                    player.rect.left - brick1.rect.right) < player.left1[0]:
                player.left1[0] = abs(player.rect.left - brick1.rect.right)
                player.left1[1] = 1
        if brick1.rect.colliderect(player.rect):

            if brick1.rect.top < player.rect.top < brick1.rect.bottom:
                player.rect.top = brick1.rect.bottom
                player.speed[1] = -5
                player.limit = 2
                if brick1.type_sprite == 3:
                    brick1.hit = 1
                if brick1.type_sprite == 2:
                    player.kill()

            elif player.rect.right > brick1.rect.right:
                # player.rect.left=brick1.rect.right
                background.rect.left = background.rect.left - 5
                background.speed[0] = 0
                player.speed[0] = 0
            elif player.rect.left < brick1.rect.left:
                background.rect.left = background.rect.left + 5
                # player.rect.right=brick1.rect.left
                background.speed[0] = 0
                player.speed[0] = 0

    for prop1 in player.group_prop:
        if pygame.sprite.collide_rect(player, prop1):
            if prop1.type_sprite == 4:
                print('xx')
                if player.Check_p < 9:
                    player.Check_p = player.Check_p + 1
                    Save()
                    prop1.type_sprite = 1
            elif prop1.type_sprite == 0:
                prop1.get()
                prop1.kill()

    # 子弹打怪碰撞
    if k_a[0] == 1 and player.clip:
        player.fire()
        player.clip = player.clip - 1

    if pygame.sprite.groupcollide(player.group_npc, player.group_bullet, True, True):
        pass
    # 英雄和怪物碰撞
    if pygame.sprite.groupcollide(player.group_npc, player.group_player, True, False):
        pass
    if pygame.sprite.groupcollide(player.group_bullet, player.group_brick, True, False):
        pass


# 初始化
pygame.init()
# 背景
background = Background()
# 屏幕对象
screen = pygame.display.set_mode([600, background.rect[3]])  # 尺寸
# 玩家精灵对象
exc=1
while exc:
    # 初始化精灵
    player = Player()
    # 初始化精灵位置
    player.rect.bottom = background.sur[1] - 40
    # 创建按钮对象
    clock = pygame.time.Clock()  # 帧率
    old_ticks = 1  # 随机产生怪物
    n_npc = 1  # 怪物的数量
    '''
    npc = Npc()
    npc.rect.right=200
    npc.rect.bottom=background.sur[1]-250
    player.group_npc .add(npc)
    '''
    k_num = 0
    k_a = [0, 1, 0]
    button = Button()
    button_save = Button_save()
    L = 70
    B = 100
    C = 0
    # 选关卡
    for i in range(10):
        if i <= player.Check_p:
            checkpoint = Checkpoint()
            checkpoint.rect.left = L
            checkpoint.rect.bottom = B
            checkpoint.C_point = C
            L = L + 100
            C = C + 1
            if i % 5 == 4 and i > 0:
                B = B + 100
                L = 70
            player.group_c_point.add(checkpoint)
    # 主循环
    while len(player.group_player):
        # while 1:
        if background.rect.left == 0:
            background.who_move[0] = 1
            background.who_move[1] = 0

        elif background.rect.right == background.sur[0]:
            background.who_move[1] = 1
            background.who_move[0] = 0
        else:
            background.who_move[1] = 0
            background.who_move[0] = 0

        screen.fill([255, 255, 255])
        # 帧率
        clock.tick(30)
        ticks = pygame.time.get_ticks()
        k_space = 0  # 跳跃
        k_a[0] = 0
        k_a[2] = 0  # 攻击
        player.list_key = [0, 0, 0]  # 跳跃，前后
        background.list_key = [0, 0]  # 前后
        # 获得键盘状态

        for event in pygame.event.get():
            if event.type == QUIT:  # 点击右上角的'X'，终止主循环
                pygame.quit()
                os.system('python D:/pythongame/main1.py')
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # 按下'ESC'键，终止主循环
                    pygame.quit()
                    os.system('python D:/pythongame/main1.py')
                    sys.exit()
                if event.key == K_SPACE:
                    k_space = 1

            if event.type == VIDEORESIZE:
                background.sur = event.w, event.h
                screen = pygame.display.set_mode(background.sur, RESIZABLE)

            elif event.type == MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                mouse_x = pos[0]
                mouse_y = pos[1]
                # 开始按钮
                if button.rect.right > mouse_x > button.rect.left and button.rect.bottom > mouse_y > button.rect.top and player.star == 0:
                    player.star = 0.5
                elif (
                        button.rect.right < mouse_x or mouse_x < button.rect.left or button.rect.bottom < mouse_y or mouse_y < button.rect.top) and player.star == 0.5:
                    player.star = 0
                button.update()
                # 存档按钮
                if button_save.rect.right > mouse_x > button_save.rect.left and button_save.rect.bottom > mouse_y > button_save.rect.top and player.star == 2:
                    player.star = 2.5
                elif (
                        button_save.rect.right < mouse_x or mouse_x < button_save.rect.left or button_save.rect.bottom < mouse_y or mouse_y < button_save.rect.top) and player.star == 2.5:
                    player.star = 2
                button_save.update()
                # 选关按钮
                for c_point in player.group_c_point:

                    if c_point.rect.right > mouse_x > c_point.rect.left and c_point.rect.bottom > mouse_y > c_point.rect.top and player.star == 1:
                        player.star = 1.5
                    elif (
                            c_point.rect.right < mouse_x or mouse_x < c_point.rect.left or c_point.rect.bottom < mouse_y or mouse_y < c_point.rect.top) and player.star == 1.5:
                        player.star = 1
                    c_point.update0()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 点击开始按钮
                click = pygame.mouse.get_pressed()
                if button.rect.right > mouse_x > button.rect.left and button.rect.bottom > mouse_y > button.rect.top:

                    if click[0] == 1:
                        player.star = 1
                # 点击存档按钮
                if button_save.rect.right > mouse_x > button_save.rect.left and button_save.rect.bottom > mouse_y > button_save.rect.top and player.star == 2.5:
                    # click =pygame.mouse.get_pressed()
                    if click[0] == 1:
                        print('存档')
                        Save()
                # 点击选关按钮
                for c_point in player.group_c_point:
                    if c_point.rect.right > mouse_x > c_point.rect.left and c_point.rect.bottom > mouse_y > c_point.rect.top:
                        # click =pygame.mouse.get_pressed()
                        if click[0] == 1:
                            # 初始化地图
                            Mam_init(c_point.C_point)
                            player.Check_p0 = c_point.C_point
                            player.star = 2
                            # c_point.f.C_point

        # 获得键盘状态
        key = pygame.key.get_pressed()
        # 移动
        player.speed[0] = 5  # 对移动速度赋值
        background.speed[0] = 5
        # 背景动
        # background.who_move=1：背景在边
        if background.sur[0] // 2 + background.speed[0] > player.rect.left and player.rect.left > background.sur[
            0] // 2 - background.speed[0]:

            if background.who_move[0]:

                if key[K_LEFT]:
                    player.list_key[1] = 1
                else:
                    player.list_key[1] = 0
                if key[K_RIGHT]:
                    background.list_key[0] = 1
                else:
                    background.list_key[0] = 0
            if background.who_move[1]:

                if key[K_RIGHT]:
                    player.list_key[2] = 1
                else:
                    player.list_key[2] = 0
                if key[K_LEFT]:
                    background.list_key[0] = 1
                else:
                    background.list_key[0] = 0
            else:

                if key[K_RIGHT]:
                    background.list_key[1] = 1
                else:
                    background.list_key[1] = 0
                if key[K_LEFT]:
                    background.list_key[0] = 1
                else:
                    background.list_key[0] = 0


        else:

            if key[K_LEFT]:
                player.list_key[1] = 1

            else:
                player.list_key[1] = 0

            if key[K_RIGHT]:

                player.list_key[2] = 1

            else:
                player.list_key[2] = 0

        # 跳跃
        if player.rect.bottom == player.bottom1:
            player.tf_jump = 0
            player.speed[1] = 0
            player.limit = 0
        if k_space == 1 and player.limit < 2:
            player.limit = player.limit + 1
            player.tf_jump = 1
            player.speed[1] = 15

        if player.tf_jump:
            player.jump()
        if key[K_a]:
            k_num = k_num + 1
        if key[K_LEFT]:
            k_a[1] = -1
        elif key[K_RIGHT]:
            k_a[1] = 1
        if key[K_UP]:
            k_a[2] = -1
        elif key[K_DOWN]:
            k_a[2] = 1

        if k_num % 5 == 4:
            k_a[0] = 1
            k_num = 0
        # 碰撞检测
        Collide()
        # 更新玩家
        blit_game()
        pygame.display.flip()
    kill_s(player.group_c_point)
    kill_s(player.group_brick)
    kill_s(player.group_bullet)
    kill_s(player.group_player)
    kill_s(player.group_npc)
    kill_s(player.group_prop)
    background.rect.left = 0
    background.rect.top = 0
