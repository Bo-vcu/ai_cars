import sys
import pygame
from settings import *
from state import State
from button import Button

class Menu(State):
    def __init__(self, game_state):
        self.game_state = game_state
        self.smallFont = pygame.font.SysFont('Corbel', int(HEIGHT * 0.03819444444444445))  # resposive: 33 if screen height is 864px, so 33 / 864 = 0.03819444444444445
        self.buttons = [
                        Button(pos = (HALF_WIDTH, HALF_HEIGHT * 0.7685185185185185),  # resposive: - 100px if half screen height is 432px, so 432 - 100 = 332 and 332 / 432 = 0.76851851851851853
                               text_input = "Play with set points",
                               font = self.smallFont,
                               base_color = black,
                               hovering_color = taxi_blue,
                               background_color = white,
                               background_width = HEIGHT * 0.37037037037037035,  # resposive: 320px if screen height is 864px, so 320 / 864 = 0.37037037037037035
                               border_color = black,
                               border_width = 2,
                               radius = 12,
                               game_state = self.game_state,
                               function = self.game_state.__setstate_test2__),
                        Button(pos = (HALF_WIDTH, HALF_HEIGHT),
                               text_input = "Pick your own points",
                               font = self.smallFont,
                               base_color = black,
                               hovering_color = taxi_blue,
                               background_color = white,
                               background_width = HEIGHT * 0.37037037037037035,  # resposive: 320px if screen height is 864px, so 320 / 864 = 0.37037037037037035
                               border_color = black,
                               border_width = 2,
                               radius = 12,
                               game_state = self.game_state,
                               function = self.game_state.__setstate_test1__),
                        Button(pos = (HALF_WIDTH, HALF_HEIGHT * 1.2314814814814814),  # resposive: + 100px if half screen height is 432px, so 432 + 100 = 532 and 532 / 432 = 1.2314814814814814
                               text_input = "Quit",
                               font = self.smallFont,
                               base_color = black,
                               hovering_color = taxi_blue,
                               background_color = white,
                               background_width = HEIGHT * 0.37037037037037035,  # resposive: 320px if screen height is 864px, so 320 / 864 = 0.37037037037037035
                               border_color = black,
                               border_width = 2,
                               radius = 12,
                               game_state = self.game_state,
                               function = self.game_state.quit)
                        ]
        self.image = pygame.image.load("Logo.png")
        image_prop = HEIGHT * 0.23148148148148148
        self.image = pygame.transform.smoothscale(self.image, (image_prop, image_prop))  # resposive: 200px wide if screen height is 864px, so 200 / 864 = 0.23148148148148148
        self.image_rect = self.image.get_rect(center=(HALF_WIDTH, HEIGHT * 0.1736111111111111))  # resposive: 150px if screen height is 864px, so 150 / 864 = 0.1736111111111111

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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_state.quit()
                
        keys = pygame.mouse.get_pressed()

        if keys[0]:
            if not self.left_clicked:
                self.first_left_clicked = True
            self.left_clicked = True
        else:
            self.left_clicked = False
