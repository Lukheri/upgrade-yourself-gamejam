import pygame
import sys

from gun import Gun
from player import Player
from enemy import Bird
from settings import *

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

player_sprite = Player(screen)
player = pygame.sprite.GroupSingle()
player.add(player_sprite)
enemies = pygame.sprite.Group()
e1 = Bird(screen, "Graphics/BlueBird/", {"Flying":[], "Hit":[]})
e2 = Bird(screen, "Graphics/BlueBird/", {"Flying":[], "Hit":[]})
enemies.add(e1)
enemies.add(e2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill("black")
    player.draw(screen)
    player.update()
    enemies.draw(screen)
    enemies.update()

    pygame.display.update()
    clock.tick(60)