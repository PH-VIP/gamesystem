import pygame, sys
from pygame.locals import *
import random
import time
import random
class Player(pygame.sprite.Sprite):#Sprite是sprite模块的精灵类，内有很多有用的方法。
    # super(FooChild,self) 首先找到 FooChild 的父类（就是类 FooParent），然后把类 FooChild 的对象转换为类 FooParent 的对象
    speed=[5,20]#第一个元素是左右移动速度，第二个元素是跳跃速度（只做初始化）
    cnt=5#计数
    j_or_d=0#值为1的时候在跳跃
    limit=0
    n=0
    tf_jump=0
    bottom1=0
    group1 = pygame.sprite.Group()
    list_key=[0,0,0]
    #初始化
    def __init__(self):   
        #继承父类pygame.sprite.Sprite的__init__()方法
        super().__init__()
        # load函数，返回一个 Surface 对象("./images/background.png")
        self.image = pygame.image.load('./sprite/1.png').convert_alpha() 
        width,height = self.image.get_size()
        #调整角色大小（变为原来的1/2）
        self.image = pygame.transform.scale(self.image, (width//8,height//8))
        #位置
        self.rect = self.image.get_rect()
    # 随着方向键运动
    def update(self):
        
        if self.list_key[0]==1 and self.list_key[1]==0 and self.list_key[2]==0:
            if self.j_or_d==1:
                self.rect.move_ip(0,-self.speed[1])
            else:
                self.rect.move_ip(0,self.speed[1])
        elif self.list_key[2]==1 and self.list_key[0]==0 :
            self.rect.move_ip(self.speed[0],0)
        elif self.list_key[1]==1 and self.list_key[0]==0 :
            self.rect.move_ip(-self.speed[0],0)
        elif self.list_key[1]==1 and self.list_key[0]==1 :
            if self.j_or_d==1:
                self.rect.move_ip(-self.speed[0],-self.speed[1])
            else:
                self.rect.move_ip(-self.speed[0],self.speed[1])
        elif self.list_key[2]==1 and self.list_key[0]==1 :
            if self.j_or_d==1:
                self.rect.move_ip(self.speed[0],-self.speed[1])
            else:
                self.rect.move_ip(self.speed[0],self.speed[1])
        # 限定player在屏幕中
        
       
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > sur[0]:
            self.rect.right = sur[0]
        '''if self.rect.top <= 0:
            self.rect.top = 0'''
        if self.rect.bottom >=self.bottom1:
            self.rect.bottom =self.bottom1
        self.image = pygame.image.load('./sprite/'+str(self.n+1)+'.png').convert_alpha()
        self.n=self.n+1
        if self.n>7:
            self.n=0
        width,height = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (width//8,height//8))
    def fire(self):
        #print("发射子弹...")

    
        # 1. 创建子弹精灵
        bullet = Bullet()

        # 2. 设置精灵的位置
        bullet.rect.bottom = self.rect.centery
        bullet.rect.centerx = self.rect.x

        # 3. 将精灵添加到精灵组
        self.group1.add(bullet)
    

        

        
    #跳跃
    def jump(self):
        #if brick.rect.colliderect(player.rect):
        #if brick.rect.colliderect(player.rect)and player.rect.left<brick.rect.right and player.rect.top<brick.rect.top :
            #pass
        #else:

            self.list_key[0]=1
            self.speed[1]=self.speed[1]-1
            self.cnt=self.cnt-1
            print('****************************************************')
            print('************************')
            #self.rect.move_ip(0,-self.speed[1])
            if self.cnt==0:
                j_or_d=0
                self.cnt=5
            
    #下坠
    def down(self):
        self.list_key[0]=1
        self.speed[1]=self.speed[1]+1

pygame.init()
# 屏幕对象
sur=750,400
screen = pygame.display.set_mode(sur,RESIZABLE) # 尺寸
# 玩家精灵对象
player = Player()
#初始化精灵位置
#player.rect.bottom=sur[1]

# 窗口主循环
clock = pygame.time.Clock()#帧率
group2 = pygame.sprite.Group()
group3 = pygame.sprite.Group()
group3.add(player)
old_ticks=0#随机产生怪物
out=1
#pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
##############################主循环##############################
while out:
    #帧率
    clock.tick(30)
    ticks = pygame.time.get_ticks()
    # 更新屏幕
    screen.fill((0,0,0))
    k_space=0 #跳跃
    k_a=0#攻击
    player.list_key=[0,0,0]#跳跃，前后
    for event in pygame.event.get():
        if event.type == QUIT: # 点击右上角的'X'，终止主循环
            pygame.quit()
            sys.exit()       
        elif event.type == KEYDOWN:           
            if event.key == K_ESCAPE: # 按下'ESC'键，终止主循环
                out=0
            if event.key == K_SPACE :
                k_space=1
            if event.key == K_a:
                k_a=1 
        if event.type == VIDEORESIZE:
            sur = event.w, event.h
            screen = pygame.display.set_mode(sur, RESIZABLE)#获得键盘状态
    key = pygame.key.get_pressed()#获得键盘状态
    #移动
    if key[K_LEFT]:
        player.list_key[1]=1
    else:
        player.list_key[1]=0
    if key[K_RIGHT]:
        player.list_key[2]=1
    else:
        player.list_key[2]=0
    #跳跃
    if k_space==1 and player.limit<1:
        player.limit=player.limit+1
        player.speed[1]=20#对跳跃速度赋值
        player.tf_jump=1
    if player.tf_jump:
        player.jump()
        print(player.limit)
    if player.rect.bottom ==sur[1]:
        player.limit=0
    
    
    
            
                
      
    # 更新玩家
    group3.update()
    group3.draw(screen)
    # 放置玩家
    #screen.blit(player.image, player.rect)
    pygame.display.flip()
    '''
        for brick1 in brick.group_brick:
            print(player1.rect.bottom,brick1.rect.top)
            
            if brick1.rect.colliderect(player1.rect) and player1.rect.bottom<=brick1.rect.top+1:
                player1.bottom1=brick1.rect.top+1
                player1.tf_jump=0
                player1.limit=0
                print('上墙')
            elif brick1.rect.colliderect(player1.rect) and brick1.rect.top<player1.rect.top<brick1.rect.bottom:
                player1.rect.top=brick1.rect.bottom
                player1.speed[1]=0
                print('归零')
            elif brick1.rect.colliderect(player1.rect) and (player1.rect.left<brick1.rect.right or player1.rect.right>brick1.rect.left) :
                print('从左右撞')
                #player1.rect.left=brick1.rect.right
                player1.speed[0]=0
    '''