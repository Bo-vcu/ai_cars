import sys
import pygame
from settings import *
from state import State
from button import Button

class Menu(State):
    def __init__(self, game_state):
        self.game_state = game_state
        self.smallFont = pygame.font.SysFont('Corbel', 33)
        self.buttons = [
                        Button(pos = (HALF_WIDTH, HALF_HEIGHT - 100),
                               text_input = "Play with set points",
                               font = self.smallFont,
                               base_color = black,
                               hovering_color = taxi_blue,
                               background_color = white,
                               background_width = 320,
                               border_color = black,
                               border_width = 2,
                               radius = 12,
                               game_state = self.game_state,
                               function = self.game_state.__setstate_game__),
                        Button(pos = (HALF_WIDTH, HALF_HEIGHT),
                               text_input = "Pick your own points",
                               font = self.smallFont,
                               base_color = black,
                               hovering_color = taxi_blue,
                               background_color = white,
                               background_width = 320,
                               border_color = black,
                               border_width = 2,
                               radius = 12,
                               game_state = self.game_state,
                               function = self.game_state.__setstate_game__),
                        Button(pos = (HALF_WIDTH, HALF_HEIGHT + 100),
                               text_input = "Quit",
                               font = self.smallFont,
                               base_color = black,
                               hovering_color = taxi_blue,
                               background_color = white,
                               background_width = 320,
                               border_color = black,
                               border_width = 2,
                               radius = 12,
                               game_state = self.game_state,
                               function = self.game_state.quit)
                        ]
        self.image = pygame.image.load("Logo.png") 
        self.image = pygame.transform.smoothscale(self.image, (200, 200))
        self.image_rect = self.image.get_rect(center=(HALF_WIDTH, 125))

        self.left_clicked = False
        self.first_left_clicked = False

    def update(self):
        for button in self.buttons:
            button.update()

    def render_frame(self):
        self.game_state.screen.fill(grey)
        self.game_state.screen.blit(self.image, self.image_rect)
        for button in self.buttons:
            button.render()

    def process_input(self):
        keys = pygame.mouse.get_pressed()

        if keys[0]:
            if not self.left_clicked:
                self.first_left_clicked = True
            self.left_clicked = True
        else:
            self.left_clicked = False
