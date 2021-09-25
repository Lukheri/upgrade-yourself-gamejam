import pygame
from random import randint
from support import import_folder

class Enemy(pygame.sprite.Sprite):
    def __init__(self, surface, image_path, animation_dict):
        super().__init__()
        self.import_images(image_path, animation_dict)
        self.display_surface = surface
        self.frame_index = 0
        self.animation_speed = 0.4
        self.direction_x = 5
    
    def import_images(self, image_path, animation_dict):
        self.animations = animation_dict

        for animation in self.animations.keys():
            full_path = image_path + animation
            self.animations[animation] = import_folder(full_path)

# "Graphics/BlueBird/", {"Flying":[], "Hit":[]}
class Bird(Enemy):
    def __init__(self, surface, image_path, animation_dict):
        super().__init__(surface, image_path, animation_dict)

        self.image = self.animations["Flying"][self.frame_index]
        self.rect = self.image.get_rect(center = (randint(1060, 1300), randint(76, 500)))

    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.animations["Flying"]):
            self.frame_index = 0
        
        self.image = self.animations["Flying"][int(self.frame_index)]
    
    def move(self):
        self.rect.x -= self.direction_x
    
    def update(self):
        self.animate()
        self.move()
    
