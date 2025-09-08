#벽돌깨기게임
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
rect_pedal = pygame.Ret(x_pos_pedal, y_pos_pedal, size_width_pedal, size_height_pedal)

# 공의 사이즈, 좌표, Rect
size_radius_ball = 20

x_pos_ball = size_width_bg//2
y_pos_ball = size_height_bg - size_height_pedal - size_radius_ball

rect_ball = pygame.Rect(x_pos_ball, y_pos_ball, size_radius_ball*2,size_radius_ball*2)
rect_ball.center = (x_pos_ball, y_pos_ball)

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
print(rect_block)

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                to_x = 1
            if event.key == pygame.K_LEFT:
                to_x = -1    

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_LEFT:
                to_x = 0  
    #원숭이가 화면박으로 사라지지 않도록 하기위함
    if x_pos_monkey < 0: 
        x_pos_monkey = 0
    elif x_pos_monkey > size_bg_width-size_monkey_width:
        x_pos_monkey = size_bg_width-size_monkey_width
    else:
        x_pos_monkey += to_x                      

    x_pos_banana += x_speed_banana   
    y_pos_banana += y_speed_banana

    if x_pos_banana <= 0:
        x_speed_banana = -x_speed_banana
        x_pos_bananan = 0
    elif x_pos_banana >= size_bg_width-size_banana_width:
        x_speed_banana = -x_speed_banana
        x_pos_banana = size_bg_width-size_banana_width
    
    if y_pos_banana <= 0:
        y_speed_banana = -y_speed_banana
        y_pos_bananan = 0
    elif y_pos_banana >= size_bg_height-size_banana_height:
        print('바닥')
        y_speed_banana = -y_speed_banana
        y_pos_banana = size_bg_height-size_banana_height   

    rect_banana = image_banana.get_rect()
    rect_banana.left = x_pos_banana
    rect_banana.top = y_pos_banana

    rect_monkey = image_monkey.get_rect()
    rect_monkey.left = x_pos_monkey
    rect_monkey.top = y_pos_monkey

    if rect_monkey.colliderect(rect_banana):
        x_speed_banana = -x_speed_banana
        y_speed_banana = -y_speed_banana
        point += 1

    background.blit(image_bg, (0,0))
    background.blit(image_banana, (x_pos_banana, y_pos_banana))
    background.blit(image_monkey, (x_pos_monkey, y_pos_monkey))

    text_point = font_point.render(str(point), True, (0,0,0))
    background.blit(text_point, (10,10))

    pygame.display.update()

pygame.quit()