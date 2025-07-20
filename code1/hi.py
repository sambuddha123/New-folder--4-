import pygame
pygame.init()
s=pygame.display.set_mode((640, 480))
done=False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    pygame.draw.rect(s, (255, 0, 0), (100, 100, 50, 50))
    pygame.display.flip()