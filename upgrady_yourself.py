import pygame
import sys
from random import choice
from player import Player
from enemy import Bird
from settings import *

class Game:
    def __init__(self, surface):
        self.display_surface = surface

        self.player = pygame.sprite.GroupSingle()
        self.setup_player()

        self.enemies = pygame.sprite.Group()
        self.enemy_respawn_rate = 50
        self.enemy_respawn_current = 0
        self.bird = "Graphics/BlueBird/", {"Flying":[], "Hit":[]}
        self.ghost = "Graphics/Ghost/", {"Flying":[], "Hit":[], "Ghosting":[]}

        self.clicking = False

        self.score = 0
        self.font = pygame.font.Font("freesansbold.ttf", 256)

    def setup_player(self):
        player_sprite = Player(self.display_surface)
        self.player.add(player_sprite)    

    def spawn_enemy(self):
        if self.score > 10:
            enemies = choice([self.bird, self.ghost])
            
        else:
            enemies = self.bird

        if enemies == self.bird:
            size = (64, 64)
        else:
            size = (88, 60)

        if self.enemy_respawn_current >= self.enemy_respawn_rate:
            self.enemy_respawn_current = 0
            self.enemies.add(Bird(self.display_surface, *enemies, size))
        else:
            self.enemy_respawn_current += 1

    def pistol_collision(self):
        player = self.player.sprite
        for enemy in self.enemies.sprites():
            if enemy.rect.colliderect(player.rect) and pygame.mouse.get_pressed()[0] and enemy.status == "Flying":
                if not self.clicking:
                    print(enemy.status)
                    enemy.die()
                    self.score += 1
                    self.clicking = True

        if not player.clicking:
            self.clicking = False
    
    def shotgun_collision(self):
        bullets = self.player.sprite.bullet_upgrade

        for bullet in bullets.sprites():
            for enemy in self.enemies.sprites():
                if enemy.rect.colliderect(bullet.rect) and enemy.status == "Flying":
                    enemy.die()
                    self.score += 1

    def player_miss(self):
        if self.score > 10:
            enemies = choice([self.bird, self.ghost])
        else:
            enemies = self.bird
        
        if enemies == self.bird:
            size = (64, 64)
        else:
            size = (88, 60)

        player = self.player.sprite
        for enemy in self.enemies.sprites():
            if not enemy.rect.colliderect(player.rect) and pygame.mouse.get_pressed()[0]:
                if not self.clicking:
                    self.enemies.add(Bird(self.display_surface, *enemies, size))
                    self.clicking = True
        
        if not player.clicking:
            self.clicking = False
    
    def show_score(self):
        score = self.font.render(str(self.score), True, "white")
        self.display_surface.blit(score, (462, 182))
    
    def change_gun(self):
        player = self.player.sprite
        gun = self.player.sprite.gun.sprite
        if self.score == 10:
            gun.gun_type = "Shotgun"
            gun.rect.center = (140, 225)
            player.gun_mode = "bullet3"

    def run(self):
        gun = self.player.sprite.gun.sprite
        
        self.show_score()

        self.enemies.draw(self.display_surface)
        self.enemies.update()
        self.spawn_enemy()

        self.player.draw(self.display_surface)
        self.player.update()

        if gun.gun_type == "Pistol":
            self.pistol_collision()
        
        if gun.gun_type == "Shotgun":
            self.shotgun_collision()

        self.player_miss()
        self.change_gun()

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