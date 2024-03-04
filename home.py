import pygame
from properties import Properties
from sound import Sound

properties = Properties()
sound = Sound()

class Home :

    def __init__(self) :
        self.start = False
        self.start_button_img = pygame.image.load("assets/play.png")
        self.hover_start_button_img = pygame.image.load("assets/play_toggle.png")
        self.quit_button_img = pygame.image.load("assets/quit.png")
        self.hover_quit_button_img = pygame.image.load("assets/quit_toggle.png")
        
        self.start_button = self.start_button_img
        self.quit_button = self.quit_button_img

    def reset(self) :
        self.start = False

    # Fonction pour afficher le menu d'accueil
    def run(self):

        sound.menu_play()   

        while not self.start:
            
            properties.screen.fill(properties.WHITE)
            text_font = pygame.font.Font(None, 50)
            text_surface = text_font.render("Menu d'accueil", True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=(properties.WIDTH // 2, properties.HEIGHT // 4))
            
            # Affichage des boutons
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            # Bouton pour démarrer le jeu
            start_button_rect = self.start_button.get_rect(center=(properties.WIDTH // 2, properties.HEIGHT // 2 - 60))

            # Bouton pour quitter
            quit_button_rect = self.quit_button.get_rect(center=(properties.WIDTH // 2, properties.HEIGHT // 2 + + 60))

            # Gestion des événements
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if start_button_rect.collidepoint(mouse):
                        self.start = True
                    if quit_button_rect.collidepoint(mouse):
                        pygame.quit()
                        
                if event.type == pygame.MOUSEMOTION:
                    # Vérifier si la souris survole les boutons
                    if start_button_rect.collidepoint(event.pos):
                        self.start_button = self.hover_start_button_img
                    else:
                        self.start_button = self.start_button_img

                    if quit_button_rect.collidepoint(event.pos):
                        self.quit_button = self.hover_quit_button_img
                    else:
                        self.quit_button = self.quit_button_img


            properties.screen.blit(text_surface, text_rect)
            properties.screen.blit(self.start_button, start_button_rect)
            properties.screen.blit(self.quit_button, quit_button_rect)

            pygame.display.update()