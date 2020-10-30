import pygame
import random

#   VARIABLES
#   Screen
width = 800
height = 600

#   Player
playerX = 370
playerY = 480
change_to_playerX_position = 0

#   Enemy
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
change_to_enemyX_position = 0.5
change_to_enemyY_position = 20


# initialize pygame
pygame.init()

# create the  screeen with 800x600 px resolution
screen = pygame.display.set_mode((width, height))

#Title and Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load("assets/ufo.png")
pygame.display.set_icon(icon)

# player
player_image = pygame.image.load("assets/player.png")


def player(x, y):
    screen.blit(player_image, (x, y))


# Enemy
enemy_image = pygame.image.load("assets/alien.png")


def enemy(x, y):
    screen.blit(enemy_image, (x, y))


    # game loop (it is an infinite loop...)
game_is_running = True
while game_is_running:
    #            R  G  B
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_is_running = False

    # checking for keystrokes...
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                change_to_playerX_position = -0.3
            if event.key == pygame.K_RIGHT:
                change_to_playerX_position = 0.3
        if event.type == pygame.KEYUP:
            if event.type == pygame.KEYUP or event.type == pygame.KEYUP:
                change_to_playerX_position = 0

    playerX += change_to_playerX_position

############################################################
#   Restricting the player form going beyond screen boundary
#   For the SPACESHIP
    if playerX < 0:
        playerX = 0
    elif playerX > width-64:
        playerX = width-64

############################################
#   Enemy movement and boundarry restriction
    enemyX += change_to_enemyX_position

    if enemyX < 0:
        change_to_enemyX_position = 0.5
        enemyY += change_to_enemyY_position
    elif enemyX > width-64:
        change_to_enemyX_position = -0.5
        enemyY += change_to_enemyY_position
    player(playerX, playerY)
    enemy(enemyX, enemyY)

    pygame.display.update()
