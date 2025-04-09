import pygame
import pytest
from ship import Ship

class MockSettings:
    ship_speed = 1.5

class MockGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.settings = MockSettings()

@pytest.fixture
def game():
    return MockGame()

def test_ship_initial_position(game):
    ship = Ship(game)
    screen_rect = game.screen.get_rect()
    assert ship.rect.midbottom == screen_rect.midbottom
    assert ship.x == float(ship.rect.x)
