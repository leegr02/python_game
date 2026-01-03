# 게임제작시 기본이 되는 코드
import pygame

pygame.init()

background = pygame.display.set_mode((480, 360))
pygame.display.set_caption("게임연습")

play = True
while play:
    for event in pygame.event.get():
        # print(event.type)
        if event.type == pygame.QUIT:
            play = False

pygame.quit()