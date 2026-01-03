import pygame
import random

pygame.init()
screen_w=800
screen_h=300
screen=pygame.display.set_mode((screen_w,screen_h))

WHITE=(255,255,255)
BLACK=(0,0,0)

b_img=pygame.image.load('images/monkey.png')#주인공
b_img = pygame.transform.scale(b_img, (60, 60))
b_w,b_h=b_img.get_size()

c_img=pygame.image.load('images/banana.png')#장애물
c_img = pygame.transform.scale(c_img, (20, 40))
c_w,c_h=c_img.get_size()

b_x=50
b_y=screen_h - b_h# 300 - 60 240
is_jumping=False# 현재 점핑 상태인지?
jump_speed=15#점프 속도
gravity=1#중력

c_x=screen_w
c_y=screen_h - c_h# 300 -40  260
c_speed=5#장애물 속도
running=True
clock=pygame.time.Clock()
while running:
    clock.tick(30)
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys=pygame.key.get_pressed()
    if not is_jumping:#점프 상태가 아닐때만 스페이스바 누르면 점프
        if keys[pygame.K_SPACE]:
            is_jumping=True
    if is_jumping:# 중력 작용한 점프 기능
        b_y=b_y-jump_speed
        jump_speed=jump_speed-gravity
        if jump_speed<-15:
            is_jumping=False
            jump_speed=15
    if c_x<0:
        c_x=screen_w
        c_speed=c_speed+1
    if b_x+b_w>c_x and b_x<c_x+c_w:
        if b_y+b_h>c_y:
            running=False
    c_x-=c_speed
    screen.blit(b_img,(b_x,b_y))
    screen.blit(c_img, (c_x,c_y))
    pygame.display.flip()
pygame.quit()
