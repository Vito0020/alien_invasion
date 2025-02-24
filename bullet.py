import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Клас для керування кулями випущеними з корабля"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #Створити rect кулі у (0, 0) та задати правильну позицію
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_heigth)
        self.rect.midtop = ai_game.ship.rect.midtop

        #Зберегти позицію пулі яе десяткове значення
        self.y = float(self.rect.y)

    def update(self):
        """Перемістити кулю на верх екрану"""
        #Оновити позицію кулі
        self.y -= self.settings.bullet_speed
        #Оновити позицію в rect
        self.rect.y = self.y

    def draw_bullet(self):
        """Намалювати кулю на екрані"""
        pygame.draw.rect(self.screen, self.color, self.rect)