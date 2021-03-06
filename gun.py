import pygame
from math import hypot, asin, pi
from support import import_folder

class Gun(pygame.sprite.Sprite):
    def __init__(self, pos, surface):
        super().__init__()
        self.import_images()
        self.scale_images()
        self.display_surface = surface
        self.gun_type = "Pistol"

        self.orig_image = self.guns[self.gun_type][0]
        self.image = self.guns[self.gun_type][0]
        self.rect = self.image.get_rect(center = pos)

        self.animation_frame = 0
        self.animation_speed = 0.5
        self.firing = False
    
    def scale_images(self):
        for i, image in enumerate(self.guns["Pistol"]):
            image = pygame.transform.scale(image, (128,64))
            self.guns["Pistol"][i] = image
        
        for i, image in enumerate(self.guns["Shotgun"]):
            image = pygame.transform.scale(image, (240,48))
            self.guns["Shotgun"][i] = image

    def import_images(self):
        gun_image_path = "Graphics/Guns/"
        self.guns = {"Pistol":[], "Shotgun":[]}

        for gun in self.guns.keys():
            full_path = gun_image_path + gun
            self.guns[gun] = import_folder(full_path)
    
    def fire_animation(self):
        if self.firing:
            self.animation_frame += self.animation_speed

            if self.animation_frame >= len(self.guns[self.gun_type]):
                self.animation_frame = 0
                self.firing = False

            self.orig_image = self.guns[self.gun_type][int(self.animation_frame)]

    def fire(self):
        self.firing = True
    
    def change_angle(self):
        mouse_pos = pygame.mouse.get_pos()
        opposite_side = self.rect.y - mouse_pos[1]
        adjacent_side = mouse_pos[0] - self.rect.x
        hypotenuse = hypot(opposite_side, adjacent_side)

        angle = asin(opposite_side/hypotenuse)
        angle = (angle/pi) * 180
        self.rotate(angle)

    def rotate(self, angle):
        self.image = pygame.transform.rotozoom(self.orig_image, angle, 1)
        self.rect = self.image.get_rect(center = self.rect.center)
    
    def update(self):
        self.fire_animation()
        self.change_angle()


