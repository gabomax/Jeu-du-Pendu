import pygame
from properties import *
from state import State

properties = Properties()
state = State()

# Classe pour choisir la phrase de départ
class PhraseChooser:
    def __init__(self):
        self.input_text = ""
        self.confirmed = False  # Variable pour indiquer si la phrase a été confirmée

    def reset(self) :
        self.confirmed = False
        self.input_text = ""

    def run(self):
        choosing = True

        self.input_text = ""

        print(self.input_text)

        while choosing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        # Si la touche "Entrée" est pressée, retourner la phrase saisie
                        self.confirmed = True
                        choosing = False
                    elif event.key == pygame.K_BACKSPACE:
                        # Si la touche "Retour arrière" est pressée, supprimer le dernier caractère
                        self.input_text = self.input_text[:-1]
                    else:
                        # Ajouter le caractère saisi à la phrase
                        self.input_text += event.unicode

            # Effacer l'écran
            properties.screen.fill((255, 255, 255))

            # Afficher le texte de la phrase en cours de saisie
            properties.draw_text("Saisissez la phrase de départ (uniquement des lettres !!) :", (0, 0, 0), 20, 20)
            properties.draw_text(self.input_text, (0, 0, 0), 20, 60)

            # Rafraîchir l'écran
            pygame.display.flip()

        return self.input_text