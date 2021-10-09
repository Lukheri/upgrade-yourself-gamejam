import pygame
from gun import Gun
from bullet import BulletUpgrade

class Player(pygame.sprite.Sprite):
    def __init__(self, surface):
        super().__init__()
        self.display_surface = surface

        self.image = pygame.image.load("Graphics/target.png").convert_alpha()
        self.rect = self.image.get_rect(center = pygame.mouse.get_pos())
        self.clicking = False

        pistol = Gun((90, 384), self.display_surface)
        self.gun = pygame.sprite.GroupSingle()
        self.gun.add(pistol)
        self.gun_mode = "normal"

        self.bullet_upgrade = pygame.sprite.Group()
    
    def update_position(self):
        self.rect.center = pygame.mouse.get_pos()

    def player_input(self):
        if pygame.mouse.get_pressed()[0]:
            if not self.clicking:
                self.gun.sprite.fire()
                if self.gun_mode != "normal":
                    self.animate_bullet(self.rect.center)
                
                self.clicking = True

        if not pygame.mouse.get_pressed()[0]:
            self.clicking = False

    def animate_bullet(self, pos):
        if self.gun_mode == "bullet2":
            self.bullet_upgrade.add(BulletUpgrade(pos, self.gun_mode))

        if self.gun_mode == "bullet3":
            self.bullet_upgrade.add(BulletUpgrade(pos, self.gun_mode))

    def update(self):
        self.gun.update()
        self.gun.draw(self.display_surface)

        self.bullet_upgrade.draw(self.display_surface)
        self.bullet_upgrade.update()

        self.player_input()
        self.update_position()