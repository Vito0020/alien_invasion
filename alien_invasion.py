import sys

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Загальний клас програми що керує ресурсами та поведінкою гри"""

    def __init__(self):
        """Ініціалізувати гру, створити ресурси гри"""

        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_wight, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        #Задати колір фону
        self.bg_image = pygame.image.load("images/space.bmp")

    def run_game(self):
        """Запуск головного циклу гри"""

        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        # Відстеження руху клавіатури та мишки
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        #Наново перемалювати екран
        #self.screen.fill(self.settings.bg_color)
        self.screen.blit(self.bg_image, (0,0))
        self.ship.blitme()

        #Показати останній намальований екран
        pygame.display.flip()

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()