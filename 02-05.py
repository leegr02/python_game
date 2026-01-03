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
            pass
            #print('MOUSEMOTION')
            #print(pygame.mouse.get_pos())  
        if event.type == pygame.MOUSEBUTTONDOWN:
            #print('MOUSEBOTTONDOWN')
            #print(pygame.mouse.get_pos())
            if event.button == 1:
                print('왼쪽 클릭')
            elif event.button == 2:
                print('휠 클릭')
            elif event.button == 3:
                print('오른쪽 클릭')
            elif event.button == 4:
                print('휠 올리기')
            elif event.button == 5:
                print('휠 내리기')                
        if event.type == pygame.MOUSEBUTTONUP:
            pass
            #print('MOUSEBUTTONUP')   
            #print(pygame.mouse.get_pos())     

pygame.quit()
