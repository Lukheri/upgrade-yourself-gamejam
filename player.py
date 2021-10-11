import pygame
from gun import Gun
from bullet import BulletUpgrade

class Player(pygame.sprite.Sprite):
    def __init__(self, surface):
        super().__init__()
        self.display_surface = surface

        self.image = pygame.image.load("Graphics/Player/target.png").convert_alpha()
        self.rect = self.image.get_rect(center = pygame.mouse.get_pos())
        self.clicking = False

        self.gunshot = pygame.mixer.Sound("Music/shot.mp3")
        self.gunshot.set_volume(0.2)

        pistol = Gun((90, 384), self.display_surface)
        self.gun = pygame.sprite.GroupSingle()
        self.gun.add(pistol)
        self.gun_mode = "normal"

        self.bullet_upgrade = pygame.sprite.Group()
    
    def update_position(self):
        self.rect.center = pygame.mouse.get_pos()

    def player_input(self, sfx):
        if pygame.mouse.get_pressed()[0]:
            if not self.clicking:
                self.gun.sprite.fire()
                if sfx:
                    self.gunshot.play()
                if self.gun_mode != "normal":
                    self.animate_bullet(self.rect.center)
                
                self.clicking = True

        if not pygame.mouse.get_pressed()[0]:
            self.clicking = False

    def animate_bullet(self, pos):
        # idk where to use this
        if self.gun_mode == "bullet2":
            self.bullet_upgrade.add(BulletUpgrade(pos, self.gun_mode))

        # Shotgun bullet
        if self.gun_mode == "bullet3":
            self.bullet_upgrade.add(BulletUpgrade(pos, self.gun_mode))

    def update(self, sfx):
        self.gun.update()
        self.gun.draw(self.display_surface)

        self.bullet_upgrade.draw(self.display_surface)
        self.bullet_upgrade.update()

        self.player_input(sfx)
        self.update_position()