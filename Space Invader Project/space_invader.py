import math
import random
import pygame
screen_width = 800
screen_height = 500
player_start_x = 370
player_start_y = 380
enemy_start_y_min = 50
enemy_start_y_max = 150
enemy_speed_x = 4
enemy_speed_y = 40
bullet_speed_y = 10
collision_distance = 27
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invader")
background = pygame.image.load("backround.jpeg")
icon = pygame.image.load("player.jpeg")
pygame.display.set_icon(icon)

# Player
player_img = pygame.image.load("player.jpeg")
player_x = player_start_x
player_y = player_start_y
player_x_change = 0

# Enemy
enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
num_of_enemies = 6
for _i in range(num_of_enemies):
    enemy_img.append(pygame.image.load("monster.jpeg"))
    enemy_x.append(random.randint(0, screen_width - 64))
    enemy_y.append(random.randint(enemy_start_y_min, enemy_start_y_max))
    enemy_x_change.append(enemy_speed_x)
    enemy_y_change.append(enemy_speed_y)

# Bullet
bullet_img = pygame.image.load("bullet.jpeg")
bullet_x = 0
bullet_y = player_y
bullet_x_change = 0
bullet_y_change = bullet_speed_y
bullet_state = "ready"

# Score
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)
text_x = 10
text_y = 10

# Game Over
game_over_font = pygame.font.Font("freesansbold.ttf", 64)

def show_score(x, y):
    # DIsplay the score on the screen
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))
    
def game_over_text():
    # Display the game over text on the screen
    over_text = game_over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

#Draw the player on the screen
def player(x, y):    
    screen.blit(player_img, (x, y))

#Draw the enemy on the screen
def enemy(x, y, i):
    screen.blit(enemy_img[i], (x, y))
      