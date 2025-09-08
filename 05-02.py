import pygame

pygame.init()

background = pygame.display.set_mode((480, 360))
pygame.display.set_caption("GWANYANG")

fps = pygame.time.Clock() 

image_bg = pygame.image.load("images/sky.png")
image_banana = pygame.image.load("images/banana.png")

size_bg_width = background.get_size()[0]
size_bg_height = background.get_size()[1]

size_banana_width = image_banana.get_rect().size[0]
size_banana_height = image_banana.get_rect().size[1]

x_pos_banana = size_bg_width/2 - size_banana_width/2
y_pos_banana = 0

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.MOUSEMOTION:
            x_pos_mouse, y_pos_mouse = pygame.mouse.get_pos()
            x_pos_banana = x_pos_mouse-size_banana_width/2  
            y_pos_banana = y_pos_mouse-size_banana_height/2     
   

    background.blit(image_bg, (0,0))
    background.blit(image_banana, (x_pos_banana, y_pos_banana))
    pygame.display.update()

pygame.quit()
