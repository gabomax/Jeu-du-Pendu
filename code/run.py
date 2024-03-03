from numpy import choose
import pygame
from state import State
from game import Game
from choose import PhraseChooser
from properties import Properties
from home import Home

state = State()
game = Game()
phrase_chooser = PhraseChooser()
properties = Properties()
home = Home()

class Run :

    def __init__(self):
        self.playing = False
        self.phrase = []
        self.letter = " "

    def reset_game(self):
        print("Hello World")
        # Réinitialiser les paramètres du jeu
        state.reset()
        game.reset()
        home.reset()
        phrase_chooser.reset()
        properties.reset()
        self.phrase = []
        self.playing = False
        self.run()
        self.letter = " "

    def run(self) :

        print("Hello World")
        home.run()

        if home.start :

            self.phrase = phrase_chooser.run()

            if phrase_chooser.confirmed :

                game.setLetters(self.phrase.lower())

                print(self.phrase)
                print(game.letters)

                guessed_letters = []
                self.playing = True
                    
            while self.playing :

                properties.screen.blit(state.state, (-100, -100))

                for event in pygame.event.get() :

                    if event.type == pygame.QUIT :
                        running = False
                        pygame.quit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key >= pygame.K_a and event.key <= pygame.K_z:
                            # Si la touche appuyée correspond à une lettre de l'alphabet
                            self.letter = chr(event.key)
                            if self.letter.lower() in game.letters:
                                print("La lettre", self.letter, "existe dans la phrase choisie.")
                                guessed_letters.append(self.letter)
                            else:
                                if self.letter not in properties.wrong_letters :
                                    state.change_state()
                                    properties.wrong_letters.append(self.letter)
                                print("La lettre", self.letter, "n'existe pas dans la phrase choisie.")

                properties.draw_wrong_letters()
                properties.draw_phrase(self.phrase, guessed_letters)

                # victoire
                if all(char.lower() in guessed_letters for char in self.phrase.lower() if char != ' '):

                    # Effacer l'écran
                    properties.screen.fill((255, 255, 255))

                    properties.draw_win()

                    pygame.display.flip()

                    # attendre 5 secondes
                    pygame.time.delay(5000)

                    self.reset_game()

                # défaite
                if state.state == state.st9 :

                    # Effacer l'écran
                    properties.screen.fill((255, 255, 255))

                    properties.draw_loose()

                    pygame.display.flip()

                    # attendre 5 secondes
                    pygame.time.delay(5000)

                    self.reset_game()

                pygame.display.flip()
