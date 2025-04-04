import pygame.font

class Button:

    def __init__(self, ai_game, msg):
        """Ініціалізація атрибутів кнопки"""

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #Задати розміри та властивості кнопки
        self.width, self.height = 200, 50
        self.button_color = (72, 61, 139)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        #Створити об'єкт rect кнопки та розмістити по центру
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        #Повідомлення на кнопці потрібно показати лише один раз
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Перетворити текст на зображення
        та розмістити його по центру кнопки"""

        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Намалювати пусту кнопку, а потім -- повідомлення"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)