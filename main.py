import pygame
import sys
from settings import *
from menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(RES)
        self.clock = pygame.time.Clock()
        self.delta_time = 1
        self.state = Menu(self)
        self.mouse_pos = pygame.mouse.get_pos()

    def __setstate__(self, state):
        self.state = state

    def new_game(self):
        self.state = Menu(self)

    def update(self):
        pygame.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pygame.display.set_caption(f'{self.clock.get_fps() :.1f}')
        self.mouse_pos = pygame.mouse.get_pos()
        self.state.update()

    def draw(self):
        self.state.render_frame()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        self.state.process_input()

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == '__main__':
    game = Game()
    game.run()
