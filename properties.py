import pygame

class Properties :
    
    def __init__(self):
        pygame.init()
        self.WIDTH, self.HEIGHT = 1080, 720
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Jeu du Pendu")
        self.font = pygame.font.Font(None, 36)
        self.wrong_letters = []
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)

    def reset(self) :
        self.wrong_letters = []

    def draw_text(self, text, color, x, y):
        surface = self.font.render(text, True, color)
        self.screen.blit(surface, (x, y))
    
    def draw_wrong_letters(self):
        self.wrong_letters_text = "Mauvaises lettres: " + ", ".join(self.wrong_letters)
        self.draw_text(self.wrong_letters_text, (255, 0, 0), 20, 20)

    def draw_phrase(self, phrase, guessed_letters):
        display_text = ""
        for char in phrase:
            if char.lower() in guessed_letters :
                display_text += char
            elif char == " " :
                display_text += "   "
            else:
                display_text += "_  "
        self.draw_text(display_text, (0, 150, 0), 20, 60)

    def draw_win(self, phrase) :
        text_surface = self.font.render(f"Félicitations, vous avez gagné, le mot était ({phrase}) !", True, (0, 0, 255))
        text_rect = text_surface.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2))
        self.screen.blit(text_surface, text_rect)

    def draw_loose(self, phrase) :
        text_surface = self.font.render(f"Désolé, vous avez perdu, le mot était ({phrase}).", True, (255, 0, 0))
        text_rect = text_surface.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2))
        self.screen.blit(text_surface, text_rect)






