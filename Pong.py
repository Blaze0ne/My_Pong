import pygame

pygame.init()
screen = pygame.display.set_mode((840, 420))
clock = pygame.time.Clock()
running = True

x = 20
y = 50

witdth =20
height = 45
vel = 10

#Mettre un get.rect()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("Black")
    player1 = pygame.draw.rect(screen, "white", (x,y,witdth, height))
   
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and y>0:
        y -= vel
    if keys[pygame.K_DOWN] and y<420-height:
        y += vel

  
    pygame.display.flip()
    clock.tick(60)
pygame.quit()

