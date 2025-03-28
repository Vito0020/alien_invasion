import pygame

from pygame.sprite import Sprite

class Ship(Sprite):
    """Клас для налаштування корабля"""

    def __init__(self, ai_game):
        """Ініціалізуємо корабель та задаємо його початкову позицію"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #Завантажити зображення корабля та отримати його rect
        self.image = pygame.image.load('images/new_ship.png')
        self.rect = self.image.get_rect()

        #Створювати кожний новий корабель знизу екрана по центру
        self.rect.midbottom = self.screen_rect.midbottom

        #Зберегти десяткове значення для позиції корабля по горизонталі
        self.x = float(self.rect.x)

        #Індикатор руху корабля
        self.moving_right = False
        self.moving_left = False

    def center_ship(self):
        """Відцентрувати корабель по екрану"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def update(self):
        """Оновити точну позицію корабля відносно індикатора руху"""
        #Оновити значення ship.x
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        #Оновити значення rect.x
        self.rect.x = self.x

    def blitme(self):
        """Намалювати корабель у його поточному розташуванні"""
        self.screen.blit(self.image, self.rect)