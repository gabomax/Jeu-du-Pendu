import pygame
import numpy as np

class Game() :

    def __init__(self) :
        self.letters = []

    def reset(self) :
        self.letters = []

    def setLetters(self, guess) :
        li = list(guess)
        letters = np.unique(li)
        self.letters = letters