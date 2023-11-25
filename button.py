import pygame

class Button:
    def __init__(self, pos, text_input, font, base_color, hovering_color, background_color, border_color, game_state):
        self.game_state = game_state
        self.pos = pos
        self.text_input = text_input
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.background_color, self.border_color = background_color, border_color

        self.text = self.font.render(self.text_input, True, self.base_color)

        self.text_rect = self.text.get_rect(center=pos)

        self.background_rect = pygame.Rect(0, 0, 320, self.text_rect.height + 30)
        self.background_rect.center = pos
        self.border_rect = pygame.Rect(0, 0, 322, self.text_rect.height + 32)
        self.border_rect.center = pos

    def render(self):
        pygame.draw.rect(self.game_state.screen, self.base_color, self.border_rect, border_radius=12)
        pygame.draw.rect(self.game_state.screen, self.background_color, self.background_rect, border_radius=12)
        self.game_state.screen.blit(self.text, self.text_rect)

    def update(self):
        if self.check_collisions(self.game_state.mouse_pos):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)

    def check_collisions(self, position):
        if position[0] in range(self.background_rect.left, self.background_rect.right) and \
                position[1] in range(self.background_rect.top, self.background_rect.bottom):
            return True
        return False
