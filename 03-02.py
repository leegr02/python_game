import pygame

pygame.init()

background = pygame.display.set_mode((480, 360))
pygame.display.set_caption("GWANYANG")

x = background.get_size()[0]//2
y = background.get_size()[1]//2

play = True
while play:
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
            play = False
        
    background.fill((255,255,255))
    # 원
    # pygame.draw.circle(화면, 색, 중심 좌표, 반지름, 선 굵기)
    # pygame.draw.circle(surface, color, center, radius, width)
    # pygame.draw.circle(background, (255,0,0), (240,180), 50)
    #pygame.draw.circle(background, (255,0,0), (240,180), 50,5)

    # 사각형
    # pygame.draw.rect(화면, 색, 위치와 크기, 선 굵기)
    # pygame.draw.rect(background, (0,255,0), (240,180,100,50))
    # pygame.draw.rect(background, (0,255,0), (240,180,100,50), 5)

    # 타원
    # pygame.draw.ellipse(화면, 색, 위치와 크기, 선 굵기)
    # pygame.draw.ellipse(background, (0,0,255), (240,180,100,50))
    # pygame.draw.ellipse(background, (0,0,255), (240,180,100,50), 5)

    # 다각형
    # pygame.draw.polygon(화면, 색, 점들의 위치, 선 굵기)
    # pygame.draw.polygon(background, (255,255,0), [[100,100],[0,200],[200,200]])
    # pygame.draw.polygon(background, (255,255,0), [[100,100],[0,200],[200,200]],5)
    # pygame.draw.polygon(background, (255,255,0), ((146,0),(291,106),(236,277),(56,277),(0,106)))
    pygame.draw.polygon(background, (255,255,0), ((146,0),(291,106),(236,277),(56,277),(0,106)),5)

    pygame.draw.line(background, (0,0,0), (x,0), (x, y*2))
    pygame.draw.line(background, (0,0,0), (0,y), (x*2, y))


    pygame.display.update()


#pygame.quit()
