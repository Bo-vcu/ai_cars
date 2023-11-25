import pygame
import sys
from settings import *
from menu import Menu
from test2 import Test2
from test import Test1

class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(RES)
        self.clock = pygame.time.Clock()
        self.delta_time = 1
        self.mouse_pos = pygame.mouse.get_pos()
        self.new_game()

    def __setstate__(self, state):
        self.state = state

    def new_game(self):
        self.state = Menu(self)
    
    def __setstate_test1__(self):
        self.state = Test1(self)

    def __setstate_test2__(self):
        self.state = Test2(self)
    
    def __setstate_menu__(self):
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
        self.state.process_input()

    def quit(self):
        pygame.quit()
        sys.exit()

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == '__main__':
    game = Main()
    game.run()
