import pygame
pygame.init()
screen_width, screen_height = 400, 500
displlay_surface = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Background")
background_image = pygame.transform.scale(pygame.image.load("bg.jpeg").convert(), (screen_width, screen_height))
penguin_image = pygame.transform.scale(pygame.image.load("penguin.jpeg").convert_alpha(), (200, 200))
text = pygame.font.Font(None, 36).render("Cute Penguin", True, pygame.Color('black'))
text_rect = text.get_rect(center=(screen_width // 2, screen_height//2 + 110))
def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        displlay_surface.blit(background_image, (0, 0))
        displlay_surface.blit(penguin_image, (screen_width//2, screen_height//2-30))
        displlay_surface.blit(text, text_rect)
        pygame.display.flip()
        clock.tick(30)
if __name__ == "__main__":
    game_loop()
