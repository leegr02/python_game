import pygame

pygame.init()

background = pygame.display.set_mode((480, 360))
pygame.display.set_caption("GWANYANG")

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.MOUSEMOTION:
            #print('MOUSEMOTION')
            print(pygame.mouse.get_pos())  
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass
            #print('MOUSEBOTTONDOWN')
            #print(pygame.mouse.get_pos())
        if event.type == pygame.MOUSEBUTTONUP:
            pass
            #print('MOUSEBUTTONUP')   
            #print(pygame.mouse.get_pos())     

pygame.quit()
