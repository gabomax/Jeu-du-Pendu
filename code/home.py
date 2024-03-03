import pygame
from properties import Properties

properties = Properties()

class Home :

    def __init__(self) :
        self.start = False
        self.stat_button_img = pygame.image.load("assets/play.png")
        self.quit_button_img = pygame.image.load("assets/quit.png")

    def reset(self) :
        self.start = False

    # Fonction pour afficher le menu d'accueil
    def run(self):

        while not self.start:
            
            properties.screen.fill(properties.WHITE)
            text_font = pygame.font.Font(None, 50)
            text_surface = text_font.render("Menu d'accueil", True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=(properties.WIDTH // 2, properties.HEIGHT // 4))
            
            # Affichage des boutons
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            # Bouton pour démarrer le jeu
            start_button_rect = self.stat_button_img.get_rect(center=(properties.WIDTH // 2, properties.HEIGHT // 2 - 60))

            # Bouton pour quitter
            quit_button_rect = self.quit_button_img.get_rect(center=(properties.WIDTH // 2, properties.HEIGHT // 2 + + 60))

            # Gestion des événements
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if start_button_rect.collidepoint(mouse):
                        self.start = True
                    if quit_button_rect.collidepoint(mouse):
                        pygame.quit()

            properties.screen.blit(text_surface, text_rect)
            properties.screen.blit(self.stat_button_img, start_button_rect)
            properties.screen.blit(self.quit_button_img, quit_button_rect)

            pygame.display.update()