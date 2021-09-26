import pygame
import sys
from gun import Gun
from player import Player
from enemy import Bird
from settings import *

class Game:
    def __init__(self, surface):
        self.display_surface = surface
        self.player = pygame.sprite.GroupSingle()
        self.setup_player()

        self.enemies = pygame.sprite.Group()
        self.enemy_respawn_rate = 30
        self.enemy_respawn_current = 0
        self.clicking = False

    def spawn_enemy(self):
        if self.enemy_respawn_current >= self.enemy_respawn_rate:
            self.enemy_respawn_current = 0
            self.enemies.add(Bird(self.display_surface, "Graphics/BlueBird/", {"Flying":[], "Hit":[]}))
        else:
            self.enemy_respawn_current += 1
    
    def setup_player(self):
        player_sprite = Player(self.display_surface)
        self.player.add(player_sprite)
    
    def check_collision(self):
        player = self.player.sprite
        for enemy in self.enemies.sprites():
            if enemy.rect.colliderect(player.rect) and pygame.mouse.get_pressed()[0] and enemy.status == "Flying":
                if not self.clicking:
                    enemy.die()
                    if not player.rapid_fire:
                        self.clicking = True
        
        if not player.clicking:
            self.clicking = False

    def run(self):
        self.enemies.draw(self.display_surface)
        self.enemies.update()
        self.spawn_enemy()

        self.player.draw(self.display_surface)
        self.player.update()

        self.check_collision()

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

upgrade_yourself = Game(screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill("black")
    upgrade_yourself.run()

    pygame.display.update()
    clock.tick(60)