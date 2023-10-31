
import pygame

#Intialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))
#Title 
pygame.display.set_caption("Alien intruder")
#player
playerImg = pygame.image.load('sp.jfif')
playerX= 275
playerY = 400
playerX_change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))

#Game Loop
running = True
while running:

    screen.fill((128, 0, 128))
    playerX += 0.1
    playerX -= 0.1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if keystroke is pressed check whwther its right or left
       
            for event in pygame.event.get():
              if event.type == pygame.QUIT:
                running = False
       
                
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                playerX_change = 0 
                print("W key pressed")
            elif event.key == pygame.K_s:
                playerX_change = 0.1
                print("S key pressed")
            elif event.key == pygame.K_d:
                playerX_change = -0.1
                print("D key pressed")
                

    # 5 = 5 +- 0.1 ->5 = 5 -0.1
    # 5 = 5 + 0.1
    playerX += playerX_change
    player(playerX, playerY)
    pygame.display.update()
