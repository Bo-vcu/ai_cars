import pygame
from settings import *
from state import State

class Game(State):
    def __init__(self, game_state):
        self.game_state = game_state

        self.left_clicked = False
        self.first_left_clicked = False

    def update(self):
        pass

    def render_frame(self):
        self.game_state.screen.fill(grey)

    def process_input(self):
        keys = pygame.mouse.get_pressed()

        if keys[0]:
            if not self.left_clicked:
                self.first_left_clicked = True
            self.left_clicked = True
        else:
            self.left_clicked = False
