import pygame

class Sound :

    def __init__(self) :
        self.correct_sfx = pygame.mixer.Sound("assets/sound/correct.mp3")
        self.fail_sfx = pygame.mixer.Sound("assets/sound/fail.mp3")
        self.win_sfx = pygame.mixer.Sound("assets/sound/win.mp3")
        self.loose_sfx = pygame.mixer.Sound("assets/sound/loose.mp3")
        self.play_menu = False
        
    def correct_play(self) :
        self.correct_sfx.play()
        
    def fail_play(self) :
        self.fail_sfx.play()
        
    def win_play(self) :
        self.win_sfx.play()
        self.stop_menu
        
    def loose_play(self) :
        self.loose_sfx.play()
        self.stop_menu()
        
    def menu_play(self) :
        self.play_menu = True
        if self.play_menu :
            pygame.mixer.music.load("assets/sound/menu.mp3")
            pygame.mixer.music.play(loops=-1)
            
    def stop_menu(self) :
        self.play_menu = False
        pygame.mixer.music.stop()