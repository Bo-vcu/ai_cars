from state import State
from button import Button
from settings import *
import pygame

class Menu(State):
    def __init__(self, game_state):
        self.game_state = game_state
        self.smallFont = pygame.font.SysFont('Corbel', 32)
        self.buttons = [Button(pos=(HALF_WIDTH, HALF_HEIGHT - 100), text_input="Play with set points",
                            font=self.smallFont,
                            base_color=black, hovering_color=taxi_blue, background_color=white,
                            border_color=yellow, game_state = self.game_state),
                        Button(pos=(HALF_WIDTH, HALF_HEIGHT), text_input="Pick your own points",
                            font=self.smallFont,
                            base_color=black, hovering_color=taxi_blue, background_color=white,
                            border_color=yellow, game_state = self.game_state),
                        Button(pos=(HALF_WIDTH, HALF_HEIGHT + 100), text_input="Quit",
                            font=self.smallFont,
                            base_color=black, hovering_color=taxi_blue, background_color=white,
                            border_color=yellow, game_state = self.game_state)]
        self.menu_image = pygame.image.load("Logo.png") 
        self.menu_image = pygame.transform.smoothscale(self.menu_image, (200, 200))
        self.menu_image_rect = self.menu_image.get_rect(center=(HALF_WIDTH, 150))

    def update(self):
        for button in self.buttons:
            button.update()

    def render_frame(self):
        self.game_state.screen.fill(grey)
        self.game_state.screen.blit(self.menu_image, self.menu_image_rect)
        for button in self.buttons:
            button.render()

    def process_input(self):
        pass