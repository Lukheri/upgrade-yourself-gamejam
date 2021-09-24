import pygame
from support import import_folder

class Gun(pygame.sprite.Sprite):
    def __init__(self, pos, surface) -> None:
        super().__init__()
        self.import_images()
        self.display_surface = surface

        self.image = self.guns["Pistol"][0]
        self.rect = self.image.get_rect(topleft = pos)

    def import_images(self):
        gun_image_path = "Graphics/Guns/"
        self.guns = {"Pistol":[]}

        for gun in self.guns.keys():
            full_path = gun_image_path + gun
            self.guns[gun] = import_folder(full_path)


