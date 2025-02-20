import sys

import pygame

class AlienInvasion:
    """Загальний клас програми що керує ресурсами та поведінкою гри"""

    def __init__(self):
        """Ініціалізувати гру, створити ресурси гри"""

        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Запуск головного циклу гри"""
        while True:
            """Відстеження руху клавіатури та мишки"""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            """Показати останній намальований екран"""
            pygame.display.flip()

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()