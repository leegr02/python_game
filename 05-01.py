import pygame

pygame.init()

background = pygame.display.set_mode((480, 360))
pygame.display.set_caption("GWANYANG")

fps = pygame.time.Clock() 

image_bg = pygame.image.load("images/sky.png")
image_monkey = pygame.image.load("images/monkey.png")

size_bg_width = background.get_size()[0]
size_bg_height = background.get_size()[1]

size_monkey_width = image_monkey.get_rect().size[0]
size_monkey_height = image_monkey.get_rect().size[1]

x_pos_monkey = size_bg_width/2 - size_monkey_width/2
y_pos_monkey = size_bg_height - size_monkey_height

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
                to_y = -2
            elif event.key==pygame.K_DOWN:
                to_y = 2
            elif event.key==pygame.K_RIGHT:
                to_x = 2
            elif event.key==pygame.K_LEFT:
                to_x = -2
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_UP:
                to_y = 0
            elif event.key==pygame.K_DOWN:
                to_y = 0
            elif event.key==pygame.K_RIGHT:
                to_x = 0
            elif event.key==pygame.K_LEFT:
                to_x = 0
    x_pos_monkey += to_x
    y_pos_monkey += to_y                   

    background.blit(image_bg, (0,0))
    background.blit(image_monkey, (x_pos_monkey, y_pos_monkey))
    pygame.display.update()

pygame.quit()
