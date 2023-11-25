import pygame

class Button:
    def __init__(self, pos, text_input, font, base_color, hovering_color, background_color, background_width, border_color, border_width, radius, game_state, function):
        self.game_state = game_state
        self.pos = pos
        self.text_input = text_input
        self.font = font
        self.base_color = base_color
        self.hovering_color = hovering_color
        self.background_color = background_color
        self.background_width = background_width
        self.border_color = border_color
        self.border_width = border_width
        self.radius = radius
        self.function = function

        self.text = self.font.render(self.text_input, True, self.base_color)
        self.text_rect = self.text.get_rect(center=pos)
        self.background_rect = pygame.Rect(0, 0, (self.text_rect.w if self.background_width == None else self.background_width), self.text_rect.height * 2.1)  # resposive: + 30 if text height is 33, so 33 - 30 = 63 and 63 / 30 = 2.1
        self.background_rect.center = pos

        self.border_rect = pygame.Rect(0, 0, (self.text_rect.w if self.background_width == None else self.background_width) + self.border_width, self.text_rect.height * 2.1 + self.border_width)  # resposive: + 30 if text height is 33, so 33 - 30 = 63 and 63 / 30 = 2.1
        self.border_rect.center = pos

    def render(self):
        pygame.draw.rect(self.game_state.screen, self.border_color, self.border_rect, border_radius=self.radius)
        pygame.draw.rect(self.game_state.screen, self.background_color, self.background_rect, border_radius=self.radius)

        self.game_state.screen.blit(self.text, self.text_rect)

    def update(self):
        if self.check_collisions(self.game_state.mouse_pos):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
            if self.game_state.state.first_left_clicked:
                self.game_state.state.first_left_clicked = False
                self.function()
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)

    def check_collisions(self, position):
        if position[0] in range(self.background_rect.left, self.background_rect.right) and \
                position[1] in range(self.background_rect.top, self.background_rect.bottom):
            return True
        return False
