import pygame
pygame.init()
s=pygame.display.set_mode((640, 480))
done=False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.circle(s, (0, 255, 0), (320, 240), 50)
    pygame.display.flip()