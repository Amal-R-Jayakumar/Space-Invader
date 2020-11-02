import pygame
import random
import math
from pygame import mixer
# initialize pygame
pygame.init()

#   VARIABLES
#   Screen
width = 800
height = 600

#   Player
playerX = 370
playerY = 480
change_to_playerX_position = 0

#   Enemy
enemyX = []
enemyY = []
change_to_enemyX_position = []
change_to_enemyY_position = []
enemy_image = []
num_of_enimies = 6


#   Bullet
#   Ready = Bullet is invisible
#   Fire = Bullet is fired
bulletX = 0
bulletY = 480
change_to_bulletX_position = 0
change_to_bulletY_position = 20
bullet_state = "ready"

#   Score_printing
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# Game Over Text
game_over_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x, y):
    score = font.render("Score: "+str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    game_over = game_over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(game_over, (200, 250))


# create the  screeen with 800x600 px resolution
screen = pygame.display.set_mode((width, height))

#   Background
background = pygame.image.load("assets/background.png")

# Music
mixer.music.load('assets/background.wav')
mixer.music.play(-1)


#Title and Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load("assets/ufo.png")
pygame.display.set_icon(icon)

# player
player_image = pygame.image.load("assets/player.png")


def player(x, y):
    screen.blit(player_image, (x, y))


# Enemy
for _ in range(num_of_enimies):
    enemy_image.append(pygame.image.load("assets/alien.png"))
    enemyX.append(random.randint(0, 800))
    enemyY.append(random.randint(50, 150))
    change_to_enemyX_position.append(6)
    change_to_enemyY_position.append(20)


def enemy(x, y, i):
    screen.blit(enemy_image[i], (x, y))


#   Bullet
bullet_image = pygame.image.load("assets/bullet.png")


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_image, (x+20, y))


# Collition between bullet and enemy/alien

def isCollition(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(pow(enemyX - bulletX, 2) + pow(enemyY - bulletY, 2))
    if distance < 30:
        return True
    else:
        return False


#######################################
# game loop (it is an infinite loop...)
game_is_running = True
while game_is_running:
    #            R  G  B
    screen.fill((0, 0, 0))

    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_is_running = False

    # checking for keystrokes...
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                change_to_playerX_position = -6
            if event.key == pygame.K_RIGHT:
                change_to_playerX_position = 6
            if event.key == pygame.K_SPACE:
                if bullet_state is 'ready':
                    bullet_sound = mixer.Sound("assets/laser.wav")
                    bullet_sound.play()
                    # Get the current X- Coordinate of the bullet
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.type == pygame.KEYUP or event.type == pygame.KEYUP:
                change_to_playerX_position = 0

    playerX += change_to_playerX_position

############################################################
#   Restricting the player form going beyond screen boundary
#   For the SPACESHIP
    if playerX <= 0:
        playerX = 0
    elif playerX >= width-64:
        playerX = width-64

############################################
#   Enemy movement and boundarry restriction
    for enemy_list_var in range(num_of_enimies):

        # GAME OVER text
        if enemyY[enemy_list_var] > 440:
            for j in range(num_of_enimies):
                enemyY[j] == 2000
            game_over_text()
            break
            
        enemyX[enemy_list_var] += change_to_enemyX_position[enemy_list_var]
        if enemyX[enemy_list_var] <= 0:
            change_to_enemyX_position[enemy_list_var] = 5
            enemyY[enemy_list_var] += change_to_enemyY_position[enemy_list_var]
        elif enemyX[enemy_list_var] >= width-64:
            change_to_enemyX_position[enemy_list_var] = -5
            enemyY[enemy_list_var] += change_to_enemyY_position[enemy_list_var]

        collision = isCollition(enemyX[enemy_list_var], enemyY[enemy_list_var],
                                bulletX, bulletY)
        #   Explosion
        if collision:
            collision_sound = mixer.Sound("assets/explosion.wav")
            collision_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[enemy_list_var] = random.randint(0, width)
            enemyY[enemy_list_var] = random.randint(50, 150)
        enemy(enemyX[enemy_list_var], enemyY[enemy_list_var], enemy_list_var)

    player(playerX, playerY)

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= change_to_bulletY_position

    show_score(textX, textY)
    pygame.display.update()
##############################################
