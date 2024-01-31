import pygame

class Board:
    def __init__(self, color, square_code):
        self.color = color
        self.square_code = square_code
        

    def draw(self, screen):
        square = pygame.Surface((50, 50),None, None, self.color,)
        screen.blit(square,(100, 400))
