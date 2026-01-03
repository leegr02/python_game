#벽돌깨기게임- 화면구성하기
import pygame
import random

pygame.init()

background = pygame.display.set_mode((480, 360))
pygame.display.set_caption("Brick Breaking")

# 배경 사이즈
size_width_bg = background.get_size()[0]
size_height_bg = background.get_size()[1]

# 페달의 사이즈, 좌표, rect
size_width_pedal = 100
size_height_pedal = 15

x_pos_pedal = size_width_bg//2 - size_width_pedal/2
y_pos_pedal = size_height_bg - size_height_pedal

# 사각형에 관한 정보
rect_pedal = pygame.Rect(x_pos_pedal, y_pos_pedal, size_width_pedal, size_height_pedal)

## 페달을 좌우로 움직이기
to_x_pedal = 0

# 공의 반지름, 사이즈, 좌표, Rect
size_radius_ball = 20

x_pos_ball = size_width_bg//2
y_pos_ball = size_height_bg - size_height_pedal - size_radius_ball

rect_ball = pygame.Rect(x_pos_ball, y_pos_ball, size_radius_ball*2,size_radius_ball*2)
rect_ball.center = (x_pos_ball, y_pos_ball)

## 공의 방향과 스피드
x_speed_ball = 0.1
y_speed_ball = 0.1

# 블록 사이즈, 좌표, Rect
size_width_block = size_width_bg//10
size_height_block = 30

x_pos_block = 0
y_pos_block = 0

rect_block = [[] for i in range(10)]
color_block = [[] for i in range(10)]

for i in range(10):
    for j in range(3):
        rect_block[i].append(pygame.Rect(i*size_width_block, j*size_height_block, size_width_block, size_height_block))
        color_block[i].append((random.randrange(255),random.randrange(150,255), random.randrange(150,255)))


# 마우스 좌표
x_pos_mouse, y_pos_mouse = 0, 0

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

        ## 마우스로 페달 움직이기
        if event.type == pygame.MOUSEMOTION:
            x_pos_mouse, y_pos_mouse = pygame.mouse.get_pos()
            if x_pos_mouse-size_width_pedal//2 >=0 and x_pos_mouse+size_width_pedal//2 <= size_width_bg: #양쪽벽에서 멈추기
                x_pos_pedal = x_pos_mouse-size_width_pedal//2
                rect_pedal.left = x_pos_mouse-size_width_pedal//2

    # 배경색 칠하기
    background.fill((255,255,255)) # 배경은 흰색이며 기본값은 검정색

    # 페달 그리기
    pygame.draw.rect(background, (255,255,0), rect_pedal)  
    
    # 공 좌표 계산
    if x_pos_ball-size_radius_ball <= 0:
        x_speed_ball = -x_speed_ball
    elif x_pos_ball >= size_width_bg-size_radius_ball: 
        x_speed_ball = -x_speed_ball    

    if y_pos_ball-size_radius_ball <= 0:
        y_speed_ball = -y_speed_ball
    elif y_pos_ball >= size_height_bg-size_radius_ball: 
        y_speed_ball = -y_speed_ball        

    # 공 좌표에 스피드값 누적
    x_pos_ball += x_speed_ball
    y_pos_ball += y_speed_ball

    # 공 그리기   
    rect_ball.center = (x_pos_ball, y_pos_ball)
    pygame.draw.circle(background, (255,0,255), (x_pos_ball, y_pos_ball), size_radius_ball)
    
    ## 공-페달 닿았을 때
    if rect_ball.colliderect(rect_pedal):
        y_speed_ball = -y_speed_ball

    # 블록 그래기(for문으로 10개*3층 만들기)
    for i in range(10):
        for j in range(3):
            if rect_block[i][j]:
                pygame.draw.rect(background, color_block[i][j], rect_block[i][j])
                rect_block[i][j].topleft = (i*size_width_block, j*size_height_block)

                ## 공-페달 닿았을 때
                if rect_ball.colliderect(rect_block[i][j]):
                    x_speed_ball = x_speed_ball
                    y_speed_ball = y_speed_ball
                    rect_block[i][j] = 0

    pygame.display.update()

pygame.quit()