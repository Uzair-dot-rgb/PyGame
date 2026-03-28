import pygame
def main():
    pygame.init()
    screen_height, screen_width = 500, 500
    display_surface = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Color changing sprite.")
    colors = {
        "red": pygame.Color("red"),
        "green": pygame.Color("green"),
        "white": pygame.Color("white"),
        "blue": pygame.Color("blue"),
        "yellow": pygame.Color("yellow")
    }
    current_color = colors["white"]
    clock = pygame.time.Clock()
    x, y = 30, 30
    width, height = 60, 60
    running = False
    while not running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = True
        press = pygame.key.get_pressed()
        if press[pygame.K_LEFT]:
            x = x - 3
        if press[pygame.K_RIGHT]:
            x = x + 3
        if press[pygame.K_UP]:
            y = y -3
        if press[pygame.K_DOWN]:
            y = y + 3
        
        x = min(max(0, x), screen_width - width)
        y = min(max(0, y), screen_height - height)
        if x == 0:
            current_color = colors["blue"]
        elif x == screen_width - width:
            current_color = colors["yellow"]
        elif y == 0:
            current_color = colors["red"]
        elif y == screen_height - height:
            current_color = colors["green"]
        else:
            current_color = colors["white"]
        display_surface.fill((0, 0, 0))
        pygame.draw.rect(display_surface, current_color, pygame.Rect(x, y, width, height))
        pygame.display.flip()
        clock.tick(90)
    pygame.quit()
if __name__ == "__main__":
    main()