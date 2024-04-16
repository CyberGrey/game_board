import pygame, sys

width, height = 40, 40
distance = 10
briсk = 25

size = ((width+distance)*briсk+distance, (height+distance)*briсk+distance)

red = (255, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
board = [[0]*briсk for i in range(briсk)]

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pixel paint")
icon = pygame.image.load('image/icon.png')
pygame.display.set_icon(icon)

running = True
while running:

    #screen.fill(blue)
    pygame.display.update()

    for event in pygame.event.get():        
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            print(x_mouse, y_mouse)
            col = x_mouse//(width+distance)
            row = y_mouse//(height+distance)
            board[row][col] ^= 1

    for row in range(briсk):
        for col in range(briсk):
            if board[row][col] == 1:
                color = red
            else:
                color = white
            x = distance + col*(width+distance)
            y = distance + row*(height+distance)
            pygame.draw.rect(screen, color, (x, y, width, height))
