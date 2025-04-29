import unittest
import pygame
from ship import Ship
from settings import Settings

class DummyGame:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((800, 600))

class ShipMovementTest(unittest.TestCase):
    def setUp(self):
        self.game = DummyGame()
        self.ship = Ship(self.game)

    def test_move_right(self):
        """Перевірити, що корабель рухається праворуч"""
        initial_x = self.ship.rect.x
        self.ship.moving_right = True
        self.ship.update()
        self.assertGreater(self.ship.rect.x, initial_x)

    def test_move_left(self):
        """Перевірити, що корабель рухається ліворуч"""
        initial_x = self.ship.rect.x
        self.ship.moving_left = True
        self.ship.update()
        self.assertLess(self.ship.rect.x, initial_x)

if __name__ == '__main__':
    unittest.main()
