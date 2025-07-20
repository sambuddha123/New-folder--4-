import pygame
def main():
    pygame.init()
    screen_width, screen_height = 640, 480
    screen=pygame.display.set_mode((screen_width, screen_height))

    color={
        "green": (0, 255, 0),
        "red": (255, 0, 0),
        "white": (255, 255, 255),
        "yellow": (255, 255, 0),
        "blue": (0, 0, 255),
    }
    current_color = color["white"]

    x,y=30,30
    sprite_width, sprite_height = 50, 50

    clock = pygame.time.Clock()
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            
            pressed= pygame.key.get_pressed()
            if pressed[pygame.K_LEFT]:
                x -= 5
            if pressed[pygame.K_RIGHT]:
                x += 5
            if pressed[pygame.K_UP]:
                y -= 5
            if pressed[pygame.K_DOWN]:
                y += 5
            x = max(0, min(x, screen_width - sprite_width))
            y = max(0, min(y, screen_height - sprite_height))

            if x ==0:
                current_color = color["red"]
            elif x == screen_width - sprite_width:
                current_color = color["green"]
            elif y == 0:
                current_color = color["blue"]
            elif y == screen_height - sprite_height:
                current_color = color["yellow"]
            else:
                current_color = color["white"]

        screen.fill((0,0,0))
        pygame.draw.rect(screen,current_color, (x, y, sprite_width, sprite_height))
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
if __name__ == "__main__":
    main()

        

    
    

    