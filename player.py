import pygame
from gun import Gun

class Player(pygame.sprite.Sprite):
    def __init__(self, surface) -> None:
        super().__init__()
        self.display_surface = surface

        self.image = pygame.image.load("Graphics/target.png")
        self.rect = self.image.get_rect(center = pygame.mouse.get_pos())
        self.clicking = False

        pistol = Gun((50, 288), self.display_surface)
        self.gun = pygame.sprite.GroupSingle()
        self.gun.add(pistol)
    
    def update_position(self):
        self.rect.center = pygame.mouse.get_pos()

    def player_input(self):
        if pygame.mouse.get_pressed()[0]:
            if not self.clicking:
                self.gun.sprite.fire()
                self.clicking = True
                
        if not pygame.mouse.get_pressed()[0]:
            self.clicking = False
    
    def update(self):
        self.gun.update()
        self.gun.draw(self.display_surface)

        self.player_input()
        self.update_position()