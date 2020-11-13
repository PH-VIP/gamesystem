import pygame, sys
from pygame.locals import *
import random
import time
from math import *
import math
#大摆锤
def wrap_angle(angle):
        return angle % 360
class Point(object):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    #X property
    def getx(self): return self.__x
    def setx(self, x): self.__x = x
    x = property(getx, setx)

    #Y property
    def gety(self): return self.__y
    def sety(self, y): self.__y = y
    y = property(gety, sety)
class chuizi(pygame.sprite.Sprite):

    type_sprite=2
    i=1
    w,h=0,0
    old_background=0
    radius = 150
    angle = 0.0
    pos = Point(0,0)
    old_pos = Point(0,0)
    init_location=0
    a=0
    b=0
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./bullet.png").convert_alpha() 
        self.image = pygame.transform.scale(self.image, (100,100))
        self.rect = self.image.get_rect()
        self.w,self.h = self.image.get_size()
        player.group_npc.add(self)
        



    def update(self): 
        if self.i:#第一次
            self.a=self.rect[0]
            self.b=self.rect[1]
            #print('1315313513',self.a,self.b)
            self.i=self.i-1
        
        
        #if self.i:#第一次
        
            #print('@',self.rect[0],self.rect[1])
            
        
            
            #self.i=self.i-1
        
        #if self.old_background!=background.rect.left:#屏幕有移动
        if 1:            
            self.angle = wrap_angle(self.angle - 1.5)
            self.pos.x = math.sin( math.radians(self.angle) ) * self.radius
            self.pos.y = math.cos( math.radians(self.angle) ) * self.radius  
           
            self.rect.left=self.a+self.pos.x-self.w//2+background.rect.left
            self.rect.top=self.b+self.pos.y+self.h
        
            #pos.x1 = math.sin( math.radians(-angle) ) * radius
            #pos.y1 = math.cos( math.radians(-angle) ) * radius 
            #chuizi_sprite.position = 2500+x+pos.x-width//2,pos.y+height
            #chuizi_sprite2.position = 2800+x+pos.x1-width//2,pos.y1+height
#上下移动障碍物

class up_down(pygame.sprite.Sprite):

    type_sprite=2
    i=1
    wh=0,0   
    init_location=0
    a=0
    b=0
    speed=5
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./bullet.png").convert_alpha() 
        self.image = pygame.transform.scale(self.image, (80,20))
        self.rect = self.image.get_rect()
        self.w,self.h = self.image.get_size()
        player.group_npc.add(self)





    def update(self): 

        if self.i:#第一次
            self.a=self.rect[0]
            self.b=self.rect[1]       
            self.i=self.i-1
        
        if 1:
            
            if self.b>=128 and self.b<=380:
                self.b+=self.speed
            else:
                self.speed=-self.speed
                self.b+=self.speed
            self.rect.left=self.a+background.rect.left
            self.rect.top=self.b
           
#龙炮
class Battery(pygame.sprite.Sprite):
    i=1
    init_location=[0,0]
    type_sprite=5
    wh=0,0
    speed=1
    cnt=0
    old_background=0
    fir=0
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./long.png").convert_alpha() 
        self.image = pygame.transform.scale(self.image, (60,60))
        self.rect = self.image.get_rect()
        self.wh = self.image.get_size()
        player.group_prop.add(self)
    def update(self): 
        
        if self.i:
            self.init_location=self.rect[0]
            self.i=self.i-1
        else:
            self.rect.left=self.init_location+background.rect[0]
        
        if self.fir%100==0 :
            self.fire()
        self.fir=self.fir+1
    def fire(self):
        # 1. 创建子弹
        #self.rect.bottom=50
        bullet = NPC_Bullet()
        # 2. 设置子弹的位置
        bullet.x1=self.rect.right-self.rect[2]//2-bullet.rect[2]//2
        bullet.y1=self.rect.bottom
        bullet.rect.bottom = self.rect.bottom
        #bullet.rect.right = self.rect.right
        bullet.rect.left=self.rect.right-self.rect[2]//2-bullet.rect[2]//2
        
        # 3. 将子弹添加到子弹组
        player.group_bullet.add(bullet) 
#存档点
class S_place(pygame.sprite.Sprite):
    i=1
    init_location=0
    type_sprite=4#存档
    wh=0,0
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./save.png").convert_alpha() 
        self.image = pygame.transform.scale(self.image, (80,40))
        self.rect = self.image.get_rect()
        self.wh = self.image.get_size()
        player.group_prop.add(self)
    
    def update(self):
            
              
        if self.i:
            self.init_location=self.rect[0]
            self.i=self.i-1
        else:
            self.rect.left=self.init_location+background.rect[0]
#存档
def Save():
    if player.Check_p0==Load():

        txt1 = open("./存档.txt", "w")
        txt1.write(str(player.Check_p0+1)  )
        txt1.close()
#读档
def Load():
    book_b0=open("./存档.txt",'r',encoding='gbk')
    book_b0=book_b0.read()
    #player.Check_p=int(book_b0)
    return int(book_b0)
#开始按键
class Button_save(pygame.sprite.Sprite):
    wh=0,0
    
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./game_back.png").convert_alpha() 
        self.image = pygame.transform.scale(self.image, (90,30))

        self.rect = self.image.get_rect()
        self.wh = self.image.get_size()
        self.rect.left=0
        self.rect.top=20
    def update(self):
        if player.star==2:
            self.image = pygame.image.load("./game_back.png").convert_alpha() 
            self.image = pygame.transform.scale(self.image, (90,30))
        if player.star==2.5:
            self.image = pygame.image.load("./game__back.png").convert_alpha() 
            self.image = pygame.transform.scale(self.image, (90,30))
#清空精灵组
def kill_s(content):
    for s in  content:
        s.kill()
#状态机
def blit_game():
    #绘制游戏运行时候
    if player.star==0 or player.star==0.5:
        screen.blit(background.image,background.rect)
        screen.blit(button.image,button.rect)
    elif player.star==2 or player.star==2.5:
        screen.blit(background.image,background.rect)
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
        screen.blit(drawText("关卡："+str(player.Check_p0)+'     '+"弹夹："+str(player.clip)+'     '+"金币："+str(player.gold_coin)),(0,0))
        
        screen.blit(button_save.image,button_save.rect)
    elif player.star==1 or player.star==1.5:
        screen.blit(background.image,background.rect)

        player.group_c_point.draw(screen)
        player.group_c_point.update()
#关卡按键
class Checkpoint(pygame.sprite.Sprite):
    wh=0,0
    C_point=0
    
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./Checkpoint.png").convert_alpha() 
        self.image = pygame.transform.scale(self.image, (40,40))
        self.rect = self.image.get_rect()
        self.wh = self.image.get_size()
        self.rect.left=240
        self.rect.top=300
       

 

        
    def update(self):
        pygame.font.init()
        f=pygame.font.Font("站酷庆科黄油体.ttf",40)
        f_rect=f.render(str(self.C_point),True,pygame.Color(255,255,255))#font.render(content,True,pygame.Color(255,255,255))
        f_position=self.rect.x+10,self.rect.y-5
        screen.blit(f_rect,f_position)

    def update0(self):
        if player.star==1:
            self.image = pygame.image.load("./Checkpoint.png").convert_alpha() 
            self.image = pygame.transform.scale(self.image, (40,40))
        if player.star==1.5:
            self.image = pygame.image.load("./Checkpoint0.png").convert_alpha() 
            self.image = pygame.transform.scale(self.image, (40,40))         
#开始按键
class Button(pygame.sprite.Sprite):
    wh=0,0
    
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./game_start_up.png").convert_alpha() 
        self.image = pygame.transform.scale(self.image, (120,40))

        self.rect = self.image.get_rect()
        self.wh = self.image.get_size()
        self.rect.left=240
        self.rect.top=300
    def update(self):
        if player.star==0:
            self.image = pygame.image.load("./game_start_up.png").convert_alpha() 
            self.image = pygame.transform.scale(self.image, (120,40))
        if player.star==0.5:
            self.image = pygame.image.load("./game_start_down.png").convert_alpha() 
            self.image = pygame.transform.scale(self.image, (120,40))
#掉落砖头
class Trap_brick_drop(pygame.sprite.Sprite):
    i=1
    init_location=0
    type_sprite=2
    wh=0,0
    drop=0
    speed=0
 
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./Trap_brick_drop.png").convert_alpha() 
        self.image = pygame.transform.scale(self.image, (80,40))
        self.rect = self.image.get_rect()
        self.wh = self.image.get_size()
        player.group_brick.add(self)
    
    def update(self):
            
              
        if self.i:
            self.init_location=self.rect[0]
            self.i=self.i-1
         
        else:
            self.rect.left=self.init_location+background.rect[0]
        if 0<self.rect.right-player.rect.left<player.rect[2]+self.rect[2] or 0<player.rect.right-self.rect.left<player.rect[2]+self.rect[2]:

            self.drop=1
        if self.drop==1:
            self.rect.bottom=self.rect.bottom+self.speed
            self.speed=self.speed+1.2
        if self.rect.bottom>background.sur[1]+10:
            self.kill()
#倒刺砖头
class Trap_brick(pygame.sprite.Sprite):
    i=1
    init_location=0
    type_sprite=2
    wh=0,0
    drop=0
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./Trap_brick.png").convert_alpha() 
        self.image = pygame.transform.scale(self.image, (120,40))
        self.rect = self.image.get_rect()
        self.wh = self.image.get_size()
        player.group_brick.add(self)
    
    def update(self):
            
              
        if self.i:
            self.init_location=self.rect[0]
            self.i=self.i-1
        else:
            self.rect.left=self.init_location+background.rect[0]
        if self.drop==1:
            self.rect.bottom=self.rect.bottom+self.speed
            self.speed=self.speed+1.2
        if self.rect.bottom>background.sur[1]+10:
            self.kill()
#移动砖头
class Move_brick(pygame.sprite.Sprite):
    i=1
    init_location=0
    type_sprite=0
    wh=0,0
    speed=1
    cnt=0
    old_background=0
    
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./Checkpoint1.png").convert_alpha() 
        self.image = pygame.transform.scale(self.image, (120,40))
        self.rect = self.image.get_rect()
        self.wh = self.image.get_size()
        player.group_brick.add(self)





    def update(self): 
        
        if self.i:#第一次
            self.init_location=self.rect[0]
            self.i=self.i-1
        if self.old_background!=background.rect.left:#屏幕有移动
            self.rect.left=self.rect.left+background.rect.left-self.old_background
            self.init_location=self.init_location+background.rect.left-self.old_background
            self.old_background=background.rect.left
        if self.rect.left-player.rect.right<650:
            self.rect.left=self.rect.left+self.speed
            
        if self.rect.left==self.init_location-20 or self.rect.left==self.init_location+20:
            self.speed=-self.speed
#怪物
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
#子弹
class NPC_Bullet(pygame.sprite.Sprite):
    """子弹精灵"""
    type_sprite=1
    wh=0,0
    killself=0
    old_rect=0
    x=0
    y=0
    distance=0
    section=0
    sina=0
    cosa=0
    angle=0
    d_angle=0
    dis_angle=0
    old_angle=0
    velocity=1
    x1=0
    y1=0
    z=0
    z0=0
    def __init__(self):
        super().__init__()

        # 调用父类方法，设置子弹图片，设置初始速度
     
        self.image = pygame.image.load("./bullet.png").convert_alpha() 
        self.wh = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (self.wh[0]//2,self.wh[1]//2))
        self.rect = self.image.get_rect()
    def update(self):
        self.killself=self.killself+1
        
        if self.velocity<8000:
            self.velocity=self.velocity+100
        self.x=player.rect.centerx
        self.y=player.rect.centery
        #print(self.velocity)
        if self.rect.left>self.x:
    
            self.z=1
        else:
            self.z=-1
            
        if self.z!=self.z0 :
            self.velocity=0
            self.z0=self.z
            

        self.distance=sqrt(pow(self.x1-self.x,2)+pow(self.y1-self.y,2))      #两点距离公式
        self.section=self.velocity*1/1000             #每个时间片需要移动的距离
        self.sina=(self.y1-self.y)/self.distance
        self.cosa=(self.x-self.x1)/self.distance
        self.angle=atan2(self.y-self.y1,self.x-self.x1)              #两点线段的弧度值
        self.x1=self.x1+self.section*self.cosa
        self.y1=self.y1-self.section*self.sina
        self.d_angle = degrees(self.angle)        #弧度转角度
        self.rect[0]=self.x1-self.rect[2]
        self.rect[1]=self.y1-self.rect[3]/2
        self.dis_angle=self.d_angle-self.old_angle          #dis_angle就是到下一个位置需要改变的角度
        self.old_angle=self.d_angle    #更新初始角度
            

            
            
        if background.rect.left-self.old_rect!=0:
                self.x1=self.x1+(background.rect.left-self.old_rect)
                self.rect.left=self.rect.left+(background.rect.left-self.old_rect)
                self.old_rect=background.rect.left       
#子弹
class Bullet(pygame.sprite.Sprite):
    """子弹精灵"""
    type_sprite=0
    k_a1=0
    k_a2=0
    wh=0,0
    i=-1
    init_location=0
    old_rect=0
 
    def __init__(self):
        super().__init__()

        # 调用父类方法，设置子弹图片，设置初始速度

     
        self.image = pygame.image.load("./bullet.png").convert_alpha() 
         
        self.wh = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (self.wh[0]//4,self.wh[1]//4))
        self.rect = self.image.get_rect()
        self.k_a1=k_a[1]
        self.k_a2=k_a[2]
        self.old_rect=background.rect.left

    def update(self):
        
        if background.rect.left-self.old_rect!=0:
            self.rect.left=self.rect.left+(background.rect.left-self.old_rect)
            self.old_rect=background.rect.left


        # 调用父类方法，让子弹沿垂直方向飞行
        if self.k_a2!=0:
            self.rect.move_ip(0,self.k_a2*10)
        else:
            self.rect.move_ip(self.k_a1*10,0)
        # 判断子弹是否飞出屏幕
        if self.rect.left<0 or self.rect.right>background.sur[0]:
            self.kill()
#弹药箱
class Clip_add(pygame.sprite.Sprite):
    i=1
    init_location=0
    wh=0,0
    type_sprite=0
    def __init__(self):
        super().__init__()

        # 调用父类方法，设置子弹图片，设置初始速度

        self.image = pygame.image.load("./clipadd.png").convert_alpha()  
        
        #self.image = pygame.image.load("./clipadd.png").convert_alpha() 
        self.wh = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (self.wh[0]//3,self.wh[1]//3))
        self.wh = self.image.get_size()
        self.rect = self.image.get_rect()
        player.group_prop.add(self)
       
    def update(self):
        if self.i:
            self.init_location=self.rect[0]
            self.i=self.i-1
        else:
            self.rect.left=self.init_location+background.rect[0]
    def get(self):
        player.clip=player.clip+1
        self.kill()
#金币
class Gold_coin(pygame.sprite.Sprite):
    """子弹精灵"""
    type_sprite=0
    i=1
    init_location=0
    wh=0,0
    def __init__(self):
        super().__init__()

        # 调用父类方法，设置子弹图片，设置初始速度
        
        self.image = pygame.image.load("./gold coin.png").convert_alpha() 
        #self.image = pygame.image.load("./clipadd.png").convert_alpha() 
        self.wh = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (self.wh[0],self.wh[1]))
        self.rect = self.image.get_rect()
        player.group_prop.add(self)
    def update(self):
        if self.i:
            self.init_location=self.rect[0]
            self.i=self.i-1
        else:
            self.rect.left=self.init_location+background.rect[0]
    def get(self):
        player.gold_coin=player.gold_coin+1
        self.kill()
#钥匙
class Key(pygame.sprite.Sprite):
    """子弹精灵"""
    type_sprite=0
    i=1
    init_location=0
    wh=0,0
    def __init__(self):
        super().__init__()

        # 调用父类方法，设置子弹图片，设置初始速度
        
        self.image = pygame.image.load("./key.png").convert_alpha() 
        #self.image = pygame.image.load("./clipadd.png").convert_alpha() 
        self.wh = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (20,30))
        self.rect = self.image.get_rect()
        player.group_prop.add(self)
    def update(self):
        if self.i:
            self.init_location=self.rect[0]
            self.i=self.i-1
        else:
            self.rect.left=self.init_location+background.rect[0]
    def get(self):
        player.key=player.key+1
        self.kill()
#砖头
class Brick(pygame.sprite.Sprite):
    i=1
    init_location=0
    type_sprite=0
    wh=0,0
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./Checkpoint.png").convert_alpha() 
        self.image = pygame.transform.scale(self.image, (40,40))
        self.rect = self.image.get_rect()
        self.wh = self.image.get_size()
        player.group_brick.add(self)
    
    def update(self):
            
              
        if self.i:
            self.init_location=self.rect[0]
            self.i=self.i-1
        else:
            self.rect.left=self.init_location+background.rect[0]
#水管
class Pipe(pygame.sprite.Sprite):
    init_location=0
    type_sprite=0
    wh=0,0
    def __init__(self):

        super().__init__()
        self.image = pygame.image.load("./pipe.png").convert_alpha() 
        self.wh = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (self.wh[0]*2,self.wh[1]*2))
        self.rect = self.image.get_rect()
        self.wh = self.image.get_size()
        self.overlord_flower=self.Overlord_flower()
        player.group_npc.add(self.overlord_flower)
        player.group_brick.add(self)
    def update(self):
        if self.overlord_flower.i:
            self.overlord_flower.rect.bottom=self.rect.bottom-10
            self.overlord_flower.rect.left=self.rect.right-self.wh[0]/2-self.overlord_flower.wh[0]/2
            self.overlord_flower.i=self.overlord_flower.i-1
            self.init_location=self.rect[0]
            self.overlord_flower.init_location=self.overlord_flower.rect[0]
        else:
            self.overlord_flower.rect.left=self.overlord_flower.init_location+background.rect[0]
            self.rect.left=self.init_location+background.rect[0]
            if self.overlord_flower.rect.bottom==self.rect.top :
                self.overlord_flower.speed=0
                self.overlord_flower.cnt=self.overlord_flower.cnt+1
                if self.overlord_flower.cnt==50:
                    self.overlord_flower.rect.bottom=self.overlord_flower.rect.bottom+1
                    self.overlord_flower.cnt=0
                    self.overlord_flower.speed=1
            if self.overlord_flower.rect.bottom==self.rect.top or self.overlord_flower.rect.bottom==self.rect.bottom-10:
                self.overlord_flower.speed=-self.overlord_flower.speed
            self.overlord_flower.rect.move_ip(0,self.overlord_flower.speed)
    class Overlord_flower(pygame.sprite.Sprite):
        init_location=0
        cnt=0
        type_sprite=1
        i=1
        wh=0,0
        speed=1
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load("./Overlord_flower.png").convert_alpha() 
            self.wh = self.image.get_size()
            self.image = pygame.transform.scale(self.image, (self.wh[0]*3//2,self.wh[1]*3//2))
            self.rect = self.image.get_rect()
            self.wh = self.image.get_size()            
#问号箱
class Box(pygame.sprite.Sprite):
    hit=0
    suprise_speed=1
    i=1
    suprise_location=0
    init_location=0
    type_sprite=3
    wh=0,0
    def __init__(self):
        
        super().__init__()
        
        self.image = pygame.image.load("./box.png").convert_alpha() 
        self.wh = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (40,40))
        self.rect = self.image.get_rect()
        self.wh = self.image.get_size()
    
        if random.randint(-1,0)==0:
            self.suprise=Clip_add()
        else:
            self.suprise=Gold_coin()
        player.group_brick.add(self)
        player.group_prop.add(self.suprise)
        

    def update(self):

        if self.i:
            self.suprise.rect.bottom=self.rect.bottom-10
            self.suprise.rect.left=self.rect.right-self.wh[0]//2-self.suprise.wh[0]//2
            self.i=self.i-1
            self.init_location=self.rect[0]
            self.suprise_location=self.suprise.rect[0]

        else:
            self.suprise.rect.left=self.suprise_location+background.rect[0]
            self.rect.left=self.init_location+background.rect[0]
            if self.suprise.rect.bottom==self.rect.top :
                self.suprise_speed=0
            elif self.hit:
                self.suprise.rect.move_ip(0,-self.suprise_speed)
#背景
class Background(pygame.sprite.Sprite):#Sprite是sprite模块的精灵类，内有很多有用的方法。
    # super(FooChild,self) 首先找到 FooChild 的父类（就是类 FooParent），然后把类 FooChild 的对象转换为类 FooParent 的对象
    speed=[5,20]#第一个元素是左右移动速度，第二个元素是跳跃速度（只做初始化）
    list_key=[0,0]
    sur=[0,0]
    who_move=[0,0]
    next=0#是否过关
    #初始化
    def __init__(self):   
        #继承父类pygame.sprite.Sprite的__init__()方法
        super().__init__()
        self.image = pygame.image.load("backgruond.png")
        self.sur=self.image.get_size()
        #调整角色大小（变为原来的1/2）
        self.image = pygame.transform.scale(self.image, (self.sur[0]*2,self.sur[1]*2))
        #位置

        self.rect = self.image.get_rect()
        self.sur=self.image.get_size()

    # 随着方向键运动
    def update(self):
        if self.list_key[1]==1:
            self.rect.move_ip(-self.speed[0],0)

        elif self.list_key[0]==1:
            self.rect.move_ip(self.speed[0],0)
 



        # 限定player在屏幕中
        if self.rect.left > 0:
            self.rect.left = 0
        elif self.rect.right <= self.sur[0]:
            self.rect.right = self.sur[0]
#文字
def drawText(content):
    pygame.font.init()
    font  =  pygame.font.Font("站酷庆科黄油体.ttf",15)
    text_sf  =  font.render(content,True,pygame.Color(255,255,255))
    return  text_sf 
#初始化地图
def Mam_init(n0):
    brick_left=0
    x=1
    list_map=[]
    n0=int(n0)
    if n0==0:
        list_map=[
                    [1,0,0],                                                          
                    [1,0,480],#[1,0,400]
                    [1,0,0],        [1,0,0],         [1,0,0],         [1,0,0],
                    [1,0,0],                
                    [-1,0,0],       
                    [0,220,250],    [5,220,231],    [1,0,2320],      [1,0,2360],
                    [6,420,260],    [6,420,380],    [2,350,380],     [7,420,500],     [7,420,580],    
                    [7,420,660],    [8,40,2320],    [1,0,2280],      [3,130,800],     [3,260,820],
                    [3,390,840],    [5,390,1150],   [7,500,100],     [5,390,1550],    [0,0,1800], 
                    [6,200,1800],   [9,80,1820],    
                ]
      
    elif n0==1:
        list_map=[
                    [5,0,0],        [5,0,100],        [5,0,100],         [5,0,100],         [5,0,100],                                                         
                    [5,0,100],      [5,0,100],        [5,0,100],         [5,0,100],         [5,0,100],
                    [5,0,100],                     
                    [-1,0,0],
                    [10,400,200],   [7,420,600],      [7,420,2000],       [9,80,1820],       [8,40,2320],
                    [1,0,2280],     [1,0,2320],       [1,0,2360]
                ]
    elif n0==2:
        list_map=[
                    [1,0,0],                                                          
                    [1,0,0],#[1,0,400]
                    [1,0,0],        [1,0,0],         [1,0,0],         [1,0,0],
                    [1,0,0],        [1,0,0],        [1,0,0],         [1,0,0],         [1,0,0],
                    [1,0,0],        [1,0,0],        [1,0,0],         [1,0,0],         [1,0,0],  
                    [1,0,0],        [1,0,0],        [1,0,0],         [1,0,0],         [1,0,0],  
                    [1,0,1100],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],
                    [1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],
                    [1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],
                    [1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],
                    [1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],
                    [1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],
                    [1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],
                    [1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],
                    [1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],
                    [1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],
                    [-1,0,0],
                   
                        
                    [12,300,100],[12,48,250],[12,300,400],[12,48,550],[12,300,700],
                    [5,60,900],[5,100,1100],
                    [11,300,1300],[5,20,1300],[5,60,1500],[5,100,1700],[11,400,1700],
                  [7,420,2020], [7,420,2100], 
                    [8,40,2320],[9,250,427]
                    ]
    elif n0==3:
        list_map=[
                    [1,0,0],        [1,0,0],         [1,0,0],         [1,0,0],                                                          
                    [1,0,0],        [1,0,0],         [1,0,0],         [1,0,0],
                    [1,0,0],        [1,0,0],         [1,0,0],         [1,0,0],
                    [1,0,0],        [1,0,0],         [1,0,0],         [1,0,0],
                    [1,0,0],        [1,0,0],         [1,0,0],         [1,0,0],                                                          
                    [1,0,0],        [1,0,0],         [1,0,0],         [1,0,0],
                    [1,0,0],        [1,0,0],         [1,0,0],         [1,0,0],
                    [1,0,0],        [1,0,0],         [1,0,0],         [1,0,0],
                    [1,0,0],        [1,0,0],         [1,0,0],         [1,0,0],                                                          
                    [1,0,0],        [1,0,0],         [1,0,0],         [1,0,0],
                    [1,0,0],        [1,0,0],         [1,0,0],         [1,0,0],
                    [1,0,0],        [1,0,0],         [1,0,0],         [1,0,0],
                    [1,0,0],        [1,0,0],         [1,0,0],         [1,0,0],
                    [1,0,0],        [1,0,0],         [1,0,0],         [1,0,0],
                    [1,0,0],        [1,0,0],         [1,0,0],         [1,0,0],
                    [1,0,0],        
                    [-1,0,0],       
                    [1,420,1000],[1,380,960],[1,340,960],[1,300,960],[1,260,1000],[1,220,1040],[1,180,1080],
                    [1,220,1120],[1,260,1160],[1,300,1200],[1,340,1200],[1,380,1200],[1,420,1160],[1,380,1120],[1,340,1080],[1,380,1040], 
                ]
    

    for i in list_map:
        if i[2]==-1:
            brick_left=0
        else:

            if i[0]==2:
                brick=Clip_add()
            elif i[0]==1:
                brick=Brick()
            elif i[0]==0:
                brick=Pipe()
            elif i[0]==3:
                brick=Box()
            elif i[0]==4:
                brick=Gold_coin()
            elif i[0]==5:
                brick=Move_brick()
            elif i[0]==6:
                brick=Trap_brick()
            elif i[0]==7:
                brick=Trap_brick_drop()
            elif i[0]==8:
                brick=S_place()
            elif i[0]==9:
                brick=Key()
            elif i[0]==10:
                brick=Battery()
            elif i[0]==11:
                brick=chuizi()
            elif i[0]==12:
                brick=up_down()
            elif i[0]==-1:
                x=0


            brick.rect.bottom=background.sur[1]-i[1]
            if x:
                brick.rect.left=brick_left+i[2]
                brick_left=brick.rect.left+brick.wh[0]
            else:
                brick.rect.bottom=background.sur[1]-i[1]
                brick.rect.left=i[2]        
# 玩家
class Player(pygame.sprite.Sprite):#Sprite是sprite模块的精灵类，内有很多有用的方法。
    # super(FooChild,self) 首先找到 FooChild 的父类（就是类 FooParent），然后把类 FooChild 的对象转换为类 FooParent 的对象
    Check_p0=0#正在进行的关卡
    key=0
    Check_p=0#已经通关的关卡
    star=1#游戏状态#未开始；选关；开始；结束
    speed=[5,15]#第一个元素是左右移动速度，第二个元素是跳跃速度（只做初始化）
    clip=0#弹夹
    gold_coin=0#金币
    tf_jump=0#值为1的时候在跳跃
    limit=0#限制跳跃次数
    n=0#动态参数
    list_state=[0,9,29]
    bottom1=100000#可落地的坐标
    left1=[100000,-1]#可撞击坐标
    wh=0,0#角色的长宽
    #精灵组
    group_c_point = pygame.sprite.Group()
    group_brick = pygame.sprite.Group()
    group_bullet = pygame.sprite.Group()
    group_player = pygame.sprite.Group()
    group_npc = pygame.sprite.Group()
    group_prop = pygame.sprite.Group()
    #group_overlord_flower = pygame.sprite.Group()
    list_key=[0,0,0]
    #初始化
    def __init__(self):   
        #继承父类
        super().__init__()
        #取图片
        self.image = pygame.image.load('./sprite/1.png').convert_alpha()
        #取得图片的尺寸
        self.wh = self.image.get_size()
        #调整角色大小（变为原来的1/2）
        self.image = pygame.transform.scale(self.image, (self.wh[0]//7,self.wh[1]//7))
        #位置
        self.rect = self.image.get_rect()
        #把player加入组
        self.group_player.add(self)
        self.Check_p=Load()

    def fire(self):
        # 1. 创建子弹
        bullet = Bullet()
        # 2. 设置子弹的位置
        bullet.rect.bottom = self.rect.centery
        bullet.rect[0] = self.rect.centerx
        # 3. 将子弹添加到子弹组
        self.group_bullet.add(bullet)
        bullent_sound.play_sound()

    def update(self):
          #动图
        self.image = pygame.image.load('./sprite/'+str(self.n+1)+'.png').convert_alpha()
        self.n=self.n+1
        if self.n>7:#n张图片，n-1
            self.n=0
        self.image = pygame.transform.scale(self.image, (self.wh[0]//7,self.wh[1]//7))  
        if self.rect.bottom>background.sur[1]+500:
            self.kill()
        if player.left1[0]==0 and player.left1[1]==0 and key[K_LEFT]:
            player.speed[0]=5
            background.speed[0]=5
        elif player.left1[0]==0 and player.left1[1]==1 and key[K_RIGHT]:
            player.speed[0]=5
            background.speed[0]=5
        elif player.left1[0]<player.speed[0]:
            player.speed[0]=player.left1[0]
            background.speed[0]=player.left1[0]
        if self.rect.bottom<self.bottom1 :
            self.tf_jump=1
            self.list_key[0]=1
        
        if self.list_key[0]==1 and self.list_key[1]==0 and self.list_key[2]==0 and self.tf_jump:
            self.rect.move_ip(0,-self.speed[1])
        elif self.list_key[2]==1 and self.list_key[0]==0 :
            self.rect.move_ip(self.speed[0],0)
        elif self.list_key[1]==1 and self.list_key[0]==0 :
            self.rect.move_ip(-self.speed[0],0)
        elif self.list_key[1]==1 and self.list_key[0]==1 and self.tf_jump:
            self.rect.move_ip(-self.speed[0],-self.speed[1])    
        elif self.list_key[2]==1 and self.list_key[0]==1  and self.tf_jump:
            self.rect.move_ip(self.speed[0],-self.speed[1])

        

        
       
        #边界的关系
      
        if self.rect.left < 0:
            self.rect.left = 0
            
        elif self.rect.right > background.sur[0]:
            self.rect.right = background.sur[0]
            #可落地的坐标
    
             
        
       
        


            

        
    def jump(self):
            self.list_key[0]=1
            
            if self.bottom1==self.rect.bottom:
               #print('bullent_flag',bullent_flag)
               pass
                
                
            elif self.bottom1-self.rect.bottom<abs(self.speed[1]):
                self.speed[1]=-self.bottom1+self.rect.bottom
                
                
            else:
                self.speed[1]=self.speed[1]-1
#碰撞检测
def Collide():
    #英雄和砖块碰撞
    player.left1[0]=100000
    player.left1[1]=-1
    player.bottom1=100000
    for brick1 in player.group_brick:
        
        if brick1.rect.top>=player.rect.bottom and 0<player.rect.right-brick1.rect.left<player.rect[2]+brick1.rect[2] and brick1.rect.top<=player.bottom1:
            player.bottom1=brick1.rect.top
        if 0<brick1.rect.bottom-player.rect.top<player.rect[3]+brick1.rect[3] :
            if abs (player.rect.right-brick1.rect.left)<abs(player.rect.left-brick1.rect.right) and abs(player.rect.right-brick1.rect.left)<player.left1[0]:
                player.left1[0]=abs(player.rect.right-brick1.rect.left)
                player.left1[1]=0
            elif abs(player.rect.left-brick1.rect.right)<abs(player.rect.right-brick1.rect.left) and abs(player.rect.left-brick1.rect.right)<player.left1[0]:
                player.left1[0]=abs(player.rect.left-brick1.rect.right)
                player.left1[1]=1
        if brick1.rect.colliderect(player.rect):
           
            if  brick1.rect.top<player.rect.top<brick1.rect.bottom:
                player.rect.top=brick1.rect.bottom
                player.speed[1]=-5
                player.limit=2
                if brick1.type_sprite==3:
                    brick1.hit=1
                if brick1.type_sprite==2:
                    player.kill() 
            elif  player.rect.right>brick1.rect.right  :
                #player.rect.left=brick1.rect.right
                background.rect.left=background.rect.left-5
                background.speed[0]=0
                player.speed[0]=0
            elif  player.rect.left<brick1.rect.left:
                background.rect.left=background.rect.left+5
                #player.rect.right=brick1.rect.left
                background.speed[0]=0
                player.speed[0]=0
            if brick1.type_sprite==2 and brick1.rect.top==player.rect.bottom:
                #print('drop')
                brick1.drop=1


          

             
    for prop1 in player.group_prop:
        if pygame.sprite.collide_rect(player, prop1):
            if prop1.type_sprite==4and player.key!=0:
                if player.Check_p<9:
                    player.Check_p=player.Check_p+1
                    Save()
                    prop1.type_sprite=1
                    background.next=1
                    player.kill()
                    
            elif prop1.type_sprite==5:
                pass

            elif prop1.type_sprite==0:
                prop1.get()
                prop1.kill()
           
    #子弹打怪碰撞
    if k_a[0]==1 and player.clip:
        player.fire()
        player.clip=player.clip-1
    for bullet1 in player.group_bullet:  
        if bullet1.type_sprite==1:
            if pygame.sprite.spritecollide(bullet1,player.group_player,True):
                bullet1.kill()
        if bullet1.type_sprite==0:
            for npc1 in player.group_npc:
                if pygame.sprite.collide_rect(bullet1, npc1) and npc1.type_sprite==1:
                    bullet1.kill()
                    npc1.kill()
                elif pygame.sprite.collide_rect(bullet1, npc1):
                    bullet1.kill()



        pass
    #英雄和怪物碰撞
    if pygame.sprite.groupcollide(player.group_npc,player.group_player,False,True):
        pass
    if pygame.sprite.groupcollide(player.group_bullet,player.group_brick,True,False):
        pass


#定义一个控制声音的类和初始音频的方法
def replay_music():
     bg_sound.play_pause()
     bg_sound.play_sound()
def audio_init():
     global bg_au,hit_au,bullent_au
     pygame.mixer.init()
     hit_au = pygame.mixer.Sound("exlposion.wav")
     #btn_au = pygame.mixer.Sound("button.wav")
     bg_au = pygame.mixer.Sound("background.ogg")
     bullent_au = pygame.mixer.Sound("bullet.wav")
class Music():
     def __init__(self,sound):
         self.channel = None
         self.sound = sound     
     def play_sound(self):
         self.channel = pygame.mixer.find_channel(True)
         self.channel.set_volume(0.5)
         self.channel.play(self.sound)
         
     def play_pause(self):
         self.channel = pygame.mixer.find_channel(True)
         self.channel.set_volume(0.0)
         self.channel.play(self.sound)
   



# 初始化
pygame.init()
audio_init()
#背景
background=Background()
# 屏幕对象
screen = pygame.display.set_mode([600,background.rect[3]]) # 尺寸



#音乐的一些设置
global bg_sound,hit_sound,btn_sound,bullent_sound
bg_sound= Music(bg_au)
hit_sound=Music(bullent_au)
bullent_sound=Music(hit_au)
replay_flag = True
bullent_flag = False


# 玩家精灵对象
cnt=0
while 1:
    
    #初始化精灵
    player = Player()
    if cnt==0:
        player.star=0
        cnt=cnt+1

    #初始化精灵位置
    player.rect.bottom=background.sur[1]-40
    #创建按钮对象
    clock = pygame.time.Clock()#帧率
    old_ticks=1#随机产生怪物
    n_npc=1#怪物的数量
    '''
    npc = Npc()
    npc.rect.right=200
    npc.rect.bottom=background.sur[1]-250
    player.group_npc .add(npc)
    '''
    k_num=0
    k_a=[0,1,0]
    button=Button()
    button_save=Button_save()
    L=70
    B=100
    C=0
    #选关卡
    for i in range(10):
        if i<=player.Check_p:
            checkpoint=Checkpoint()
            checkpoint.rect.left=L
            checkpoint.rect.bottom=B
            checkpoint.C_point=C
            L=L+100
            C=C+1
            if i%5==4 and i>0:
                B=B+100
                L=70
            player.group_c_point.add(checkpoint)


    if background.next==1 and now==Load()-1:

        now=now+1
        Mam_init(now)
        player.Check_p0=now
        player.star=2
        background.next=0
        #c_point.f.C_point
    #主循环




    
    while len(player.group_player):
 
        if background.rect.left ==0 :
            background.who_move[0]=1
            background.who_move[1]=0

        elif  background.rect.right == background.sur[0]:
            background.who_move[1]=1
            background.who_move[0]=0
        else:
            background.who_move[1]=0
            background.who_move[0]=0

        screen.fill([255,255,255])
        #帧率
        clock.tick(30)
        ticks = pygame.time.get_ticks()
        k_space=0 #跳跃
        k_a[0]=0
        k_a[2]=0#攻击
        player.list_key=[0,0,0]#跳跃，前后
        background.list_key=[0,0]#前后
        #获得键盘状态

        for event in pygame.event.get():
            if event.type == QUIT: # 点击右上角的'X'，终止主循环
                pygame.quit()
                sys.exit()       
            elif event.type == KEYDOWN:           
                if event.key == K_ESCAPE: # 按下'ESC'键，终止主循环
                    sys.exit()
                if event.key == K_SPACE :
                    k_space=1
                    hit_sound.play_sound()
                   
                    
            if event.type == VIDEORESIZE:
                background.sur = event.w, event.h
                screen = pygame.display.set_mode(background.sur, RESIZABLE)
            
            elif event.type == MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                mouse_x = pos[0]
                mouse_y = pos[1]
                #开始按钮
                if button.rect.right>mouse_x>button.rect.left and button.rect.bottom>mouse_y>button.rect.top and player.star==0:
                    player.star=0.5
                elif (button.rect.right<mouse_x or mouse_x<button.rect.left or button.rect.bottom<mouse_y or mouse_y< button.rect.top) and player.star==0.5:
                    player.star=0
                button.update()
                #返回按钮
                if button_save.rect.right>mouse_x>button_save.rect.left and button_save.rect.bottom>mouse_y>button_save.rect.top and player.star==2:
                    player.star=2.5
                elif (button_save.rect.right<mouse_x or mouse_x<button_save.rect.left or button_save.rect.bottom<mouse_y or mouse_y< button_save.rect.top) and player.star==2.5:
                    player.star=2
                button_save.update()
                #选关按钮
                for c_point in player.group_c_point:

                    if c_point.rect.right>mouse_x>c_point.rect.left and c_point.rect.bottom>mouse_y>c_point.rect.top and player.star==1:
                        player.star=1.5
                    elif (c_point.rect.right<mouse_x or mouse_x<c_point.rect.left or c_point.rect.bottom<mouse_y or mouse_y< c_point.rect.top) and player.star==1.5:
                        player.star=1
                    c_point.update0()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                #点击开始按钮
                click =pygame.mouse.get_pressed()
                if button.rect.right>mouse_x>button.rect.left and button.rect.bottom>mouse_y>button.rect.top and player.star==0.5:
                    if click[0]==1:
                        player.star=1
                #点击返回按钮
                if button_save.rect.right>mouse_x>button_save.rect.left and button_save.rect.bottom>mouse_y>button_save.rect.top and player.star==2.5 :
                    #click =pygame.mouse.get_pressed()
                    if click[0]==1:
                        player.kill()
                #点击选关按钮
                for c_point in player.group_c_point:
                    if c_point.rect.right>mouse_x>c_point.rect.left and c_point.rect.bottom>mouse_y>c_point.rect.top and( player.star==1 or player.star==1.5):
                        #click =pygame.mouse.get_pressed()
                        if click[0]==1:
                            #初始化地图
                            #print('123')
                            Mam_init(c_point.C_point)
                            player.Check_p0=c_point.C_point
                            player.star=2
                            #c_point.f.C_point
                            now=c_point.C_point
            
                
        #获得键盘状态
        key = pygame.key.get_pressed()
        
        #移动
        player.speed[0]=5#对移动速度赋值
        background.speed[0]=5
       #背景动
       #background.who_move=1：背景在边
        if background.sur[0]//2+background.speed[0]>player.rect.left and player.rect.left>background.sur[0]//2-background.speed[0]:


            if background.who_move[0] :
    
                if key[K_LEFT]:
                    player.list_key[1]=1
                else:
                    player.list_key[1]=0
                if key[K_RIGHT]:
                    background.list_key[0]=1
                else:
                    background.list_key[0]=0
            if background.who_move[1] :

                if key[K_RIGHT]:
                    player.list_key[2]=1
                else:
                    player.list_key[2]=0
                if key[K_LEFT]:
                    background.list_key[0]=1
                else:
                    background.list_key[0]=0
            else:

                if key[K_RIGHT]:
                    background.list_key[1]=1
                else:
                    background.list_key[1]=0
                if key[K_LEFT]:
                    background.list_key[0]=1
                else:
                    background.list_key[0]=0
      
        
        else:


            if key[K_LEFT]:
                player.list_key[1]=1
            
            else:
                player.list_key[1]=0
           
            if key[K_RIGHT]:
            
                player.list_key[2]=1
           
            else:
                player.list_key[2]=0
  
        
        #跳跃
        if player.rect.bottom==player.bottom1:
            player.tf_jump=0
            player.speed[1]=0
            player.limit=0
        if k_space==1 and player.limit<2:
            player.limit=player.limit+1
            player.tf_jump=1
            player.speed[1]=15
    
        if player.tf_jump:
            player.jump()
            
        if key[K_a]:
            k_num=k_num+1
        if key[K_LEFT]:
            k_a[1]=-1
        elif key[K_RIGHT]:
            k_a[1]=1
        if key[K_UP]:
            k_a[2]=-1
        elif key[K_DOWN]:
            k_a[2]=1
    
        
        if k_num%5==4:
            k_a[0]=1
            k_num=0
        #碰撞检测
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
    background.rect.left=0
    background.rect.top=0
