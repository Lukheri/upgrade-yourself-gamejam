import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, surface) -> None:
        super().__init__()
        self.display_surface = surface

        self.image = pygame.image.load("Graphics/target.png")
        self.rect = self.image.get_rect(center = pygame.mouse.get_pos())