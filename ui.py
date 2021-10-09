import pygame

class Background_Tile(pygame.sprite.Sprite):
    def __init__(self, surface, pos, speed):
        super().__init__()
        self.display_surface = surface
        self.image = pygame.image.load("Graphics/Green.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.movement = speed
    
    def move(self):
        self.rect.x += self.movement
    
    def check(self):
        if self.rect.x <= -63:
            self.rect.x = 1280
    
    def update(self):
        self.move()
        self.check()

class UI:
    def __init__(self, surface):
        self.display_surface = surface
        self.score_font = pygame.font.Font("freesansbold.ttf", 256)
        self.life_font = pygame.font.Font("freesansbold.ttf", 24)
        # self.shield_image = pygame.image.load("Graphics/shield.png").convert_alpha()
        # self.shield_down = pygame.image.load("Graphics/shield_down.png").convert_alpha()
        # self.shield_rect = self.shield_image.get_rect(topleft = (10, 10))
        self.color = (10, 28, 3)
    
    def show_score(self, score_val):
        score = self.score_font.render(str(score_val), True, self.color)
        score_rect = score.get_rect(center = (640, 384))
        self.display_surface.blit(score, score_rect)

    # Might add shield mechanic in the future, might not, who knows.
    # def show_player_shield(self, shield_up):
    #     if shield_up:
    #         self.display_surface.blit(self.shield_image, self.shield_rect)
    #     if not shield_up:
    #         self.display_surface.blit(self.shield_down, self.shield_rect)