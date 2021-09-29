import pygame
from random import randint, choice
from support import import_folder

class Enemy(pygame.sprite.Sprite):
    def __init__(self, surface, image_path, animation_dict):
        super().__init__()
        self.import_images(image_path, animation_dict)
        self.display_surface = surface
        self.frame_index = 0
        self.animation_speed = 0.4
        self.direction_x = 4
        self.direction_y = choice([-2, 2, 0, 0])
    
    def import_images(self, image_path, animation_dict):
        self.animations = animation_dict

        for animation in self.animations.keys():
            full_path = image_path + animation
            self.animations[animation] = import_folder(full_path, True, (64, 64))

# "Graphics/BlueBird/", {"Flying":[], "Hit":[]}
class Bird(Enemy):
    def __init__(self, surface, image_path, animation_dict):
        super().__init__(surface, image_path, animation_dict)
        self.status = "Flying"

        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center = (randint(1400, 1600), randint(64, 560)))

    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0
            if self.status == "Hit":
                self.kill()
        
        self.image = self.animations[self.status][int(self.frame_index)]
    
    def die(self):
        self.frame_index = 0
        self.direction_x = -2
        self.direction_y = 0
        self.status = "Hit"
    
    def move(self):
        self.rect.x -= self.direction_x
        self.rect.y += self.direction_y
        # if self.rect.y <= 50:
        #     self.direction_y = 1
        
        # if self.rect.y >= 400:
        #     self.direction_y = -1

        if self.rect.y <= 32 or self.rect.y >= 600:
            self.direction_y *= -1

    
    def update(self):
        self.animate()
        self.move()
    
