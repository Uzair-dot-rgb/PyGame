import pygame
import random
screen_width, screen_height = 500, 400
movement_speed = 5
font_size = 70
pygame.init()
#Load and transform the backround image
backround_image = pygame.transform.scale(pygame.image.load("backround.jpeg"), (screen_width, screen_height))
font = pygame.font.SysFont("New Times Roman", font_size)
class Sprite(pygame.sprite.Sprite):
    def __init__(self, colour, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(pygame.Color("White"))
        pygame.draw.rect(self.image, colour, pygame.Rect(0, 0, width, height))
        self.rect = self.image.get_rect()
    def move(self, x_change, y_change):
        self.rect.x = max(0, min(self.rect.x + x_change, screen_width - self.rect.width))
        self.rect.y = max(0, min(self.rect.y + y_change, screen_height - self.rect.height))
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Collision Detection")
all_sprite = pygame.sprite.Group()
sprite1 = Sprite(pygame.Color("Red"), 20, 30)
sprite1.rect.x = random.randint(0, screen_width - sprite1.rect.width)
sprite1.rect.y = random.randint(0, screen_height - sprite1.rect.height)
all_sprite.add(sprite1)
sprite2 = Sprite(pygame.Color("Blue"), 20, 30)
sprite2.rect.x = random.randint(0, screen_width - sprite2.rect.width)
sprite2.rect.y = random.randint(0, screen_height - sprite2.rect.height)
all_sprite.add(sprite2)
clock = pygame.time.Clock()
running = True
Won = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if not Won:
        keys = pygame.key.get_pressed()
        x_change = (keys[pygame.K_LEFT] - keys[pygame.K_RIGHT]) * movement_speed
        y_change = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * movement_speed
        sprite1.move(x_change, y_change)
        if sprite1.rect.colliderect(sprite2.rect):
            Won = True
            all_sprite.remove(sprite2)
    screen.blit(backround_image, (0, 0))
    all_sprite.draw(screen)
    if Won:
        text = font.render("You Win!", True, pygame.Color("Green"))
        screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2 - text.get_height() // 2))
    pygame.display.flip()
    clock.tick(90)
pygame.quit()