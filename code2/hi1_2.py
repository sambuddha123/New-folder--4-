import pygame
import random
pygame.init()

s_c=pygame.USEREVENT+1
b_c=pygame.USEREVENT+2

blue=pygame.Color("blue")
red=pygame.Color("red")
green=pygame.Color("green")
yellow=pygame.Color("yellow")
magenta=pygame.Color("magenta")
orange=pygame.Color("orange")
white=pygame.Color("white")

class sprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]

    def update(self):
        self.rect.move_ip(self.velocity)
        flag= False

        if self.rect.left <= 0 or self.rect.right >= 640:
            self.velocity[0] = -self.velocity[0]
        if self.rect.top <= 0 or self.rect.bottom >= 480:
            self.velocity[1] *= -self.velocity[1]
            flag = True
        if flag:
            pygame.event.post(pygame.event.Event(s_c))
            pygame.event.post(pygame.event.Event(b_c))

    def cc(self):
            self.image.fill(random.choice([blue, red, green, yellow, magenta, orange, white]))
        
def cb():
     global bg
     bg = random.choice([blue, red, green, yellow, magenta, orange, white])

all_s=pygame.sprite.Group()
s1 = sprite(blue, 50, 50)
s2 = sprite(red, 50, 50)
s1.rect.x=random.randint(0, 590)
s1.rect.y=random.randint(0, 430)
s1.rect.x=random.randint(0, 590)
s1.rect.y=random.randint(0, 430)
all_s.add(s1)
all_s.add(s2)

screen = pygame.display.set_mode((640, 480))
bg = blue
screen.fill(bg)
exit = False
clock = pygame.time.Clock()

while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        elif event.type == s_c:
            s1.cc()
            s2.cc()
        elif event.type == b_c:
            cb()

    all_s.update()
    screen.fill(bg)
    all_s.draw(screen)
    pygame.display.flip()
    clock.tick(240)
pygame.quit()