import pygame

class Ship:
    """Клас для налаштування корабля"""

    def __init__(self, ai_game):
        """Ініціалізуємо корабель та задаємо його початкову позицію"""

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #Завантажити зображення корабля та отримати його rect
        self.image = pygame.image.load('images/new_ship.png')
        self.rect = self.image.get_rect()

        #Створювати кожний новий корабель знизу екрана по центру
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Намалювати корабель у його поточному розташуванні"""
        self.screen.blit(self.image, self.rect)