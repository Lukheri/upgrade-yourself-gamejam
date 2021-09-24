import pygame
import sys

from gun import Gun
from player import Player
from settings import *

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

pistol = Gun((100, 288), screen)
player_sprite = Player(screen)
gun = pygame.sprite.GroupSingle()
player = pygame.sprite.GroupSingle()
gun.add(pistol)
player.add(player_sprite)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill("grey")
    gun.draw(screen)
    player.draw(screen)


    pygame.display.update()
    clock.tick(60)