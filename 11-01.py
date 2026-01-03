#도형그리기
import pygame

pygame.init()

background = pygame.display.set_mode((480, 360))

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
    # 배경색 칠하기
    background.fill((255,255,255)) # 배경은 흰색이며 기본값은 검정색

    # 사각형 그리기
    # pygame.draw.rect(surface, color, rect)
    pygame.draw.rect(background, (255,255,0), (50,50,100,100))  
    
    # 원 그리기   
    # pygame.draw.rect(surface, color, center, radius)
    pygame.draw.circle(background, (255,0,255), (200,200), 30)

    pygame.display.update()

pygame.quit()