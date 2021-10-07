import pygame
from random import randint, choice
from support import import_folder

class Enemy(pygame.sprite.Sprite):
    def __init__(self, surface, image_path, animation_dict, size):
        super().__init__()
        self.import_images(image_path, animation_dict, size)
        self.display_surface = surface
        self.frame_index = 0
        self.animation_speed = 0.4
    
    def import_images(self, image_path, animation_dict, size):
        self.animations = animation_dict

        for animation in self.animations.keys():
            full_path = image_path + animation
            self.animations[animation] = import_folder(full_path, True, size)
    
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

class Bird(Enemy):
    def __init__(self, surface, image_path, animation_dict, size):
        super().__init__(surface, image_path, animation_dict, size)
        self.direction_x = 5
        self.direction_y = choice([-3, 3, 0, 0])

        self.status = "Flying"

        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center = (randint(1400, 1600), randint(64, 560)))
    
    def move(self):
        self.rect.x -= self.direction_x
        self.rect.y += self.direction_y

        if self.rect.y <= 32 or self.rect.y >= 600:
            self.direction_y *= -1
    
    def update(self):
        self.animate()
        self.move()

class Ghost(Enemy):
    def __init__(self, surface, image_path, animation_dict, size):
        super().__init__(surface, image_path, animation_dict, size)
        self.status = "Flying"

        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center = (randint(1400, 1600), randint(64, 560)))

        self.ghost_cd = choice([40, 50, 60])
        self.ghost_timer = 0
        self.ghost_timer_speed = 0.5
        self.ghost_duration = 0

        self.direction_x = choice([3, 3, 4, 5])
        self.direction_y = choice([0, 0, 3, 4])
    
    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0
            if self.status == "Hit":
                self.kill()
            if self.status == "Ghosting" and self.ghost_duration >= choice([2, 2, 3, 4]):
                self.status = "Flying"
        
        self.image = self.animations[self.status][int(self.frame_index)]
    
    def move(self):
        self.rect.x -= self.direction_x
        self.rect.y += self.direction_y

        if self.rect.y <= 32 or self.rect.y >= 600:
            self.direction_y *= -1

    def going_ghost(self):
        self.ghost_timer += self.ghost_timer_speed
        if self.ghost_timer >= self.ghost_cd:
            self.ghost_timer = 0
            self.ghost_duration += 1
            self.status = "Ghosting"

    def update(self):
        self.animate()
        self.move()
        self.going_ghost()