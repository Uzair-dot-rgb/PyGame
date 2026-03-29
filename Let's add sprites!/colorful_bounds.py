import pygame
import random
pygame.init()
sprite_color_change_event = pygame.USEREVENT + 1
backround_color_change_event = pygame.USEREVENT + 2
yellow = pygame.Color('yellow')
red = pygame.Color('red')
blue = pygame.Color('blue')
green = pygame.Color('green')
black = pygame.Color('black')
white = pygame.Color('white')
orange = pygame.Color('orange')
# Sprite Class that represnt the moving object.
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]
    def update(self):
        self.rect.move_ip(self.velocity)
        boundary = False
        if self.rect.left <= 0 or self.rect.right >= 800:
            self.velocity[0] = -self.velocity[0]
            boundary = True
        if self.rect.top <= 0 or self.rect.bottom >= 600:
            self.velocity[1] = -self.velocity[1]
            boundary = True
        if boundary:
            pygame.event.post(pygame.event.Event(sprite_color_change_event))
            pygame.event.post(pygame.event.Event(backround_color_change_event))
    def change_color(self):
        self.image.fill(random.choice([yellow, red, green, orange]))
def change_background_color():
    global bg_color 
    bg_color = random.choice([white, black, blue])
all_sprites = pygame.sprite.Group()
sp1 = Sprite(red, 50, 50)
sp1.rect.x = random.randint(0, 780)
sp1.rect.y = random.randint(0, 570)
all_sprites.add(sp1)
screen = pygame.display.set_mode((800, 600))
bg_color = blue
screen.fill(bg_color)
running = False
clock = pygame.time.Clock()
while not running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = True
        elif event.type == sprite_color_change_event:
            sp1.change_color()
        elif event.type == backround_color_change_event:
            change_background_color()
    all_sprites.update()
    screen.fill(bg_color)
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(240)
pygame.quit()

    