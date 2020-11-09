import sys, time, random, math, pygame
from pygame.locals import *
 
 
class MySprite(pygame.sprite.Sprite):
  def __init__(self, target):
    pygame.sprite.Sprite.__init__(self)
    self.master_image = None
    self.frame = 0
    self.old_frame = -1
    self.frame_width = 1
    self.frame_height = 1
    self.first_frame = 0
    self.last_frame = 0
    self.columns = 1
    self.last_time = 0
 
  # 　　使用property方法，让精灵类对坐标操作更方便
  def _getx(self):
    return self.rect.x
 
  def _setx(self, value):
    self.rect.x = value
 
  X = property(_getx, _setx)
 
  def _gety(self):
    return self.rect.y
 
  def _sety(self, value):
    self.rect.y = value
 
  Y = property(_gety, _sety)
 
  def _getpos(self):
    return self.rect.topleft
 
  def _setpos(self, pos):
    self.rect.topleft = pos
 
  position = property(_getpos, _setpos)
 
 
  def load(self, filename, width, height, columns):
    self.master_image = pygame.image.load(filename).convert_alpha()
    self.frame_width = width
    self.frame_height = height
    self.rect = Rect(0, 0, width, height)
    self.columns = columns
    rect = self.master_image.get_rect()
    self.last_frame = (rect.width // width) * (rect.height // height) - 1
 
 
  def update(self, current_time, rate=30):
    # 　　更新帧数
    if current_time > self.last_time + rate:
      self.frame += 1
      if self.frame > self.last_frame:
        self.frame = self.first_frame
      self.last_time = current_time
 
    # 当帧数发生改变时，创建新的图片
    if self.frame != self.old_frame:
      frame_x = (self.frame % self.columns) * self.frame_width
      frame_y = (self.frame // self.columns) * self.frame_height
      rect = Rect(frame_x, frame_y, self.frame_width, self.frame_height)
      self.image = self.master_image.subsurface(rect)
      self.old_frame = self.frame
 
pygame.init()
screen = pygame.display.set_mode((800, 600))
font = pygame.font.Font(None, 24)
framerate = pygame.time.Clock()
 
bg = pygame.image.load("background.jpg").convert_alpha()
#pl = pygame.image.load('caveman.png').convert_alpha()

# 创建精灵组
group = pygame.sprite.Group()
 
 
player = MySprite(screen)
player.load("caveman.png", 50, 64, 8)
player.first_frame = 1
player.last_frame = 7
player.position = 400, 303
group.add(player)
 
 
jump_vel = 0.0
#  设置一个记录跳跃次数的变量
space_number = 0
#  跳跃判断
player_jumping = False
player_start_y = player.Y
 
while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      sys.exit()
    if event.type == KEYDOWN:
      if event.key == K_UP:
        #  跳跃次数小于2次时，
        if space_number < 2:
          jump_vel = -15.0
          space_number += 1
          player_jumping = True
 
  keys = pygame.key.get_pressed()
  if keys[K_ESCAPE]:
    sys.exit()
  if keys[K_RIGHT]:
   
    player.X += 8
  if keys[K_LEFT]:
    if player.X > 0:
        player.X -= 8
  #  设置帧数
  framerate.tick(30)
  ticks = pygame.time.get_ticks()
 
  #  当按下空格后，jump_vel变量不断变大，直到接触地面
  if player_jumping:
    player.Y += jump_vel
    jump_vel += 2
    #  落地后
    if player.Y >= player_start_y:
        player_jumping = False
        player.Y = player_start_y
        jump_vel = 0
        space_number = 0
        rush_number = 0
 
  #  创建背景
  screen.blit(bg, (0, 0))
 
  # 精灵组更新
  group.update(ticks, 50)
  group.draw(screen)
 
  pygame.display.update()