import pygame

class State() :

    def __init__(self) :

        self.st1 = pygame.image.load('assets/state 1.png')
        self.st2 = pygame.image.load('assets/state 2.png')
        self.st3 = pygame.image.load('assets/state 3.png')
        self.st4 = pygame.image.load('assets/state 4.png')
        self.st5 = pygame.image.load('assets/state 5.png')
        self.st6 = pygame.image.load('assets/state 6.png')
        self.st7 = pygame.image.load('assets/state 7.png')
        self.st8 = pygame.image.load('assets/state 8.png')
        self.st9 = pygame.image.load('assets/state 9.png')

        self.state_n = 1
        self.state = self.st1

    def reset(self) :
        self.state = self.st1
        self.state_n = 1

    def change_state(self) :
        self.state_n += 1

        if self.state_n == 1 :
            self.state = self.st1
        elif self.state_n == 2 :
            self.state = self.st2
        elif self.state_n == 3 :
            self.state = self.st3
        elif self.state_n == 4 :
            self.state = self.st4
        elif self.state_n == 5 :
            self.state = self.st5
        elif self.state_n == 6 :
            self.state = self.st6
        elif self.state_n == 7 :
            self.state = self.st7
        elif self.state_n == 8 :
            self.state = self.st8
        elif self.state_n == 9 :
            self.state = self.st9

    def getState(self) :
        return self.state