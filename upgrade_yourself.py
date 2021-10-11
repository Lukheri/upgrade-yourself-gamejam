import pygame
import sys
from random import choice
from player import Player
from enemy import Bird, Ghost
from ui import Background_Tile, UI
from settings import *

class Game:
    def __init__(self, surface):
        self.display_surface = surface
        self.bg_speed = -2
        self.bg = pygame.sprite.Group()
        self.bg_size = 64
        self.setup_bg()

        self.ui = UI(surface)
        self.game_active = False
        self.lose_sound = pygame.mixer.Sound("Music/lose.mp3")
        self.lose_sound.set_volume(0.4)

        self.player = pygame.sprite.GroupSingle()
        self.setup_player()
        self.shield = True

        self.enemies = pygame.sprite.Group()
        self.enemy_respawn_rate = 50
        self.enemy_respawn_current = 0

        self.bird = "Graphics/BlueBird/", {"Flying":[], "Hit":[]}
        self.ghost = "Graphics/Ghost/", {"Flying":[], "Hit":[], "Ghosting":[]}

        self.clicking = False

        self.score = 0
        self.highscore = 0

    def setup_player(self):
        player_sprite = Player(self.display_surface)
        self.player.add(player_sprite)    

    def setup_bg(self):
        for col in range((screen_height//self.bg_size)):
            for row in range((screen_width//self.bg_size)+1):
                self.bg.add(Background_Tile(self.display_surface, (row*self.bg_size, col*self.bg_size), self.bg_speed))
    
    def add_bg(self):
        for col in range((screen_height//self.bg_size)):
            self.bg.add(Background_Tile(self.display_surface, (1280, col*self.bg_size), self.bg_speed))

    def play_game(self):
        if self.ui.play_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            self.game_active = True

    def reset(self):
        player = self.player.sprite
        gun = self.player.sprite.gun.sprite
        gun.rect.center = (90, 384)
        gun.gun_type = "Pistol"
        player.gun_mode = "normal"
        self.score = 0
        self.enemy_respawn_rate = 50
        self.enemy_respawn_current = 0
        self.ui.music_playing = False

    def spawn_enemy(self):
        if self.game_active:
            if self.score > 50:
                enemies = choice([self.bird, self.ghost])
                
            else:
                enemies = self.bird

            if self.enemy_respawn_current >= self.enemy_respawn_rate:
                self.enemy_respawn_current = 0
                if enemies == self.bird:
                    self.enemies.add(Bird(self.display_surface, *enemies, (64, 64)))
                else:
                    self.enemies.add(Ghost(self.display_surface, *enemies, (88, 60)))
            else:
                self.enemy_respawn_current += 1
            if self.enemy_respawn_rate >= 30:
                self.enemy_respawn_rate -= 0.01

    def player_miss(self):
        if self.game_active:
            if self.score > 50:
                enemies = choice([self.bird, self.ghost])
            else:
                enemies = self.bird

            player = self.player.sprite
            for enemy in self.enemies.sprites():
                if not enemy.rect.colliderect(player.rect) and pygame.mouse.get_pressed()[0]:
                    if not self.clicking:
                        if enemies == self.bird:
                            self.enemies.add(Bird(self.display_surface, *enemies, (64, 64)))
                        else:
                            self.enemies.add(Ghost(self.display_surface, *enemies, (88, 60)))

                        if self.score > 75:
                            if enemies == self.bird:
                                self.enemies.add(Bird(self.display_surface, *enemies, (64, 64)))
                            else:
                                self.enemies.add(Ghost(self.display_surface, *enemies, (88, 60)))

                        self.clicking = True
            
            if not player.clicking:
                self.clicking = False

    def pistol_collision(self):
        player = self.player.sprite
        for enemy in self.enemies.sprites():
            if enemy.rect.colliderect(player.rect) and pygame.mouse.get_pressed()[0] and enemy.status == "Flying":
                if not self.clicking:
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

    def change_gun(self):
        player = self.player.sprite
        gun = self.player.sprite.gun.sprite
        if self.score == 75:
            gun.gun_type = "Shotgun"
            gun.rect.center = (140, 384)
            player.gun_mode = "bullet3"
    
    def kill_all_enemies(self):
        for dead_enemy in self.enemies.sprites():
            dead_enemy.die()
    
    def check_highscore(self):
        if self.score > self.highscore:
            self.highscore = self.score

    def enemy_pass(self):
        for enemy in self.enemies.sprites():
            if enemy.rect.x < -30:
                self.kill_all_enemies()
                self.reset()
                self.ui.bg_music.stop()
                self.lose_sound.play()
                self.game_active = False

    # Might add shield mechanic in the future, might not, who knows.
    # def give_shield(self):
    #     if self.score % 150 == 0 and self.score > 0:
    #         self.shield = True
                        
    def run(self):
        gun = self.player.sprite.gun.sprite
        self.bg.draw(self.display_surface)
        self.bg.update()
        self.ui.update(self.score, self.highscore, self.game_active)

        self.enemies.draw(self.display_surface)
        self.enemies.update(self.ui.sfx)
        self.spawn_enemy()

        self.player.draw(self.display_surface)
        self.player.update(self.ui.sfx)

        if gun.gun_type == "Pistol":
            self.pistol_collision()
        
        if gun.gun_type == "Shotgun":
            self.shotgun_collision()

        self.play_game()
        self.enemy_pass()
        self.player_miss()
        self.change_gun()
        self.check_highscore()

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