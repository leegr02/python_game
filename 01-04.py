# 연속으로 방향키 누르면 연속으로 이동
import pygame

pygame.init()

background = pygame.display.set_mode((480, 360))
pygame.display.set_caption("GWANYANG")

# 초당 게임프레임 수 지정으로 1초 동안 while문을 몇 번 돌릴 것인지 정하는 것으로 속도, 빠르기
fps = pygame.time.Clock() 

x_pos = background.get_size()[0]//2
y_pos = background.get_size()[1]//2

# 연속으로 키를 눌렀을때 연속으로 이동시키기 위한 변수
to_x = 0
to_y = 0

play = True
while play:
    deltaTime = fps.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                to_y = -1
            elif event.key==pygame.K_DOWN:
                to_y = 1
            elif event.key==pygame.K_RIGHT:
                to_x = 1
            elif event.key==pygame.K_LEFT:
                to_x = -1
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_UP:
                to_y = 0
            elif event.key==pygame.K_DOWN:
                to_y = 0
            elif event.key==pygame.K_RIGHT:
                to_x = 0
            elif event.key==pygame.K_LEFT:
                to_x = 0
    x_pos += to_x
    y_pos += to_y                   

    background.fill((255,255,255))
    pygame.draw.circle(background, (0,0,255), (x_pos,y_pos), 5)
    #pygame.draw.circle(surface, clor, center, radius)
    pygame.display.update()

pygame.quit()
