import pygame

class Background_Tile(pygame.sprite.Sprite):
    def __init__(self, surface, pos, speed):
        super().__init__()
        self.display_surface = surface
        self.image = pygame.image.load("Graphics/UI/Green.png").convert_alpha()
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
        self.highscore_font = pygame.font.Font("freesansbold.ttf", 24)
        self.color = (10, 28, 3)
        self.bg_music = pygame.mixer.Sound("Music/play.mp3")
        self.bg_music.set_volume(0.15)
        self.music_playing = False

        self.menu_font = pygame.font.Font("freesansbold.ttf", 256)
        play_active = pygame.image.load("Graphics/Playbutton/playa.png").convert_alpha()
        play_passive = pygame.image.load("Graphics/Playbutton/playp.png").convert_alpha()
        self.play = [play_active, play_passive]
        self.play_rect = self.play[0].get_rect(center = (640, 500))

        sound_image_on = pygame.image.load("Graphics/UI/sounda.png").convert_alpha()
        sound_image_off = pygame.image.load("Graphics/UI/soundp.png").convert_alpha()
        self.sound_images = [sound_image_on, sound_image_off]
        self.sound_rect = self.sound_images[0].get_rect(topleft = (1237, 10))
        self.sound = True

        sfx_image_on = pygame.image.load("Graphics/UI/sfxa.png").convert_alpha()
        sfx_image_off = pygame.image.load("Graphics/UI/sfxp.png").convert_alpha()
        self.sfx_images = [sfx_image_on, sfx_image_off]
        self.sfx_rect = self.sfx_images[0].get_rect(topleft = (1190, 10))
        self.sfx = True

        self.clicking = False

        # self.shield_image = pygame.image.load("Graphics/shield.png").convert_alpha()
        # self.shield_down = pygame.image.load("Graphics/shield_down.png").convert_alpha()
        # self.shield_rect = self.shield_image.get_rect(topleft = (10, 10))

    def user_input(self):
        if self.play_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] and not self.clicking and not self.music_playing:
            self.bg_music.play(loops = -1)
            self.clicking = True
            self.music_playing = True

        if self.sound_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] and not self.clicking:
            self.sound = not self.sound
            self.clicking = True
        
        if self.sfx_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]and not self.clicking:
            self.sfx = not self.sfx
            self.clicking = True
        
        if not pygame.mouse.get_pressed()[0]:
            self.clicking = False

    def show_play(self):
        if self.play_rect.collidepoint(pygame.mouse.get_pos()):
            self.display_surface.blit(self.play[0], self.play_rect)
        else:
            self.display_surface.blit(self.play[1], self.play_rect)

    def show_menu(self):
        title = self.menu_font.render("1 TAP", True, self.color)
        rect = title.get_rect(center = (640, 300))
        self.display_surface.blit(title, rect)
    
    def sound_sfx_ui(self):
        if self.sound:
            sound_image = self.sound_images[0]
        else:
            sound_image = self.sound_images[1]
        
        if self.sfx:
            sfx_image = self.sfx_images[0]
        else:
            sfx_image = self.sfx_images[1]
        
        self.display_surface.blit(sound_image, self.sound_rect)
        self.display_surface.blit(sfx_image, self.sfx_rect)

    def mute_sound(self):
        if not self.sound:
            self.bg_music.set_volume(0)
        else:
            self.bg_music.set_volume(0.15)
    
    def show_score(self, score_val):
        score = self.score_font.render(str(score_val), True, self.color)
        score_rect = score.get_rect(center = (640, 384))
        self.display_surface.blit(score, score_rect)
    
    def show_highscore(self, highscore_val):
        highscore = self.highscore_font.render("HIGHSCORE: " + str(highscore_val), True, self.color)
        highscore_rect = highscore.get_rect(topleft = (7, 7))
        self.display_surface.blit(highscore, highscore_rect)
    
    def update(self, score, highscore, active):
        if active:
            self.show_score(score)
        else:
            self.show_menu()
            self.show_play()
        self.show_highscore(highscore)
        self.sound_sfx_ui()
        self.user_input()
        self.mute_sound()

    # Might add shield mechanic in the future, might not, who knows.
    # def show_player_shield(self, shield_up):
    #     if shield_up:
    #         self.display_surface.blit(self.shield_image, self.shield_rect)
    #     if not shield_up:
    #         self.display_surface.blit(self.shield_down, self.shield_rect)