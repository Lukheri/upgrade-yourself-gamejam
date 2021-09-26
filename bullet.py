import pygame
from support import import_folder

class BulletUpgrade(pygame.sprite.Sprite):
    def __init__(self, pos, type):
        super().__init__()
        self.frame_index = 0
        
        if type == "bullet2":
            self.images = import_folder("Graphics/Bullet Upgrades/Upgrade 1", True, (128, 128))
            self.animation_speed = 0.4

        if type == "bullet3":
            self.images = import_folder("Graphics/Bullet Upgrades/Upgrade 2", True, (128, 128))
            self.animation_speed = 0.3
        
        self.image = self.images[self.frame_index]
        self.rect = self.image.get_rect(center = pos)
    
    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.images):
            self.kill()
        else:
            self.image = self.images[int(self.frame_index)]
    
    def update(self):
        self.animate()