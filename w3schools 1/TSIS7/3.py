import pygame
pygame.init()

W = 600
H = 400
scr = pygame.display.set_mode((W, H))
pygame.display.set_caption("RED BALL")

speed = 15
x = W//2
y = H//2
WHITE = (255, 255, 255)
RED = (255, 0, 0)

FPS = 60
clock = pygame.time.Clock()
done = False

flRight = flLeft = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x-=speed
    elif keys[pygame.K_RIGHT]:
        x+=speed
    elif keys[pygame.K_UP]:
        y-=speed
    elif keys[pygame.K_DOWN]:
        y+=speed
   


    scr.fill(WHITE)
    pygame.draw.circle(scr, RED, (x, y), 25)
    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
