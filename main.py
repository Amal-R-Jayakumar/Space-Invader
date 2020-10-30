import pygame

# initialize pygame
pygame.init()

# create the  screeen with 800x600 px resolution
screen = pygame.display.set_mode((800, 600))

#Title and Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load("assets/ufo.png")
pygame.display.set_icon(icon)

# player
player_image = pygame.image.load("assets/player.png")
playerX = 370
playerY = 480


def player():
    screen.blit(player_image, (playerX, playerY))


    # game loop (it is an infinite loop...)
game_is_running = True
while game_is_running:
    #            R  G  B
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_is_running = False

    player()
    pygame.display.update()
