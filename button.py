import pygame
class Button:
    def __init__(self, width, height, x, y, text, font_size = 30):
        self.width = width
        self.height = height
        self.second_width = self.width + 20
        self.second_height = self.height + 20
        self.font_size = font_size
        self.x = x
        self.y = y
        self.border_position = (self.x - 10, self.y - 10)
        self.text = text
        self.font = pygame.font.SysFont('Comic Sans', font_size)
        self.button = pygame.Rect((self.x, self.y), (self.width, self.height))
        self.border = pygame.Rect(self.border_position, (self.second_width, self.second_height))
        self.clicked = False
    def draw_button(self, screen, button_color, text_color, border_color):
        add_text = self.font.render(self.text, True, text_color).get_rect(center=self.button.center)
        pygame.draw.rect(screen, border_color, self.border, border_radius=5)
        pygame.draw.rect(screen, button_color, self.button, border_radius=5)
        screen.blit(self.font.render(self.text, True, text_color), add_text)

    def is_clicked(self, pos):
        return self.button.collidepoint(pos)
